#Esto lo guardo como código útil para posteriores desarrollos
#La función "isinstance(var, tipo)" es muy util para validar entradas

def temperatura(t):
    if isinstance(t,str):
        print("por favor introduce un valor entero no una cadena")
        return False
    elif isinstance(t,float):
        print("solo se admiten valores enteros en esta función")
        return False
    else:
        return True

#Soy cosciente que la función temperatura no esta preparada para controlar tuplas, listas o diccionarios.

#temp=input("por favor introduce la temperatura actual")

if temperatura(25):
    print("buen trabajo")
else:
    print("prueba otra vez")