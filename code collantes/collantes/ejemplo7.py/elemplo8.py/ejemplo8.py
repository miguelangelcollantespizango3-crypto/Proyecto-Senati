print("====Bienvenido al sistema ==== ")
user = input("Ingrese su usuario: ")
Clave = input("Ingrese su clave: ")

while True:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if user != "pepito" or clave != "123":
        print("Usuario o clave Incorrecta")
        print("Vuelve a ingresar los datos")
        continue
    
    if user ==  "" or clave =="":
        print("¡por favor nodejes los campos vacios!")
        continue
    if user == "pepito" and clave == "123" :
        print("¡Bienvenido usuario pepito!")
        break
