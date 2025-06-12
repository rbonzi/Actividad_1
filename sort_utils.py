def ordenar_numeros():
	numeros = []
	while len(numeros) != 5:
		try:
			numero = int(input(f"Ingrese el número a agregar (numero: {len(numeros)+1}): "))
			numeros.append(numero)
		except ValueError:
			print("El dato ingresado debe ser un número entero, reingrese")
	numeros = sorted(numeros)
	print("Sus números ordenados de menor a mayor son: ",end="")
	for numero in numeros:
		print(numero, end=" ")