cantidad = int(input("¿Cuántos números deseas ingresar? "))

numeros = []

for i in range(cantidad):
    numero = int(input("Número " + str(i + 1) + ": "))
    numeros.append(numero)

posiciones = int(input("¿Cuántas posiciones deseas desplazar? "))

rotada = []

for i in range(cantidad):
    nueva_posicion = (i + posiciones) % cantidad
    rotada.append(numeros[i])

print("Lista original:", numeros)
print("Lista rotada:", rotada)
