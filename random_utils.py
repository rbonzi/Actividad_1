import random
def generar_numero_aleatorio():
	while True:
		try:
			rango_inicial = int(input("Ingrese el inicio del rango: "))
			rango_final = int(input("Ingrese el final del rango: "))
			if rango_final > rango_inicial:
				break
			else:
				print("El rango final no puede ser menor que el rango inicial, reingrese")
		except ValueError:
			print("El valor ingresado debe ser un número entero, reingrese")
	print(f"El número al azar entre {rango_inicial} y {rango_final} es: {random.randint(rango_inicial, rango_final)}")
