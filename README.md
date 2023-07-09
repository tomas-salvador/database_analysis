# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/22)
Autor/a: tomas-salvador;

El proyecto tiene como objetivo analizar los datos de la calidad de aire a nivel global publicados en el dataset de Kaggle que se puede descargar de la siguiente URL (http://kaggle.com/erelin6613/ambient-air-quality-database-who). En el dataset no se ha realizado ninguna modificación a pesar de no tener en ciertas ocasiones algún dato. Este dataset cuenta con 30 columnas.

## Estructura de las carpetas del proyecto

* **/src**: Contiene los dos módulos de Python que forman el proyecto. Estos son airquality.py y airquality_TEST.py
    * **airquality.py**: Contiene funciones para explotar los datos sobre la calidad del aire.
    * **airquality_TEST.py**: Contiene funciones de test para probar las funciones del módulo `airquality.py`. En este módulo está el main.
* **/data**: Contiene el dataset del proyecto
    * **WHO_AirQuality_Database_2018.csv**: Archivo con los datos de calidad de aire que van a ser explotados.
        
## Estructura del *dataset*

Cada fila del dataset recoge los datos de una ciudad del globo. Los datos son de tipo str porque cuando no existe un dato de una ciudad se define con NA. De esta forma el proyecto no dará error, excepto el dato pm10 que se ha declarado como float para poder trabajar directamente con el sin realizar ninguna conversión. Existe un total de 15 datos con la siguiente descripción:

* **ID WHO city**: Identifica con un número entero una ciudad.
* **iso3**: Representa un país mediante tres letras.
* **country**: Identifica un país por su nombre.
* **city**: Representa una ciudad por su nombre.
* **pm10**: Identifica el nivel de partículas de polvo dispersas en el aire.
* **Year**: Representa el año en el que fueron tomados los valores.
* **type_of_stations**: Identifica cuántas estaciones toman datos para esa zona y el tipo de zona.
* **pm10_type**: Representa el nivel de concentración de PM10
* **pm25**: Identifica un tipo de partículas muy pequeñas que se encuentran suspendidas en el aire.
* **pm25_type**: Representa el nivel de concentración de PM2.5.
* **reference**: Identifica la institución que se encarga de la toma de datos de esa zona.
* **latitude**: Representa la latitud en la que se encuentra la estación de toma de datos.
* **longitude**: Identifica la longitud en la que se encuentra la estación de toma de datos.
* **population**: Representa el número de población de la zona
* **wbinc16_text**: Identifica el nivel de ingresos medios en la zona.
* **region**: Representa de otra manera la zona en la que se toman los datos.
* **date_compiled**: Identifica el año en el que se tomaron los primeros datos.
* **population_source**: Representa la fuente de población de la zona.
* **tempcov_PM10**: Identifica el nivel de temperatura durante la toma de datos de PM10.
* **tempcov_PM25**: Representa el nivel de temperatura durante la toma de datos de PM2.5.
* **latitude_pop**: Identifica otra forma de mostrar la latitud en la que se encuentra la estación de toma de datos.
* **longitude_pop**: Representa otra forma de mostrar la longitud en la que se encuentra la estación de toma de datos.
* **Region**: Identifica la región geográfica en la que se toman los datos.
* **region_abbr**: Representa de forma más abreviada la región geográfica en la que se toman los datos.
* **tempcov_PM10_grad**: Identifica en grados celsius el nivel de temperatura durante la toma de datos de PM10.
* **tempcov_PM25_grad**: Representa en grados celsius el nivel de temperatura durante la toma de datos de PM2.5.
* **conc_pm25**: Identifica los valores entre los que se encuentra el nivel de PM2.5 en la zona estudiada.
* **color_pm25**: Se utiliza de forma representativa un color para designar el nivel de PM2.5.
* **conc_pm10**: Representa los valores entre los que se encuentra el nivel de PM10 en la zona estudiada.
* **color_pm10**: Se utiliza de forma representativa un color para designar el nivel de PM10.

## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

RegistroAire = namedtuple("RegistroAire", "id_who_ciudad,iso3,pais,ciudad,pm10,año,tipo_de_estaciones,tipo_de_pm10,pm25,
tipo_de_pm25,referencia,latitud,longitud,poblacion,texto_binc16,region,fecha_compilada,fuente_de_poblacion,tempcov_PM10,tempcov_PM25,
latitud_pop,longitud_pop,region2,region_abbr,tempcov_PM10_grad,tempcov_PM25_grad,conc_pm25,color_pm25,conc_pm10,color_pm10")

La principal decisión de poner todos los datos en forma de str es porque cuando no existe un valor el dataset escribe NA, excepto el dato pm10 que se ha indicado como float para poder 
trabajar directamente con el valor.

## Funciones implementadas
El módulo principal es el módulo airquality.py, y el módulo de pruebas es airquality_TEST.py
En este proyecto se han implementado las siguientes funciones:

### Módulo airquality
  
  * **lee_aire(fichero)**: Lee los datos del fichero csv y devuelve una lista de tuplas con los datos del fichero.
  * **filtra_pais(registros,pais)**: Función que filtra por un país y muestra una lista de tuplas con las ciudades y el valor de pm10 para esa ciudad.
  * **obtener_conjunto_años(fichero)**: Función que devuelve el número de valores distintos para un año
  * **media_año(lista_aire)**: Funcion que calcula la media de cada año
  * **pm10_maximo_año(fichero,año)**: Función que devuelve el valor máximo de pm10 para un año
  * **def pm10_ordenar(lista_tuplas): Función que ordena la lista de ciudades por el valor del pm10
  * **obtener_dicc_cantidad_pm10_maxima_de_cada_año(registros): Funcion que devuelve un diccionario con la clave año y una lista de valores de pm10 para ese año

### Módulo airquality_TEST
En el módulo de pruebas solo se ha definido main para hacer print utilizando las funciones del módulo airquality
