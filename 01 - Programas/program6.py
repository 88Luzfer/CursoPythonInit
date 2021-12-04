with open("archivos/frases.txt","w") as inicio_archivo:
    inicio_archivo.write("")


while True:
    entrada = input("Say something: ")

    if entrada == "\end":
        with open("archivos/frases.txt") as leer_archivo:
            lectura = leer_archivo.read()

        print(lectura)
        break
    else:
        if entrada.startswith(("how", "what", "why")):
            entrada = entrada.capitalize()
            with open("archivos/frases.txt", "a") as añadir_frase:
                añadir_frase.write(entrada + "?. ")
        else:
            entrada = entrada.capitalize()
            with open("archivos/frases.txt", "a") as añadir_frase:
                añadir_frase.write(entrada + ". ")

