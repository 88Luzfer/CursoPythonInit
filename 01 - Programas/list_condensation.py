def foo(lista):
    new_list = [elemento for elemento in lista if type(elemento) == int]
    return new_list

def foo2(lista):
    new_list = [elemento if type(elemento) == int else 0 for elemento in lista]
    return new_list

def foo3(lista):
    new_list = [float(elemento) for elemento in lista]
    suma = sum(new_list)
    return new_list, suma


print(foo([1,2,3,4,5,6,"ahora"]))

print(foo2([ 1,"no data", 3,"no data", 5]))

print(foo3(["3.4","5.5","7.7"]))

a = foo3(["3.4","5.5","7.7"])

print(a)
print(type(list(a)))

