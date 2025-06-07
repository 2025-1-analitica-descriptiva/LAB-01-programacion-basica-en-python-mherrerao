"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    data_csv = 'files/input/data.csv'
    contador = {}

    with open(data_csv, 'r', encoding='utf-8') as data: 
        for linea in data:
            columnas = linea.strip().split('\t')  
            fecha = columnas[2]
            mes = fecha.split('-')[1] 

            if mes in contador:
                contador[mes] += 1
            else:
                contador[mes] = 1

    resultado = sorted(contador.items()) 
    return resultado

resultado = pregunta_04()
print("Rta/")
print(resultado) 



    ##"""
    ##La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    ##cantidad de registros por cada mes, tal como se muestra a continuación.

    ##Rta/
    ##[('01', 3),
     ##('02', 4),
     #('03', 2),
     #('04', 4),
     #('05', 3),
     #('06', 3),
     #('07', 5),
     #('08', 6),
     #('09', 3),
     #('10', 2),
     #('11', 2),
     #('12', 3)]

    ##"""
