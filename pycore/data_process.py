#IMPORTE DE SCRIPTS
import pycore.scripts as curso

#ARCHIVOS CON LA DATA
archivos = [
    "data/El Salvador.xlsx",
    "data/Costa Rica.xlsx",
    "data/Guatemala.xls",
    "data/Honduras.xls",
    "data/Panama.xls",
    "data/Nicaragua.xls"
]

#SE RECORRE CADA UNO PARA CARGAR DATA
for archivo in archivos:
    #SE AGREGA EL NOMBRE DEL EXCEL A INSTANCIA
    curso.addExcelFile(archivo)
    #SE ESTANDARIZA EL NOMBRE DEL EXCEL CON EXPRESSION REGULAR
    curso.standardizeCol('Theatre Name', r'([a-zA-Z ]*)')

#curso.test()
#len(curso.getAllData())
finalDf = curso.joinAllDataFrames()
finalDf.to_excel("data/finalDf.xlsx")

