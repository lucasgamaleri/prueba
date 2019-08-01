#Este codigo quita todos los numeros de la bobina detrás de la U
#por ejemplo si se tiene 075600U2, la salida es 075600U

material = '075600U'
print(material)
print(len(material))
material = material[:material.find('U')+1]

print(material)
print(len(material))
