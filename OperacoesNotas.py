n1 = int(input("Nota 1:"))
n2 = int(input("Nota 2:"))
n3 = int(input("Nota 3:"))
n4 = int(input("Nota 4:"))

operacoes(v1,v2,v3,v4):
	media  = ((v1 + v2 + v3 + v4)/4)
	soma = (v1 + v2 + v3 + v4)
	print(f"A Media dos valores é de {media}")
	print(f"A Soma dos valores é de {soma}")

operacoes(n1,n2,n3,n4)
