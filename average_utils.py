def calcular_promedio():
	while True:
		try:
			numeros = [float(input(f"Ingrese número {i+1}: ")) for i in range(5)]
			print(f"El promedio de las 5 notas es: {round(sum(numeros) / len(numeros),2)}")
			break
		except ValueError:
			print("El valor ingresado debe ser un número real, reingrese todas las notas")