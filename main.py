# Se Importan las Librerias a utilizar. 

from fastapi import FastAPI
import uvicorn
from routers.funciones import router as steam_router
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

app=FastAPI()#debug=True)

@app.get('/')
def message():
    return 'PROYECTO INTEGRADOR ML OPS 01 MARIA PACHECO - agregar /docs al enlace para acceder a las funciones'

app.include_router(steam_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=10000)