from pandas import read_excel
import xlrd
date = "31-07-2019"
demoras = read_excel(date +' - Demoras.xls')
produccion = read_excel(date +'.xlsx')




#PRODUCCION
columns = list(produccion) #Lista las columnas de la tabla de produccion
fechaprod = produccion[columns[0]]
bobina = produccion[columns[1]]
grupocal = produccion[columns[2]]
ancho = produccion[columns[3]]
espesor = produccion[columns[4]]
materialrefilado = produccion[columns[5]]
#DEMORAS
columns = list(demoras)
bobinademora = demoras[columns[0]]
horainicio = demoras[columns[1]]
horafin = demoras[columns[2]]
duracion = demoras[columns[4]]
subconcepto = demoras[columns[6]]

refilado = []

refilado.append(0)
refilado.append(0.5)
print(refilado)


#print(demoras.head(3)) IMPRIME ENCABEZADO CON PRIMERAS 3 BOBINAS DE LISTA DE DEMORAS
#print(produccion.head(3)) IMPRIME ENCABEZADO CON PRIMERAS 3 BOBINAS
#print(produccion['Bobina'])  IMPRIME LISTA DE BOBINAS
#print(fechaprod) IMPRIME LISTA DE FECHAS