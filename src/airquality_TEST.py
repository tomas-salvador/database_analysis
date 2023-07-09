'''
Created on 25 oct. 2021

@author: Tomás Salvador
'''

from airquality import *

def main():
    fichero = lee_aire("../data/WHO_AirQuality_Database_2018.csv")
    #Leer número total de registros y dar los tres primeros y tres últimos registros leidos
    print("El número total de registros leídos es", len(fichero)) 
    print("Los tres primeros registros leídos son", fichero[:3])
    print("Los tres últimos registros leídos son", fichero[-3:])
    
    #Filtrar por paises y enseña las ciudades con sus respectivos pm10 de dicho país, utilizaré como ejemplo España
    test_pais = filtra_pais(fichero,"Portugal")
    print("Las ciudades de Portugal de las que tenemos datos pm10 son", test_pais)
    #print() en lugar de \n
    #Devolver el número de valores distintos del atributo año y además devolver este conjunto
    print("Se tienen registros de", len(obtener_conjunto_años(fichero)), "años")
    print("Los años de los que se tiene registro son", obtener_conjunto_años(fichero))
    
    #Calcular la media de los años
    media = media_año(fichero)
    print("La media de los registros leidos para la variable año es", round(media))
    
    #Función que devuelve una lista con el pm10 máximo de cada año
    print("La cantidad de pm10 para cada año es:", obtener_dicc_cantidad_pm10_maxima_de_cada_año(fichero))
    
    test_pais_ordenado = pm10_ordenar(test_pais)
    print("Lista de pm10 ordenado para el pais seleccionado ",test_pais_ordenado)


if __name__ == '__main__':
    main()
