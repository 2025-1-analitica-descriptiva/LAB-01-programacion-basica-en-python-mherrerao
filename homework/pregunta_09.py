"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    data_csv = 'files/input/data.csv'
    contador = {}
    with open(data_csv, encoding="utf-8") as data:
        for linea in data:
            columnas = linea.strip().split("\t")
            if len(columnas) >= 5:
                claves = set()
                pares = columnas[4].split(",")
                for par in pares:
                    if ":" in par:
                        clave = par.split(":")[0]
                        claves.add(clave)
                for clave in claves:
                    contador[clave] = contador.get(clave, 0) + 1
    return dict(sorted(contador.items()))

resultado = pregunta_09()
print("Rta/")
print(resultado)

    #"""
    #Retorne un diccionario que contenga la cantidad de registros en que
    #aparece cada clave de la columna 5.

    #Rta/
    #{'aaa': 13,
    # 'bbb': 16,
    # 'ccc': 23,
    # 'ddd': 23,
    # 'eee': 15,
    # 'fff': 20,
    # 'ggg': 13,
    # 'hhh': 16,
    # 'iii': 18,
    # 'jjj': 18}}

    ##"""
