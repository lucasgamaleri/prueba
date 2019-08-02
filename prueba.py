import pandas as pd
from pandas import read_excel
import xlrd

#Definiciones y funciones
def print_full(x):
        pd.set_option('display.max_rows', len(x))
        print(x)
        pd.reset_option('display.max_rows')

#IMPORTACION DE BASE DE DATOS
date = "31-07-2019"
demoras = read_excel(date +' - Demoras.xls')
demoras.set_index('Bobina')
produccion = read_excel(date +'.xlsx')
produccion.set_index('Bobina')




# Lista de refilados
produccion = produccion.assign(REFILADO=lambda x: produccion['Material Refilado']==0)


# Lista de cambios de ancho
cambiodeancho = [False]
for i in range(0,len(produccion)-1):
    if produccion.at[i+1,'Ancho'] == produccion.at[i,'Ancho']:
        cambiodeancho.append(False)
    else:
        cambiodeancho.append(True)

# Lista de Lotes
lotes = []
index = []
count = 1

for i in range(1, len(produccion)):        
        if produccion.at[i-1,'Ancho'] == produccion.at[i,'Ancho']:
                count = count+1                
        else:
                if list(produccion.index)[i] in list(demoras.index):
                        lotes.append(count)        
                        count = 1
                else:
                        count = count+1
                
print(lotes)