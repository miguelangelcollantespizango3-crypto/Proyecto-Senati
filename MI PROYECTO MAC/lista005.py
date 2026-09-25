cantidad = int(input("¿Cuántos números deseas ingresar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Número " + str(i + 1) + ": "))
    numeros.append(numero)

resultado = []

for numero in numeros:
    if numero != 0:
        resultado.append(numero)

for numero in numeros:
    if numero == 0:
        resultado.append(numero)

print("Lista original:", numeros)
print("Lista resultante:", resultado)
