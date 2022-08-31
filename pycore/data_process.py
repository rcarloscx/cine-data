#########################################1##########################################################
## Instancia 1 para Analizar datos del ClassRoom
import pycore.scripts as instancia1

#RUTAS DE ARCHIVOS E INDEXES
setArchivos1 = [
    {"path":"data/El Salvador.xls", "starRow":2, "starCol":2},
    {"path":"data/Costa Rica.xls", "starRow":2, "starCol":2},
    {"path":"data/Guatemala.xls", "starRow":2, "starCol":2},
    {"path":"data/Honduras.xls", "starRow":2, "starCol":2},
    {"path":"data/Panama.xls", "starRow":2, "starCol":2},
    {"path":"data/Nicaragua.xls", "starRow":2, "starCol":2}
]

#Se limpia instancia
instancia1.clearInstance()
for archivo in setArchivos1:
    instancia1.addExcelFile(archivo["path"], archivo["starRow"], archivo["starCol"])
    #SE ESTANDARIZA EL NOMBRE DEL CINE
    instancia1.estandarizarColLocal(0, r'([a-zA-Z ]*)')
    
    #SE AGREGA COLUNNA PAIS SEGUN NOMBRE DEL ARCHIVO
    instancia1.addColCountryFile(archivo["path"])

#Se unen todos los excel en un unico DF
finalDf = instancia1.joinAllDataFrames()

    
## Se Modican datos finalDf
#SE SOLUCIONAN DECIMALES
#finalDf['Thu 18-Aug $'] = finalDf['Thu 18-Aug $'].apply('{:.2f}'.format)
#finalDf['Fri 19-Aug $'] = finalDf['Fri 19-Aug $'].apply('{:.2f}'.format)
#finalDf['Sat 20-Aug $'] = finalDf['Sat 20-Aug $'].apply('{:.2f}'.format)
#finalDf['Sun 21-Aug $'] = finalDf['Sun 21-Aug $'].apply('{:.2f}'.format)
#finalDf['Weekend\nGross $'] = finalDf['Weekend\nGross $'].apply('{:.2f}'.format)
#finalDf['Mon 22-Aug $'] = finalDf['Mon 22-Aug $'].apply('{:.2f}'.format)
#finalDf['Tue 23-Aug $'] = finalDf['Tue 23-Aug $'].apply('{:.2f}'.format)
#finalDf['Wed 24-Aug $'] = finalDf['Wed 24-Aug $'].apply('{:.2f}'.format)
#finalDf['Week\nGross $'] = finalDf['Week\nGross $'].apply('{:.2f}'.format)

for key in finalDf.keys():
    if '$' in key
        finalDf[key] = finalDf[key].apply('{:.2f}'.format)


#ELIMINANDO COLUMNAS DINERO REPETIDAS 
finalDf=finalDf.drop(['mf_friday $', 'mf_thursday $','mf_saturday $'
,'mf_sunday $','mf_wkend_rev $','mf_monday $','mf_tuesday $','mf_wednesday $','mf_rev $'],axis=1)
#ELIMINANDO COLUMNAS PORCENTAJES
finalDf=finalDf.drop(['%','%.1','%.2','%.3','%.4','%.5','%.6','%.7','%.8','%.9','%.10','%.11'
,'%.12','%.13','%.14','%.15','%.16','%.17'],axis=1)
#ELIMINANDO COLUMNAS VISITANTES REPETIDAS
finalDf=finalDf.drop(['mf_thursday_xtns','mf_saturday_xtns','mf_sunday_xtns','mf_monday_xtns','mf_tuesday_xtns'
,'mf_wednesday_xtns','mf_friday_xtns','mf_thursday_xtns.1','mf_xtns'],axis=1)

#Se Guarda
finalDf.to_excel("data/finalDf.xlsx", index=False)
#finalDf





#########################################2##########################################################
## Instancia 2 para Analizar datos generados
import pycore.scripts as instancia2

#Se limpia instancia
setArchivos2 = [
    {"path":"data/28-08-22/Costa_Rica.xlsx", "starRow":0, "starCol":0},
    {"path":"data/28-08-22/El_Salvador.xlsx", "starRow":0, "starCol":0},
    {"path":"data/28-08-22/Guatemala.xlsx", "starRow":0, "starCol":0},
    {"path":"data/28-08-22/Honduras.xlsx", "starRow":0, "starCol":0},
    {"path":"data/28-08-22/Nicaragua.xlsx", "starRow":0, "starCol":0},
    {"path":"data/28-08-22/Panama.xlsx", "starRow":0, "starCol":0}
]

#Se limpia instancia
instancia2.clearInstance()
for archivo in setArchivos2:
    #Carga Archiv
    instancia2.addExcelFile(archivo["path"], archivo["starRow"], archivo["starCol"])
    #Agrega Col PAIS
    instancia2.addColCountryFile(archivo["path"])
    
#Se unen todos los excel en un unico DF
finalDf2 = instancia2.joinAllDataFrames()
#finalDf2.to_excel("data/finalDf2.xlsx", index=False)

#Se limpia Instancia y se agrega el DF con toda la data unida
instancia2.clearInstance()
instancia2.addDF(finalDf2)

#Se estandariza la columna 2, los titulos de las peliculas
instancia2.estandarizarColPeliculas(2, None)
finalDf2 = instancia2.getCurrentData()

#Se Guarda
finalDf2.to_excel("data/finalDf2.xlsx", index=False)
#finalDf2


#########################################3##########################################################
## Se Crea Match entre finalDf1 y finalDf2

import pandas as pd
from fuzzywuzzy import fuzz

df1 = finalDf
#df1 = pd.read_excel ("data/finalDf.xlsx")
df2 = finalDf2
#df2 = pd.read_excel ("data/finalDf2.xlsx")


#Columnas a usar
df1 = df1.iloc[:,[0,1,2,3,4]]
df1.columns = ['pais1', 'local1', 'titulo1', 'ciudad1', 'circuito1']

df2 = df2.iloc[:,[0,1,2,3,4]]
df2.columns = ['pais2', 'local2', 'titulo2', 'ciudad2', 'circuito2']


#Union de ambos DataFrames Todo con cada Fila(Matriz de Filas)
merged_df = pd.merge(df1, df2, how='cross')
merged_df = merged_df.drop_duplicates()


#Se obtienen relaciones de cada columna
merged_df['ratio_pais'] = merged_df.apply(
    lambda row: fuzz.ratio(row['pais1'], row['pais2']),
    axis=1
)

merged_df['ratio_local'] = merged_df.apply(
    lambda row: fuzz.ratio(row['local1'], row['local2']),
    axis=1
)

merged_df['ratio_titulo'] = merged_df.apply(
    lambda row: fuzz.ratio(row['titulo1'], row['titulo2']),
    axis=1
)

merged_df['ratio_ciudad'] = merged_df.apply(
    lambda row: fuzz.ratio(row['ciudad1'], row['ciudad2']),
    axis=1
)

merged_df['ratio_circuito'] = merged_df.apply(
    lambda row: fuzz.ratio(row['circuito1'], row['circuito2']),
    axis=1
)



#Filtro para mostrar solo coincidencias mayores en los siguentes datos:
#ratio_pais     = 100%
#ratio_local    = 65%
#ratio_titulo   = 63%
#ratio_ciudad   = 75%
#ratio_circuito = 70%
matchedDf = merged_df[(merged_df["ratio_pais"]>=100) & (merged_df["ratio_local"]>=65) & (merged_df["ratio_titulo"]>=63) & (merged_df["ratio_ciudad"]>=75) & (merged_df["ratio_circuito"]>=70)]
#matchedDf

#Se Guarda
matchedDf.to_excel("data/finalDfMatch.xlsx", index=False)
print(matchedDf)

