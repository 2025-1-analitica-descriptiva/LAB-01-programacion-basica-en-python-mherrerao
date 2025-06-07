"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    data_csv = 'files/input/data.csv'
    suma_por_letra = {}
    with open(data_csv, 'r', encoding='utf-8') as data:
        for linea in data:
            columnas = linea.strip().split('\t')
            if len(columnas) < 4:
                continue  # evitar errores si hay filas incompletas
            try:
                valor = int(columnas[1])  # columna 2
            except ValueError:
                continue
            letras = columnas[3].split(',')  # separar la columna 4 por comas
            for letra in letras:
                letra = letra.strip()  # eliminar espacios en blanco alrededor
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor
                else:
                    suma_por_letra[letra] = valor
    return dict(sorted(suma_por_letra.items()))

resultado = pregunta_11()
print("Rta/")
print(resultado)

    #"""
    #Retorne un diccionario que contengan la suma de la columna 2 para cada
    #letra de la columna 4, ordenadas alfabeticamente.

    #Rta/
    #{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    #"""
