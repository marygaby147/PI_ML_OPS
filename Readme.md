<h1 align=center> Proyecto Individual 1: MACHINE LEARNING OPS </h1>

## Introducción

El **Proyecto Individual 1 de ML OPS** tiene como objetivo crear una API para Steam, una plataforma multinacional de videojuegos, implementando un modelo de recomendación basado en Machine Learning. La API proporcionará una interfaz intuitiva para que los usuarios puedan consultar datos relacionados con géneros de juegos, fechas, puntuaciones basadas en los reseñas hechas por sus usuarios.

## Tecnologías Utilizadas

En este proyecto, se han empleado las siguientes tecnologías:

- **FastAPI**: Un marco de desarrollo web rápido y moderno para construir APIs.
- **Matplotlib**: Una librería para visualización de datos en Python.
- **NLTK (Natural Language Toolkit)**: Utilizado para procesamiento de lenguaje natural.
- **Numpy**: Una librería para cálculos numéricos en Python.
- **Pandas**: Herramienta esencial para el análisis y manipulación de datos.
- **Python**: El lenguaje de programación principal utilizado en el proyecto.
- **Render**: Se utiliza para renderizar gráficos y visualizaciones.
- **Scikit-Learn**: Librería de aprendizaje automático con algoritmos de clasificación, regresión, clustering, entre otros.
- **Seaborn**: Otra librería para visualización de datos en Python.
- **Uvicorn**: Un servidor ASGI para aplicaciones FastAPI.
- **Wordcloud**: Utilizado para generar nubes de palabras.

## Resolución

El proyecto se divide en las siguientes etapas:

### 1. ETL (Extracción, Transformación y Carga)

Se realizó el proceso de ETL en archivos en formato JSON. Los datos fueron transformados y cargados para su posterior análisis y utilización dentro del modelo de Machine Learning. En esta etapa, se creó la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP a las reseñas escritas por los usuarios de los videojuegos y de esta manera facilitar el trabajo del modelo de machine learning a desarrollar. 

### 2. EDA (Exploratory Data Analysis)

El análisis exploratorio de datos se llevó a cabo en el conjunto de datos obtenido durante la etapa de ETL. El objetivo fue identificar relaciones, insights, tendencias y patrones relevantes que servirán para la creación y ejecución del modelo de ML. En esta etapa, se creó una nubes de palabras para tener una idea de cuáles títulos de videojuegos son más frecuentes en las reseñas y horas jugadas, este tipo de gráfico tiene grandes ventajas para el sistema de recomendación. 

### 3. Despliegue de la API

Se creó una API utilizando el módulo FastAPI de Python. La API ofrece 5 funciones que pueden ser consultadas:

- **Función PlayTimeGenre**: Devuelve el año con más horas jugadas para un género específico.

- **Función UserForGenre**: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

- **Función UsersRecommend**: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.

- **Función UsersWorstDeveloper**: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

- **Función Sentiment_analysis**: Devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

### 4. Modelo de Machine Learning

El modelo de Machine Learning desarrollado proporciona recomendaciones precisas y personalizadas de juegos para cada usuario. Se utilizaron algoritmos y técnicas como la similitud del coseno y Scikit-Learn. El modelo se basa en una relación ítem-ítem para hacer recomendaciones similares según el ítem tomado. 

#### Sistema de Recomendación Item-Item:

- **Función recomendacion_juego(id_producto)**: Al ingresar el ID de un producto, en este caso un título de un videojuego la función devuelve una lista con 5 juegos recomendados similares al producto ingresado. 

Por último, se realizó el deployement de esta API utilizando Render.

## Enlaces : 
- [API]
- [Video explicativo]