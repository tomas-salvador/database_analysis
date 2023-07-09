'''
Created on 25 oct. 2021

@author: Tomás Salvador
'''

import csv
from collections import namedtuple
from datetime import datetime

RegistroAire=namedtuple("RegistroAire", "id_who_ciudad,iso3,pais,ciudad,pm10,año,tipo_de_estaciones,tipo_de_pm10,pm25,tipo_de_pm25,referencia,latitud,longitud,poblacion,texto_binc16,region,fecha_compilada,fuente_de_poblacion,tempcov_PM10,tempcov_PM25,latitud_pop,longitud_pop,region2,region_abbr,tempcov_PM10_grad,tempcov_PM25_grad,conc_pm25,color_pm25,conc_pm10,color_pm10")


#Primera entrega:

#Función que lea los datos del fichero y devuelva una lista de tuplas con dicha información.
def lee_aire(fichero):
    lista_aire=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for id_who_ciudad,iso3,pais,ciudad,pm10,año,tipo_de_estaciones,tipo_de_pm10,pm25,tipo_de_pm25,referencia,latitud,longitud,poblacion,texto_binc16,region,fecha_compilada,fuente_de_poblacion,tempcov_PM10,tempcov_PM25,latitud_pop,longitud_pop,region2,region_abbr,tempcov_PM10_grad,tempcov_PM25_grad,conc_pm25,color_pm25,conc_pm10,color_pm10 in lector:
            id_who_ciudad=str(id_who_ciudad)
            iso3=str(iso3)
            pais=str(pais)
            ciudad=str(ciudad)
            pm10=float(pm10)
            año=int(año)
            tipo_de_estaciones=str(tipo_de_estaciones)
            tipo_de_pm10=str(tipo_de_pm10)
            pm25=str(pm25)
            tipo_de_pm25=str(tipo_de_pm25)
            referencia=str(referencia)
            latitud=str(latitud)
            longitud=str(longitud)
            poblacion=str(poblacion)
            texto_binc16=str(texto_binc16)
            region=str(region)
            fecha_compilada=str(fecha_compilada)
            fuente_de_poblacion=str(fuente_de_poblacion)
            tempcov_PM10=str(tempcov_PM10)
            tempcov_PM25=str(tempcov_PM25)
            latitud_pop=str(latitud_pop)
            longitud_pop=str(longitud_pop)
            region2=str(region2)
            region_abbr=str(region_abbr)
            tempcov_PM10_grad=str(tempcov_PM10_grad)
            tempcov_PM25_grad=str(tempcov_PM25_grad)
            conc_pm25=str(conc_pm25)
            color_pm25=str(color_pm25)
            conc_pm10=str(conc_pm10)
            color_pm10=str(color_pm10)

            r = RegistroAire(id_who_ciudad,iso3,pais,ciudad,pm10,año,tipo_de_estaciones,tipo_de_pm10,pm25,tipo_de_pm25,referencia,latitud,longitud,poblacion,texto_binc16,region,fecha_compilada,fuente_de_poblacion,tempcov_PM10,tempcov_PM25,latitud_pop,longitud_pop,region2,region_abbr,tempcov_PM10_grad,tempcov_PM25_grad,conc_pm25,color_pm25,conc_pm10,color_pm10)
            lista_aire.append(r)
    return lista_aire

#Segunda entrega:


#Función que filtra por paises y enseña las ciudades con sus respectivos pm10 de dicho país, utilizaré como ejemplo España
def filtra_pais(registros,pais):
    lista_tuplas = []
    for registro in registros:
        if registro.pais == pais:
            ciudad = registro.ciudad
            pm10 = registro.pm10
            tupla=(ciudad, pm10)
            lista_tuplas.append(tupla)
    return lista_tuplas


#Función que devuelve el número de valores distintos del atributo año y además devuelve este conjunto
def obtener_conjunto_años(fichero):
    return {tupla.año for tupla in fichero}

#Función que calcula la media de los años
def media_año(lista_aire):
    suma = 0
    for elemento in lista_aire:
        suma = suma + elemento[5]
    
    media = suma / len(lista_aire)
    return media

#Funciones que enseñen el valor máximo de pm10 para un años
def pm10_maximo_año(fichero,año): #función auxiliar que a partir de una lista de tuplas y un año, obtiene el viento máximo de ese año
    lista_datos_año= [tupla for tupla in fichero if tupla.año==año]
    tupla_pm10_max= max(lista_datos_año, key=lambda x:x.pm10)
    
    return tupla_pm10_max.pm10

#Funcion que ordena la lista de ciudades por el valor de pm10
def pm10_ordenar(lista_tuplas):
    orden_por_pm10 = sorted(lista_tuplas, key=lambda tup: tup[1])
    return orden_por_pm10

#Funcion que devuelve un diccionario con la clave año y una lista de valores de pm10
#para ese año.
def obtener_dicc_cantidad_pm10_maxima_de_cada_año(registros):
    conj_años = obtener_conjunto_años(registros)
    dicc={}
    
    #para cada año 
    for a in conj_años:
        #para empezar le pongo un valor de una lista vacía a la clave año
        dicc[a] = []
        
        #recorro los registros para cada año
        for registro in registros:
            
            #Si el año del registro es igual al año que vamos procesando
            if registro.año == a:
                    #recupero el valor de la clave a que tiene el diccionario
                    valor = dicc.get(a)
                    #como el valor es una lista le añado el registro pm10
                    valor.append(registro.pm10)
                    #actualizo la clave a con la nueva lista con el valor añadido
                    dicc[a] = valor
    
    return dicc
 
#Entrega 3



    