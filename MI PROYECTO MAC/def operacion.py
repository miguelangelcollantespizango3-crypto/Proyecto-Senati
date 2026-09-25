# ========== FUNCIONES PARA CADA OPERACIÓN ==========
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

# ========== MENÚ PRINCIPAL ==========
while True:
    # Mostramos el menú
    print("\n===== MENÚ DE OPERACIONES =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("================================")

    # Pedimos la opción al usuario
    opcion = input("Elige una opción (1-5): ")

    # Salir si elige 5
    if opcion == "5":
        print(" ¡Hasta luego!")
        break

    # Verificamos que sea una opción válida
    if opcion not in ["1", "2", "3", "4"]:
        print(" Opción inválida. Intenta de nuevo.")
        continue

    # Pedimos los dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizamos la operación según la opción
    if opcion == "1":
        resultado = sumar(num1, num2)
        print(f" Resultado: {num1} + {num2} = {resultado}")
    elif opcion == "2":
        resultado = restar(num1, num2)
        print(f" Resultado: {num1} - {num2} = {resultado}")
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        print(f" Resultado: {num1} × {num2} = {resultado}")
    elif opcion == "4":
        resultado = dividir(num1, num2)
        print(f" Resultado: {num1} ÷ {num2} = {resultado}")