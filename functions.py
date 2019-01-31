def saludar(name = "Nombre por defecto"):
    print(f"Hola {name}")

saludar("Alex Colombo")
saludar("Lucas")
saludar()

def sumar(n1,n2):
    print(n1+n2)
    return n1 + n2


result = sumar(10,50)
print("result", result)

print(len("super"))

suma = lambda numero1, numero2: numero1+numero2

print("suma", suma(90,50))
