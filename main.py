import os
import time

def mensaje(palabra):
    for letra in palabra:
        print(letra,end="",flush=True)
        time.sleep(0.02)

mensaje("Bienvenido a nuestro menú")

while True:
    mensaje("""
1. Generar un número aleatorio
2. Ordenar 5 números
3. Calcular promedio de 5 números
4. Salir
Opción: """)
    opcion = input()
    match opcion:
        case "1":
            generar_numero_aleatorio()
        case "2":
            ordenar_numeros()
        case "3":
            calcular_promedio()
        case "4":
            for i in range(1,4):
                os.system("cls")
                mensaje("Saliendo del programa"+"."*i)
                time.sleep(0.4)
            break
        case _:
            mensaje("Opción ingresada no válida, reingrese")