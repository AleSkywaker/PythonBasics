myStr = "alex colombo"

# para ver todos los metodos y propiedades de los string usar dir
# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("alex", 'Alex'))
print(myStr.count(' '))
print(myStr.startswith("alex"))
print(myStr.endswith("alex"))
print(myStr.split(" "))
print(myStr.find("x"))
print(len(myStr))
print(myStr.index("x"))
print(myStr[3])
print(myStr.isnumeric())
print(myStr.isalpha())

#Concatenacion strings
nombre = "Alex"

print("Mi nombre es " + nombre)
print(f"Mi nombre es {nombre}")
print("Mi nombre es {0}".format(nombre)) # para versiones anteriores a la 3