"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    data_csv = 'files/input/data.csv'
    contador = {}

    with open(data_csv, 'r', encoding='utf-8') as data:
        for linea in data:
            columnas = linea.strip().split('\t')
            letra = columnas[0]  

            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    resultado = sorted(contador.items())

    return resultado

resultado = pregunta_02()
print("Rta/")
print(resultado)

"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
