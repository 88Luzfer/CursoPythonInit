def multiples_argumentos(*args):
    new_list = [type(elemento) for elemento in args]
    #return sum(args) / len(args)
    return new_list


print(multiples_argumentos(1,"lista",3,5,6,7,12,23))

