with open ("archivos/fruits.txt", "a+") as myfile:
    myfile.write("\nOnion")
    myfile.seek(0)
    content=myfile.read()

print(content)
