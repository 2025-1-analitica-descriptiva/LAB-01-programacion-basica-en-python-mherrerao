"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01 ():
    data_csv = 'files/input/data.csv'
    indice_columna = 1 
    suma = 0 

    with open(data_csv, 'r', encoding='utf-8') as data: 
        lineas = data.readlines() 

        for linea in lineas:
            cols = linea.strip().split("\t")
            ## print(cols)
            if len(cols)>indice_columna: 
                valor = cols[indice_columna]
                if valor:
                    try: 
                        suma+= int(valor)
                    except ValueError:
                        print(f'valor no valido: {valor}')
            
    return (suma) 

resultado = pregunta_01 ()
print('Rta/')
print(resultado)  


"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
