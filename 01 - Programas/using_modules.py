import time
import os
#import pandas


while True:
    if os.path.exists("archivos/vegetables.txt"):
        with open("archivos/vegetables.txt") as file:
            print(file.read())
    else:
        print("El archivo no existe")
    time.sleep(10)
