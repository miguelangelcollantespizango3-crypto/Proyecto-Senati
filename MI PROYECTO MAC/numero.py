numero = int(input("Ingresa un numero entero positivo :"))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("El numero invertido es:", invertido)