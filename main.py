from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

app = FastAPI(title='Proyecto Individual',
            description='Benjamin Zelaya',
            version='0.101.0')


### Ruta raíz
@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>{ Mi primer API - Primer Proyecto individual Data Science}</h1>"


# Encabezado: Funciones


### IDIOMA 

# Cargamos el datasets
# ----------------------------------------------------
# 
df_lenguage = pd.read_csv('df_Languages_Def.csv',encoding='utf-8')

# ruta FastAPI
@app.get("/idioma/{idioma}")
def cantidad_peliculas_idioma(idioma: str):
    idioma = idioma.lower()

    peliculas_idioma = df_lenguage[df_lenguage['original_language'].str.lower() == idioma]

    #cantidad de películas producidas en el idioma consultado
    cantidad_peliculas = len(peliculas_idioma)

    mensaje = f"La cantidad de peliculas producidas en el idioma {idioma.capitalize()} es: {cantidad_peliculas}"
    return mensaje



# DURACION 

# Cargamos el datasets
# ----------------------------------------------------
# 
df_duracion = pd.read_csv('df_duracion_Def.csv',encoding='utf-8')

@app.get("/peliculas_times/{pelicula}")
def peliculas_times(pelicula: str):
    pelicula = pelicula.lower()

    # DataFrame para obtener las filas correspondientes a la película consultada
    pelicula_info = df_duracion[df_duracion['title'].str.lower() == pelicula]

    # Verificaremos si se encontró la película
    if pelicula_info.empty:
        raise HTTPException(status_code=404, detail=f"La película '{pelicula.capitalize()}' no fue encontrada.")

    # duración y año de la película consultada
    duracion = pelicula_info.iloc[0]['runtime'].astype(int)
    año = pelicula_info.iloc[0]['release_year']

    mensaje = f"La pelicula {pelicula} tiene una duración de {duracion} minutos, del Año {año}"
    return mensaje


### FRANQUICIA 

# Cargamos el datasets
# ----------------------------------------------------
# 
df_franquicia = pd.read_csv('df_franquicia_Def.csv',encoding='utf-8')

@app.get("/franquicia/{franquicia}")
def franquicia(Franquicia: str):
    franquicia_lower = Franquicia.lower()

    # filas correspondientes a la franquicia indicada
    peliculas_franquicia = df_franquicia[df_franquicia['franquicia'].str.lower() == franquicia_lower]

    # cantidad de películas 
    cantidad_peliculas = len(peliculas_franquicia)

    # ganancia total / ganancia promedio de la franquicia
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = peliculas_franquicia['revenue'].mean()

    # Formatear los montos de las ganancias
    ganancia_total_str = "u$s {:,.2f}".format(ganancia_total) #utilizo format para visulizar mejor los montos.
    ganancia_promedio_str = "u$s {:,.2f}".format(ganancia_promedio)

    resultado = f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total_str} y una ganancia promedio de {ganancia_promedio_str} de Dolares"
    return resultado



### PAISES  

# Cargamos el datasets
# ----------------------------------------------------
# 
df_paises = pd.read_csv('df_paises_Def.csv',encoding='utf-8')

@app.get("/peliculas_por_paises/{Pais}")
def peliculas_por_paises(Pais: str):
    pais_lower = Pais.lower()

    # Llenare los valores NaN que tiene la columna con una cadena vacía
    df_paises['country_name'] = df_paises['country_name'].fillna('')

    # filas correspondientes al país
    peliculas_pais = df_paises[df_paises['country_name'].str.lower().str.contains(pais_lower)]

    # cantidad de películas producidas en el país
    cantidad_peliculas = len(peliculas_pais)

    resultado_paises = f" En {Pais} se produjeron {cantidad_peliculas} películas"
    return resultado_paises



### PRODUCTORAS EXITOSAS  

# Cargamos el datasets
# ----------------------------------------------------
# 
df_Prod_exitosas = pd.read_csv('df_prod_exitosas_Def.csv',encoding='utf-8')

@app.get("/productoras_exitosas/{Productora}")
def productoras_exitosas(Productora: str):
    productora_lower = Productora.lower()

    # Rellenar los valores faltantes (NaN) en la columna 'name_companies' con una cadena vacía ('')
    df_Prod_exitosas['name_companies'] = df_Prod_exitosas['name_companies'].fillna('')

    # Filas correspondientes a la productora
    peliculas_productora = df_Prod_exitosas[df_Prod_exitosas['name_companies'].str.lower().str.contains(productora_lower)]

    # Total de revenue
    total_revenue = peliculas_productora['revenue'].sum()

    # Cantidad de películas realizadas por la productora
    cantidad_peliculas = len(peliculas_productora)

    # Formatear el revenue como moneda en dólares
    revenue_formateado = "u$s {:,.2f}".format(total_revenue)


    Resultado = f"La productora {Productora} ha tenido un revenue de {revenue_formateado} y ha realizado {cantidad_peliculas} películas"
    return Resultado


### DIRECTOR

# Cargamos el datasets
# ----------------------------------------------------
# 
df_directores_final = pd.read_csv('df_directores_Def.csv',encoding='utf-8')

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director:str):
    nombre_director = nombre_director.lower() 
    #  DataFrame para obtener las filas correspondientes al director consultado
    peliculas_director = df_directores_final[df_directores_final['Nombre Director'] == nombre_director]

    # Calcular el éxito del director medido a través del retorno (ganancia total / costo total)
    costo_total = peliculas_director['budget'].sum()
    ganancia_total = peliculas_director['revenue'].sum()
    retorno_director = ganancia_total / costo_total if costo_total != 0 else 0

    # Crear una lista para almacenar la información de cada película
    peliculas_info = []

    # Recorrer las filas del DataFrame y obtener la información de cada película
    for _, pelicula in peliculas_director.iterrows():
        info_pelicula = {
            'nombre_pelicula': pelicula['title'],
            'fecha_lanzamiento': pelicula['release_date'],
            'retorno_individual': pelicula['return'],
            'costo': pelicula['budget'],
            'ganancia': pelicula['revenue']
        }
        peliculas_info.append(info_pelicula)




        

    # Crearremos un dicc con la información del director y las películas
    resultado = [
         nombre_director,
       retorno_director,
         peliculas_info
    ]

    return resultado


### SISTEMAS DE RECOMENDACION MACHINE LEARNING POR PELICULA
# SISTEMA 1

# Cargamos el datasets
# ----------------------------------------------------
# 

ML_DF1 = pd.read_csv('ML_SistemaRecomendacion_1.csv')


@app.get("/Pelis_recom/{pelicula}")
def Pelis_recom(pelicula):

    movie = ML_DF1[ML_DF1['title'] == pelicula]
    
    if len(movie) == 0:
        return "La película no se encuentra en la base de datos."

    # Obtener el género y la popularidad de la película
    movie_genero = movie['genero'].values[0]
    movie_popularity = movie['popularity'].values[0]

    # matriz de características para el modelo de vecinos más cercanos
    features = ML_DF1[['popularity']]
    genres = ML_DF1['genero'].str.get_dummies(sep=' ')
    features = pd.concat([features, genres], axis=1)

    # Manejar valores faltantes (NaN) reemplazándolos por ceros
    features = features.fillna(0)

    # modelo de vecinos más cercanos
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # Encontrar las películas más similares (excluyendo la película de consulta indicada por usuario)
    _, indices = nn_model.kneighbors([[movie_popularity] + [0] * len(genres.columns)], n_neighbors=6)
    similar_movies_indices = indices[0][1:]  # Excluyendo la primera película que es la misma consulta
    Pelis_recom = ML_DF1.iloc[similar_movies_indices]['title']

    # Si la película de consulta está en la lista de recomendaciones, la eliminamos
    if pelicula in Pelis_recom.tolist():
        Pelis_recom = Pelis_recom[Pelis_recom != pelicula]

    return Pelis_recom





### SISTEMAS DE RECOMENDACION MACHINE LEARNING POR ACTOR/ACTRIZ
# SISTEMA 2

# Cargamos el datasets
# ----------------------------------------------------
# 

movie_df = pd.read_csv('df_sistema_recomendacion_artistas.csv')



@app.get("/movie_recommendation_artista/{Artista}")
def movie_recommendation_artista(Artista):
    Artista = Artista.lower() 
  
    # películas que tengan al actor/actriz especificado en la columna 'Actor'
    movies_with_artista = movie_df[movie_df['Actor'] == Artista]

    if len(movies_with_artista) == 0:
        return "El o la Artista no se encuentra en la base de datos."

    #  matriz de características para el modelo de vecinos más cercanos
    features = movie_df['genero'].str.get_dummies(sep=' ')

    # modelo de vecinos más cercanos solo con las características de género
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(features)

    # películas más similares (excluyendo las películas del actor indicado por usuario)
    indices = nn_model.kneighbors(features.iloc[movies_with_artista.index, :])

    # Recomendar películas similares
    movie_recommendation_artista = movie_df.iloc[indices[1][0][1:]]['title']

    return  movie_recommendation_artista
  









if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
