from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import zipfile

#Creamos la instancia de Fastapi

uvicorn main:app --reload

#----------------------------------------------------
app = FastAPI()          
#----------------------------------------------------

# datasets
# ----------------------------------------------------
df_Languages = None
df_timepelicula = None
df_franquicia = None
df_Paises = None
df_Prod_exitosas = None
df_directores_final = None
df_Recomen_data = None
df_movies_with_artista = None



@app.on_event('startup')
async def startup():
    global df_Languages, df_timepelicula, df_franquicia, df_Paises, df_Prod_exitosas,df_directores_final,df_Recomen_data,df_movies_with_artista
    
    zip_file = 'data_1.0.2.zip'
    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('../data/')  # Descomprime los archivos en el directorio '../data/'
    

    df_Languages = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_Languages_Def.csv')
    df_timepelicula = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_duracion_Def.csv')
    df_franquicia = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_franquicia_Def.csv')
    df_Paises = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_paises_Def.csv')
    df_Prod_exitosas = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_prod_exitosas_Def.csv')
    df_directores_final = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_directores_Def.csv')
    df_Recomen_data = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/ML_SistemaRecomendacion1.csv')
    df_movies_with_artista = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/df_ML_SistRecomendacion.csv')
    

def extract_zip():
    return df_Languages, df_timepelicula, df_franquicia, df_Paises, df_Prod_exitosas,df_directores_final,df_Recomen_data,df_movies_with_artista


# Funcion Machine Learning - "K-neighbors"

def Pelis_recom(pelicula):

    # Cargar el archivo CSV con los datos
    _, _, _, _, df_Recomen_data = extract_zip()
    # df_Recomen_data = pd.read_csv('../ML_Proyecto_Individual_Henry/FASTAPI/ML_SistemaRecomendacion1.csv'')

     # Convertir el título de la película a minúsculas
    movie_pelis = movie_pelis.lower()

    # Buscar la película por título en la columna 'title'
    movie_pelis = df_Recomen_data[df_Recomen_data['title'] == pelicula]

    if len(movie_pelis) == 0:
        return "La película no se encuentra en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genero = movie_pelis['genero'].values[0]
    movie_popularity = movie_pelis['popularity'].values[0]

    # matriz de características para el modelo de vecinos más cercanos
    features = movie_pelis[['popularity']]
    genres = movie_pelis['genero'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares (excluyendo la película de consulta indicada por usuario)
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)
    similar_movies_indices = indices[0][1:]  # Excluyendo la primera película que es la misma consulta
    Pelis_recom = movie_pelis.iloc[similar_movies_indices]['title']

    # Si la película de consulta está en la lista de recomendaciones, la eliminamos
    if pelicula in Pelis_recom.tolist():
        Pelis_recom = Pelis_recom[Pelis_recom != pelicula]

    return Pelis_recom


# Ejemplo de uso de la función

# pelicula = 'Ace Ventura: When Nature Calls'
# peliculas_recomendadas = Pelis_recom(pelicula)
# print(f"Películas recomendadas para '{pelicula}':")
#   print(peliculas_recomendadas)
# ----------------------------------------------------

# endpoints
# ----------------------------------------------------
# Ruta para el archivo index.html

@app.get("/",response_class=HTMLResponse, tags=['Index'])
async def read_index_html():
    """
    Ruta para el archivo index.html.
    """
    with open("index.html") as f:
        return f.read()



# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

