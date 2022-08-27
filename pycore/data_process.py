#########################################1##########################################################
import pycore.scripts as instancia1

#RUTAS DE ARCHIVOS E INDEXES
setArchivos1 = [
    {"path":"data/El Salvador.xls", "starRow":4, "starCol":3},
    {"path":"data/Costa Rica.xls", "starRow":4, "starCol":3},
    {"path":"data/Guatemala.xls", "starRow":4, "starCol":3},
    {"path":"data/Honduras.xls", "starRow":4, "starCol":3},
    {"path":"data/Panama.xls", "starRow":4, "starCol":3},
    {"path":"data/Nicaragua.xls", "starRow":4, "starCol":3}
]

for archivo in setArchivos1:
    instancia1.addExcelFile(archivo["path"], archivo["starRow"], archivo["starCol"])
    #SE ESTANDARIZA EL NOMBRE DEL EXCEL CON EXPRESSION REGULAR
    instancia1.estandarizarColLocal(0, r'([a-zA-Z ]*)')

#curso.test()
#len(curso.getAllData())
finalDf = instancia1.joinAllDataFrames()
finalDf.to_excel("data/finalDf.xlsx")



#########################################2##########################################################
import pycore.scripts as instancia2

setArchivos2 = [
    {"path":"data/our/El Salvador.xls", "starRow":1, "starCol":0},
    {"path":"data/our/Costa Rica.xls", "starRow":1, "starCol":0},
    {"path":"data/our/Guatemala.xls", "starRow":1, "starCol":0},
    {"path":"data/our/Honduras.xls", "starRow":1, "starCol":0},
    {"path":"data/our/Panama.xls", "starRow":1, "starCol":0},
    {"path":"data/our/Nicaragua.xls", "starRow":1, "starCol":0}
]

for archivo in setArchivos1:
    curso.addExcelFile(archivo["path"], archivo["starRow"], archivo["starCol"])
    #SE ESTANDARIZA EL NOMBRE DEL EXCEL CON EXPRESSION REGULAR
    curso.estandarizarColLocal(0, r'([a-zA-Z ]*)')

#curso.test()
#len(curso.getAllData())
finalDf = instancia1.joinAllDataFrames()
finalDf.to_excel("data/our/finalDf.xlsx")