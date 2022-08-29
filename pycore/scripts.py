#IMPORTE DE PANDAS
import pandas as pd

#IMPORTE PARA EXPRESIONES REGULARES
import re

#IMPORTE DE fuzzywuzzy
from fuzzywuzzy import fuzz
from itertools import product
from fuzzywuzzy.fuzz import ratio

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
    #GLOBALS
    global resultDataFrame
    resultDataFrame = pd.concat(allDataFrames)
    return resultDataFrame

def find_closest(make):
    return df[df['make'] == ratios.loc[ratios[ratios['k1'] == make]['ratio'].argmax(), 'k2']].index.values[0]

def keysFromCol(dframe, colNumber):
    col = dframe.iloc[:, colNumber]
    keys = list(set(col))
    return keys

def dfRatios(keys):
    ratios = pd.DataFrame([{'k1': k1, 'k2': k2, 'ratio': ratio(k1, k2)} for k1, k2 in product(keys, keys) if k1 != k2])
    return ratios

def estandarizarColPeliculas(colNumber, accuracy):
    #GOBALS
    global currentDataFrame
    tittleKeys = list(set(currentDataFrame.iloc[:, colNumber]))
    ratios = pd.DataFrame([{'k1': k1, 'k2': k2, 'ratio': ratio(k1, k2)} for k1, k2 in product(keys, keys) if k1 != k2])
