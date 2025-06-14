"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    df = open('files/input/clusters_report.txt', 'r')
    linea1 = re.sub("\s{3,}", "  ", df.readline().strip()).split("  ")
    linea2 = df.readline().replace("\n", "").strip().split("  ")


    for i in range(len(linea1)):
      linea1[i] = (linea1[i].strip().lower()).replace(" ", "_")
      if i == 1 or i == 2:
          linea1[i] = (linea1[i] + ' ' + linea2[i-1].lower()).replace(" ", "_")

    df.readline(), df.readline()

    documento = df.readlines()
    contenido1 = []
    texto = ''
    for line in documento:
        line = re.sub(r"\s{2,}", " ", line.strip()).replace('\n', '')
        print(line)
        line += ' '
        if '%' in line:
            if texto != '': 
                aux = contenido1.pop()
                texto = texto.replace('.', '').strip()
                aux[3] = aux[3] + texto
                contenido1.append(aux)
                texto = ''
            indice = line.index('%')
            sublista = line[:indice].strip().replace(',', '.').split(" ")
            contenido1.append(sublista + [line[indice + 2:]])
        else:
            texto += line

    aux = contenido1.pop()
    texto = texto.replace('.', '').strip()
    aux[3] = aux[3] + texto
    contenido1.append(aux)

    dataframe = pd.DataFrame(contenido1, columns = linea1)
    dataframe['cluster'] = dataframe['cluster'].astype('int64')
    dataframe['cantidad_de_palabras_clave'] = dataframe['cantidad_de_palabras_clave'].astype('int64')
    dataframe['porcentaje_de_palabras_clave'] = dataframe['porcentaje_de_palabras_clave'].astype('float64')

    return dataframe

