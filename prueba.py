from pandas import read_excel
import sqlalchemy as alchemy

demoras = read_excel('demoras.xlsx')
produccion = read_excel('produccion.xlsx')
#print(demoras.head())
#print(produccion.head())
print(type(demoras))
