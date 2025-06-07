"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    data_csv = 'files/input/data.csv'
    resultado = []
    with open(data_csv, encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            col4 = columnas[3].split(",")
            col5 = columnas[4].split(",")
            resultado.append((letra, len(col4), len(col5)))
    return resultado

resultado = pregunta_10()
print("Rta/")
print(resultado)


    #Retorne una lista de tuplas contengan por cada tupla, la letra de la
    #columna 1 y la cantidad de elementos de las columnas 4 y 5.

    #Rta/
    #[('E', 3, 5),
    # ('A', 3, 4),
    # ...
    # ('E', 2, 3),
    # ('E', 3, 3)]


    #""""""
