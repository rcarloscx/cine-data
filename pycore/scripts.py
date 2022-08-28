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

def addExcelFile(filename, starRow, starCol):
    #GOBALS
    global currentDataFrame
    #SE LEE EL EXCEL
    df = pd.read_excel (
        filename,
        header=starRow,
    )
    #SE ELIMINAN COLUMNAS SEGUN starCol
    df = df.iloc[: , starCol:]
    
    #SE GUARDA EL DATAFRAME
    currentDataFrame = df
    allDataFrames.append(df)

def addColCountryFile(filename):
    #SE OBITNE NOMBRE PAIS
    reResults = re.search(r"(\w*/)*([\w ]*)(.\w*)*", filename)
    nombrePais = reResults.group(2)
    #SE AGREGA COLUMNA DEL PAIS CON NOMBRE DEL ARCHIVO AL INICIO DEL DF
    currentDataFrame.insert(loc=0, column='Pais', value=nombrePais)

def estandarizarColLocal(colIndex, regularExpression):
    #GOBALS
    global currentDataFrame
    #SE PASAN ARGUMENTOS A LA FUNCION DE "str.extract" DEL DF actual acorde la posicion
    currentDataFrame.iloc[:, colIndex] = currentDataFrame.iloc[:, colIndex].str.extract(regularExpression)

def test(colIndex):
    #GOBALS
    global allDataFrames
    #return currentDataFrame.iloc[:, colIndex]
        
def getAllData():
    #GOBALS
    global allDataFrames
    return allDataFrames

def getCurrentData():
    #GOBALS
    global currentDataFrame
    return currentDataFrame

def joinAllDataFrames():
    #GOBALS
    global resultDataFrame
    resultDataFrame = pd.concat(allDataFrames)
    return resultDataFrame

def estandarizarColPeliculas(colNumber, accuracy):
    #GOBALS
    global currentDataFrame
    print("STILL")
