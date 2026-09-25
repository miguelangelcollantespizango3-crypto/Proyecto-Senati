numero = input("Ingresa un numero: ")
suma = 0

for digito in numero:
    suma = suma + int(digito)
    print("La suma de los digitos es:", suma)