#ejercicio 1: conversor de tiempo a segundo

#pedimos los datos del usuario 

hora = int(input("ingresa las horas:"))
minutos = int(input("ingresa los minutos:"))
segundos = int(input("ingresa los segundos:"))

#calculo: 1hora = 3600seg | 1min = 60seg

total_segundos = horas * 3600 + minutos* 60 + segundos 

#mostramos el resultado 

print("el total en segundos es:",total_segundos)

