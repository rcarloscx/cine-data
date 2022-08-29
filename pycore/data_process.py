#########################################1##########################################################
import scripts as instancia1

#RUTAS DE ARCHIVOS E INDEXES
setArchivos1 = [
    {"path":"data/El Salvador.xls", "starRow":2, "starCol":2},
    {"path":"data/Costa Rica.xls", "starRow":2, "starCol":2},
    {"path":"data/Guatemala.xls", "starRow":2, "starCol":2},
    {"path":"data/Honduras.xls", "starRow":2, "starCol":2},
    {"path":"data/Panama.xls", "starRow":2, "starCol":2},
    {"path":"data/Nicaragua.xls", "starRow":2, "starCol":2}
]

for archivo in setArchivos1:
    instancia1.addExcelFile(archivo["path"], archivo["starRow"], archivo["starCol"])
    #SE ESTANDARIZA EL NOMBRE DEL CINE
    instancia1.estandarizarColLocal(0, r'([a-zA-Z ]*)')
    
    #SE ESTANDARIZA EL NOMBRE DE LAS PELICULAS CON UN 50% COINCIDENCIA
    instancia1.estandarizarColPeliculas(1, 0.5)
    
    #SE AGREGA COLUNNA PAIS SEGUN NOMBRE DEL ARCHIVO
    instancia1.addColCountryFile(archivo["path"])

#curso.test()
#len(curso.getAllData())
finalDf = instancia1.joinAllDataFrames()
#ELIMINANDO COLUMNAS DINERO REPETIDAS 
finalDf=finalDf.drop(['mf_friday $', 'mf_thursday $','mf_saturday $'
,'mf_sunday $','mf_wkend_rev $','mf_monday $','mf_tuesday $','mf_wednesday $','mf_rev $'],axis=1)
#ELIMINANDO COLUMNAS PORCENTAJES
finalDf=finalDf.drop(['%','%.1','%.2','%.3','%.4','%.5','%.6','%.7','%.8','%.9','%.10','%.11'
,'%.12','%.13','%.14','%.15','%.16','%.17'],axis=1)
#ELIMINANDO COLUMNAS VISITANTES REPETIDAS
finalDf=finalDf.drop(['mf_thursday_xtns','mf_saturday_xtns','mf_sunday_xtns','mf_monday_xtns','mf_tuesday_xtns'
,'mf_wednesday_xtns','mf_friday_xtns','mf_thursday_xtns.1','mf_xtns'],axis=1)
finalDf.to_excel("data/finalDf.xlsx", index=False)

#Formato de las columnas con dos decimales
finalDf['Thu 18-Aug $'] = finalDf['Thu 18-Aug $'].apply('{:.2f}'.format)
finalDf['Fri 19-Aug $'] = finalDf['Fri 19-Aug $'].apply('{:.2f}'.format)
finalDf['Sat 20-Aug $'] = finalDf['Sat 20-Aug $'].apply('{:.2f}'.format)
finalDf['Sun 21-Aug $'] = finalDf['Sun 21-Aug $'].apply('{:.2f}'.format)
finalDf['Weekend\nGross $'] = finalDf['Weekend\nGross $'].apply('{:.2f}'.format)
finalDf['Mon 22-Aug $'] = finalDf['Mon 22-Aug $'].apply('{:.2f}'.format)
finalDf['Tue 23-Aug $'] = finalDf['Tue 23-Aug $'].apply('{:.2f}'.format)
finalDf['Wed 24-Aug $'] = finalDf['Wed 24-Aug $'].apply('{:.2f}'.format)
finalDf['Week\nGross $'] = finalDf['Week\nGross $'].apply('{:.2f}'.format)


#########################################2##########################################################
import scripts as instancia2

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
finalDf.to_excel("data/our/finalDf.xlsx", index=False)
