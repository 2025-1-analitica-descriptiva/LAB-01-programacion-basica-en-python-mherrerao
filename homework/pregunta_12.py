"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    data_csv = 'files/input/data.csv'
    suma_por_letra = {}
    with open(data_csv, 'r', encoding='utf-8') as data:
        for linea in data:
            columnas = linea.strip().split('\t')
            if len(columnas) < 5:
                continue
            letra = columnas[0]  # Columna 1
            pares = columnas[4].split(',')  # Columna 5
            suma = 0
            for par in pares:
                if ':' in par:
                    try:
                        valor = int(par.split(':')[1])
                        suma += valor
                    except ValueError:
                        continue
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma
    return dict(sorted(suma_por_letra.items()))

resultado = pregunta_12()
print("Rta/")
print(resultado)


    #"""
    #Genere un diccionario que contengan como clave la columna 1 y como valor
    #la suma de los valores de la columna 5 sobre todo el archivo.

    #Rta/
    #{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    #"""
