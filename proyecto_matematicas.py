import time
import os
import platform

def borrar():
    so=platform.system()
    windows="Windows"
    linux="Linux"
    if so == windows:
        os.system("cls")
    else:
        os.system("clear")

#presentacion
print("¡Bienvenido a mi programa de Matematicas!")
 #elejir opciones
time.sleep(3)
print("Por favor sigue las instruciones y comencemos...")
def pedirNumeros():
    a=int(input("Ingresa el valor de a:"))
    b=int(input("Ingresa el valor de b:"))
    borrar()
    return a,b
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def menu(a,b):
    while True:
        print(f"Que tipo de operacion de matematicas deseas realizar con {a} y {b}\n\
s para sumar\n\
r para restar\n\
m para multiplicar\n\
d para dividir\n\
x para salir:")

        opcion=input()
        if opcion=='s':
            print(f"Resultado es:{suma(a,b)}")
        
        elif opcion=='r':
            print(f"Resultado es:{resta(a,b)}")
        
        elif opcion=='m':
            print(f"Resultado es:{multiplicacion(a,b)}")
       
        elif opcion=='d':
            print(f"Resultado es:{division(a,b)}")
        
        elif opcion=='x':
                break
        input("Presione cualquier tecla")
        borrar()
a,b=pedirNumeros()
menu(a,b)
    
