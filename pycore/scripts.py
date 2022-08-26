#IMPORTE DE PANDAS
import pandas as pd

#IMPORTE PARA EXPRESIONES REGULARES
import re

#IMPORTE DE fuzzywuzzy
from fuzzywuzzy import fuzz
#TEST
#fuzz.ratio('geeksforgeeks', 'geeksgeeks')

allDataFrames = []
currentDataFrame = None
resultDataFrame = None

def addExcelFile(filename):
    #GOBALS
    global currentDataFrame
    #SE LEE EL EXCEL
    df = pd.read_excel (
        filename,
        #EMPIEZA FILA 2
        header=2,
    )
    #SE ELEIMINAN 2 PRIMERAS COLUMNAS
    df = df.iloc[: , 2:]
    
    #SE OBITNE NOMBRE PAIS
    reResults = re.search(r"(\w*/)*([\w ]*)(.\w*)*", filename)
    nombrePais = reResults.group(2)
    #SE AGREGA COLUMNA DEL PAIS CON NOMBRE DEL ARCHIVO AL INICIO DEL DF
    df.insert(loc=0, column='Pais', value=nombrePais)
    
    #SE GUARDA EL DATAFRAME
    currentDataFrame = df
    allDataFrames.append(df)
    
def standardizeCol(colName, regularExpression):
    #GOBALS
    global currentDataFrame
    #SE PASAN ARGUMENTOS A LA FUNCION DE "str.extract" DEL DF
    currentDataFrame[colName] = currentDataFrame[colName].str.extract(regularExpression)

def test():
    for dataF in allDataFrames:
        print(dataF)
        
def getAllData():
    return allDataFrames

def joinAllDataFrames():
    #GOBALS
    global resultDataFrame
    resultDataFrame = pd.concat(allDataFrames)
    return resultDataFrame
