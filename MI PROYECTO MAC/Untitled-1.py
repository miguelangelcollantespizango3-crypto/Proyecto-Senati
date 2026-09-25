edad = int(input("Ingrese su edad"))
if edad <= 5:
    print("No puede ingresar")
elif edad >=5 and edad <=12:
    print("Usted pagas 15 soles")
elif edad >=13 and edad <=64:
    print("Usted pagas 25 soles")
elif edad >= 65:
    print("Usted pagas 18 soles")
else:
    print("Edad no reconoce")
    
    