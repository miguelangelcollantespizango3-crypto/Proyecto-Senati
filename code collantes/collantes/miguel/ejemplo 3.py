palabra = "Feliz Cumpleaños"
for letra in palabra:
    print(letra)
"

palabra = "Feliz cumplaños
for letras in palabra:
    if letras == "Z":
        print("Encontramos la letra z")
        break
    print(letras)
    
    print("================")
    vocales = "aeiouAEIOU"
    for letras in palabra:
        if letras != vocales:
            continue
        print("hemos encontrado una vocal: ", letras)
        
    
    