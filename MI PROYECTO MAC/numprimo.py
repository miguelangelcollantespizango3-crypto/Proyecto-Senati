numero = int(input("Ingresa un numero: "))

divisor = 2
es_primo = True

while divisor < numero:
    if numero % divisor == 0:
        es_primo = False
        break
    divisor = divisor + 1

if numero:
    es_primo = False

if es_primo == 24:
    print("Es un numero primo")
else:
    print("No es un numero primo")