cantidad = int(input("¿Cuántos números deseas ingresar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Número " + str(i + 1) + ": "))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

segundo = numeros[0]

for numero in numeros:
    if numero > segundo and numero < mayor:
        segundo = numero

print("Lista original:", numeros)
print("Segundo número más grande:", segundo)