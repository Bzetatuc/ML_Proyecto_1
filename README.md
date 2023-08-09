
![image](./Images/readme1.jpg)


# Machine Learning Operations (MLOps)

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <h1 align=center> **ALUMNO BENJAMIN ZELAYA** </h1>


¡Bienvenidos a mi primer proyecto individual de la etapa de labs de la carrera de Data Science! Un gran desafio personal donde intentare hacerlo de la manera mas profesional posible, basandome en el conocimiento adquirido durante toda la etapa de los modulos, para ello, utilizaremos dos datasets Movies_dataset y Credits que utilizaremos para hacer el procesos de extraccion, transformacion y carga de datos (ETL), el proceso de Analisis exploratorio de datos (EDA), Machine Learning y por ultimo desarrollar una API.

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Tienes tu modelo de recomendación dando unas buenas métricas :smirk:, y ahora, cómo lo llevas al mundo real? 

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


# DESCRIPCIÓN DEL PROYECTO 



# **`Carpetas y archivos en repositorio`**

*    "DEF API" : "Contiene los archivos y datasets utilizados para realizar las funciones desarrolladas en la API".

*    "Datasets Sin Modificar": "En esta carpeta se guardan los archivos comprimidos del archivo PI MLOps-20230726T191455Z-001.zip".

*    "ETL - EDA": "Esta carpeta contiene un archivo en formato .ipynb que se utilizó para realizar Transformacion y contiene el archivo con el que se realizó el análisis exploratorio de los datos."
        * Analisis Exploratorio Datos: Contiene archivo .ipynb donde se pueden visualizar graficos y conclusiones.
        * Transformaciones ETL Movies_dataset: Contiene archivos para ETL del archivo movies_datasets, obtenido de PI MLOps-20230726T191455Z-001.zip.
        * Transformaciones ETL credits:Contiene archivos utilizados para hacer ETL del archivo csv credits.csv.
        * datasets princpio ETL: contiene archivos de los datasets utilizados en el proyecto, que fueron modificados y tambien algunos reestructurados.



*   "Images": "Contiene archivos con imganes utilizadas en el Readme."

*   "FASTAPI": "Contiene los archivos utilizados con **`FastAPI`**, entre ellos un zip de datasets comprimidos"

*    "Sist. Recomendacion de Peliculas - Machine Learning": "Contiene un archivo en formato .ipynb en el que se desarrollaron las funciónes
	para crear dos modelos de aprendizaje utilizando el método 'vecinos más cercanos'.

*    "main.py": "Contiene todo el código de la API desarrollada con **`FastAPI`**."

*   "requirements.txt": "Archivo útil para realizar el despliegue en Render."



**`Este proyecto se dividió en varios pasos:`**

+ ETL: Los datos se recopilaron desde un archivo CSV que tiene un Conjunto de datos, estos  conjuntos de datos se subieron a un marco de datos y se exploraron. campos, como **`belongs_to_collection`**, **`production_companies`**,**`production_countries`** y **`spoken_lenguages`** fueron desanidados y unirlos a nuevos datasets que se usaron por ejemplo para las consultas de la API creada. Los valores nulos de los campos **`revenue`**, **`budget`** fueron rellenados por el número **`0`**. Los valores nulos del campo **`release date`** fueron eliminados y las fechas fueron modificadas en formato **`AAAA-mm-dd`**, para posteriormente lograr  crear la columna **`release_year`** donde se pudieron extraer el año de la fecha de estreno de cada una de las peliculas. Se creó la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, donde se dividieron **`revenue / budget`**, poniendo la condicion que cuando no habia datos disponibles para calcularlo, tomara el valor **`0`**. Por ultimo, se eliminaron las columnas **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.


### diccionario que describe cada columna en el conjunto de datos del archivo movies_data_final.csv despues de ETL:

```python
column_description = {
    'id': 'ID de la película',
    'title': 'Título de la película',
    'overview': 'Descripción de la película',
    'popularity': 'Popularidad de la película',
    'vote_average': 'Promedio de votos de la película',
    'vote_count': 'Número de votos de la película',
    'status': 'Estado de la película',
    'original_language': 'Idioma original de la película',
    'runtime': 'Duración de la película en minutos',
    'budget': 'Presupuesto de la película',
    'revenue': 'Ingresos generados por la película',
    'tagline': 'Lema de la película',
    'id_bellongs_to_collection': 'ID de la película en BTC',
    'name_bellongs_to_collection': 'Nombre de la película en BTC',
    'poster_bellongs_to_collection': 'URL del póster de la película en BTC',
    'backdrop_bellongs_to_collection': 'URL del fondo de la película en BTC',
    'Cod_languages': 'Código ISO 639-1 del idioma',
    'name_languages': 'Nombre del idioma',
    'release_year': 'Año de lanzamiento de la película',
    'return': 'Relación entre ingresos y presupuesto de la película',
    'id_companies': 'ID de las compañías de producción',
    'name_companies': 'Nombres de las compañías de producción',
    'Cod_countries': 'Códigos ISO de los países de producción',
    'country_name': 'Nombres de los países de producción',
    'release_date': 'Fecha de lanzamiento de la película'
}

```

### ----- EDA -----

+ EDA **`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_: Se utilizó una amplia visualización de datos y estadísticas resumidas para extraer conocimientos y patrones de los diversos conjuntos de datos. Se analizo la relacion entre diferentes variables, como ser la correlacion entre los diferentes **`generos`** de las peliculas de nuestro dataset, con **`Ingresos`**, **`presupuesto`**, **`tiempo de cada pelicula`**, cuales fueron los **`paises`** con mayor cantidad de peliculas producidas o cual es el **`lenguage`** que mayor cantidad de peliculas tiene producidas.

![image3](./Images/eda%202.png)



![image4](./Images/eda%203.png)



![image5](./Images/eda%204.png)



![image6](./Images/eda%205.png)



### ----- MACHINE LEARNING SISTEMAS DE RECOMENDACION -----


+ **`Sistemas de recomendación`**`: Se construyeron dos sistemas de recomendación diferentes utilizando varias ideas y algoritmos, utilizando modelos de K-Nearest Neighbors o K-NN, vecinos mas cercanos, donde en el contexto de este sistema de recomendación de películas, el modelo de vecinos más cercanos busca películas similares a una película de consulta en términos de dos características: género y popularidad. Para ello, utiliza la métrica de distancia euclidiana para calcular la similitud entre las películas y el segundo sistema de Recomendacion tambien basado en K-Nearest Neighbors o K-NN para recomendar películas basadas en los actores o actrices. El modelo busca similitudes entre las películas basándose en los actores o actrices que participaron en ellas. 



### ----- FUNCIONES API -----


+ **`Desarrollo API`**: utilizando ***FastAPI*** utilizamos funciones para que el usuario realice diferentes consultas:

+ def **cantidad_peliculas_idioma( *`Idioma`: str* )**:
    Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.


+ def **peliculas_times( *`Pelicula`: str* )**:
    Se ingresa una pelicula. Debe devolver la duracion y el año.

+ def **franquicia( *`Franquicia`: str* )**:
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio


+ def **peliculas_por_paises( *`Pais`: str* )**:
    Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
    

+ def **productoras_exitosas( *`Productora`: str* )**:
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
    

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.


### ----- MACHINE LEARNING SISTEMAS DE RECOMENDACION -----

+ def **Pelis_recom( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.


+ def **movie_recommendation_artista( *`Artista`* )**:
    Se ingresa el nombre de un o una artista y te recomienda peliculas en una lista de 5 valores.

<br/>


![image2](./Images/API%20Proyecto.png)


# Link de Demostración de consultas

> `CONSULTAS API`<br>
[Consultas](https://ml-proyecto-individual-henry.onrender.com/docs)



# Video de Demostración

video tutorial de la API, Funciones y Resultados.

> `VIDEO`<br>
<a href="https:  " target="_blank">Video</a>


## **Recursos y links utilizados**

VISUAL STUDIO CODE

+ https://code.visualstudio.com/docs


GITHUB

+ https://docs.github.com/es
 

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/

DRIVE DATASETS HENRY

+ https://drive.google.com/drive/folders/1mfUVyP3jS-UMdKHERknkQ4gaCRCO2e1v


RENDER

+ https://render.com/docs



<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>
