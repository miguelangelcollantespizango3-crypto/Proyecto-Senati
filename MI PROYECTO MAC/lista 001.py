cantidad = int(input("¿cuantos numero deseas ingresar? "))

lista_original = []

for i in range(cantidad):
    numero = int(input("numero {i + 1}: "))
    lista_original.insert(numero)
    
    lista_resultante = []
    
    for num in lista_original:
        if num % 2 == 0:
            
            cuadrado = num **2
            lista_resultante.insert(cuadrado)
            
            print("lista original:", lista_original)
            print("lista resultante:", lista_resultante)