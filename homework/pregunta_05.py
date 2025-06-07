"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_05():
    data_csv = 'files/input/data.csv'
    valores = {}

    with open(data_csv, 'r',  encoding='utf-8') as data:
        for linea in data:
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            numero = int(columnas[1])
            if letra in valores:
                valores[letra].append(numero)
            else:
               valores[letra] = [numero]
    
    resultado = []
    for letra in sorted(valores):
        max_valor = max(valores[letra])
        min_valor = min(valores[letra])
        resultado.append((letra,max_valor,min_valor))

    return resultado

resultado = pregunta_05()
print("Rta/")
print(resultado)

                
    #"""
    #Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    #por cada letra de la columa 1.

    #Rta/
   # [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    #"""
