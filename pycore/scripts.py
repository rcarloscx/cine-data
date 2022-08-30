#IMPORTE DE PANDAS
import pandas as pd
#IMPORTE PARA EXPRESIONES REGULARES
import re

#IMPORTE DE fuzzywuzzy
from fuzzywuzzy import fuzz
from itertools import product
from fuzzywuzzy.fuzz import ratio

#READ jsonFile
import json

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
    filename = filename.replace("_", " ", 1)
    reResults = re.search(r"([\w-]*/)*([\w _]*)(.\w*)*", filename)
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

def diccionarioPeliculas(ratios, accuracy):
    diccionario={}
    print(ratios[ratios["ratio"]>70])
    for index, row in ratios.iterrows():
        #Cumple probabilidad
        if row["ratio"] >= accuracy:
            #Verificar si exite en diccionario, sino crearle conceptop array
            keyText = row["k1"]
            valText = row["k2"]

            #Buscar val internamente
            valueFound = False
            for vals in diccionario:
                if valText in vals:
                    valueFound = True
                    break
            #Si val existe, no hacer nada
            if valueFound:
                continue

            #Si no existe val internos, buscar en keys
            keyFound = False
            keyFound = keyText in diccionario
            #Si val existe, no hacer nada
            if not keyFound and not valueFound:
                diccionario[keyText] = [keyText, valText]
                continue
            diccionario[keyText].append(valText)
            #diccionario[keyText] = [valText]
            
    return diccionario

def findKeyFromValue(diccionario, value):
    #Pelicula con diferentes nombres
    for setPelis in diccionario:
        if value in setPelis:
            return setPelis[0]
    #Pelicula Unica
    return value

def loadDicFromFile():
    return json.load(open('diccionario.json'))

def estandarizarColPeliculas(colNumber, accuracy):
    #GOBALS
    global currentDataFrame
    #tittleKeys = list(set(currentDataFrame.iloc[:, colNumber]))
    #ratios = pd.DataFrame([{'k1': k1, 'k2': k2, 'ratio': ratio(k1, k2)} for k1, k2 in product(tittleKeys, tittleKeys) if k1 != k2])
    #diccionario = diccionarioPeliculas(ratios, accuracy)
    #SE SUSTITUYE EL NOMBRE DE LA PELICULA SEGUN DICCIONARIO
    diccionario = loadDicFromFile()
    currentDataFrame.iloc[:, colNumber] = currentDataFrame.iloc[:, colNumber].apply(lambda x: findKeyFromValue(diccionario, x))
    return currentDataFrame
