nombre = input ("Introduzca su nombre: \n")
apellido = input ("Introduzca su nombre: \n")
mensaje = "Hola %s %s" % (nombre, apellido) #Esta forma es para python 3.6 o inferior
mensaje2 = f"Hola {nombre} {apellido}"  #Esta forma es para python 3.6 o superior.

mensaje.title()
print(mensaje)
print(mensaje2)