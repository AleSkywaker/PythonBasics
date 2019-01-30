alimentos = ["banana", "fresas", "yogurt", "arroz"]

for alimento in alimentos:
    if alimento == "banana":
        print("tienes que comprar " + alimento)
    print(alimento)

for numero in range(1,9):
    if numero == 5:
        break
    print(numero)

for letra in "Hello":
    if letra == "l":
        continue
    print(letra)

# bucle while

contador = 8

while contador <= 10:
    print(contador)
    contador = contador + 1