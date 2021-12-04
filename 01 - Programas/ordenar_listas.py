def foo(*args):
    new_list = [elemento.upper() for elemento in args]
    new_list.sort()
    return new_list

print(foo("hola", "perro", "casa", "amigo"))