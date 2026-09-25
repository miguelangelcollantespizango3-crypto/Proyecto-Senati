def mayor_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor

# Pedir números
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

# Mostrar resultado
print("El mayor es:", mayor_de_tres(n1, n2, n3))
print("PROGRAMA TERMINADO")