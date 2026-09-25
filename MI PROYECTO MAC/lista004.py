cantidad = int(input("¿Cuántos elementos deseas ingresar? "))

elementos = []

for i in range(cantidad):
    elemento = input("Elemento " + str(i + 1) + ": ")
    elementos.append(elemento)

print("Lista original:", elementos)

vistos = []

print("Frecuencia:")

for elemento in elementos:
    
    if elemento not in vistos:
        contador = 0
        
        for otro in elementos:
            if elemento == otro:
                contador = contador + 1
                
                
        print(elemento + ":", contador)
        vistos.append(elemento)