#Calculo de IMC Basico
p = double(input("informe seu peso"))
h = double(input("informe sua altura"))

calculo (peso,altura):
	imc = (peso/(altura * altura))
	if imc < 18.5
		print(f"IMC de {imc},Abaixo do peso")
	elif imc > 18.5 OR <= 24.9
		print(f"IMC de {imc}, Peso Ideal")
	elif imc >= 25 OR <= 29.9
		print(f"IMC de {imc}, Sobrepeso")
	else
		print(f"IMC de {imc}, Obeso")
calculo(p,h)
