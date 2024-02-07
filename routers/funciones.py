from fastapi import APIRouter
import pandas as pd
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


router = APIRouter()


df = pd.read_parquet('dataset_final.parquet.gz')
df_games = pd.read_parquet('output_steam_games_clean.parquet.gz')


# Función que devuelve el año con más horas jugadas para dicho género.

@router.get('/PlayTimeGenre/{genre}')
def PlayTimeGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    max_playtime_year = year_playtime_df.loc[year_playtime_df['playtime_forever'].idxmax(), 'year']
    return {"Género": genre, "Año de lanzamiento con más horas jugadas para Género" : int(max_playtime_year)}
    


# Función que devuelve el usuario que acumula más horas jugadas para el género dado 
# y una lista de la acumulación de horas jugadas por año.

@router.get('/UserForGenre/{genre}')
def UserForGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    max_playtime_user = genre_df.loc[genre_df['playtime_forever'].idxmax(), 'user_id']
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    playtime_list = year_playtime_df.to_dict(orient='records')
    result = {
        "Usuario con más horas jugadas para Género " + genre: max_playtime_user,
        "Horas jugadas": playtime_list}
    return result


# Función que devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.

@router.get('/UsersRecommend/{year}')
def UsersRecommend(year: int) -> dict:
    df_filtrado = df[(df['year'] == year) & (df['recommend'] == True) & (df['sentiment_analysis'] >= 1)]
    if df_filtrado.empty:
        return {"error": 'Valor no encontrado'}
    df_ordenado = df_filtrado.sort_values(by='sentiment_analysis', ascending=False)
    top_3_reseñas = df_ordenado.head(3)
    resultado = {
        "Top 1": top_3_reseñas.iloc[0]['title'],
        "Top 2": top_3_reseñas.iloc[1]['title'],
        "Top 3": top_3_reseñas.iloc[2]['title']
    }
    return resultado



# Función que devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

@router.get('/UsersWorstDeveloper/{year}')
def UsersRecommend(year: int) -> dict:
    df_filtrado = df[(df['year'] == year) & (df['recommend'] == False) & (df['sentiment_analysis'] == 0 )]
    if df_filtrado.empty:
        return {"error": 'Valor no encontrado'}
    df_ordenado = df_filtrado.sort_values(by='sentiment_analysis', ascending=False)
    top_3_reseñas = df_ordenado.head(3)
    resultado = {
        "Top 1": top_3_reseñas.iloc[0]['publisher'],
        "Top 2": top_3_reseñas.iloc[1]['publisher'],
        "Top 3": top_3_reseñas.iloc[2]['publisher']
    }
    return resultado

# Función que devuelve el sentiment analysis segun el año.

@router.get('/sentiment_analysis/')
def sentiment_analysis(publisher : str) -> dict:
    filtered_df = df[df['publisher'] == publisher]
    sentiment_counts = filtered_df['sentiment_analysis'].value_counts()
    result = {
        "Positive": int(sentiment_counts.get(2, 0)),
        "Neutral": int(sentiment_counts.get(1, 0)),
        "Negative": int(sentiment_counts.get(0, 0))
    }
    return result


# Modelo de Recomendación relación ítem-ítem aplicando la similitud del coseno

muestra = df_games
tfidf = TfidfVectorizer(stop_words='english')
muestra=muestra.fillna("")
tdfid_matrix = tfidf.fit_transform(muestra['title'])
cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix)
 
@router.get('/recomendacion_id/{id_producto}')
def recomendacion(id_producto: int):
    if id_producto not in muestra['id'].values:
        return {'mensaje': 'No existe el id del producto.'}
    else:  
         
        filtered_df = muestra[muestra['id'] != id_producto]
    
        tdfid_matrix_filtered = tfidf.transform(filtered_df['title'])
        cosine_similarity_filtered = linear_kernel(tdfid_matrix_filtered, tdfid_matrix_filtered)

        idx = muestra[muestra['id'] == id_producto].index[0]
        sim_cosine = list(enumerate(cosine_similarity_filtered[idx]))
        sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
        sim_ind = [i for i, _ in sim_scores[1:6]]
        sim_juegos = filtered_df['title'].iloc[sim_ind].values.tolist()

    return {'juegos recomendados': list(sim_juegos)}