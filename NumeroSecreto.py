'''Proyecto dia 4'''
from random import *

nombre = input("Ingrese su nombre: ")

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")



numeroSecreto = randint(1,100)
print(f"numero secreto {numeroSecreto}")

intentos = 0

while intentos <= 8:
    if intentos == 8:
        print("Se ha agotado el numero de intentos, no encontraste el numero secreto")
        break
    numero = int(input("Ingrese el numero secreto: "))

    if numero < 1 or numero > 100:
        print("El numero no esta permitido, por favor ingrese un numero del 1 al 100")
    elif numero < numeroSecreto:
        print("El numero elegido es menor al numero secreto, vuelva a intentarlo")
        intentos += 1
    elif numero > numeroSecreto:
        print("El numero elegido es mayor al numero secreto, vuelva a intentarlo")
        intentos += 1
    else:
        print(f"BIEN HAZ ADIVINADO!!! Numero de intentos: {intentos}")
        break

