while True:
	a = int(input('Digite o HC:'))
	b = float(input('Digite o fator de defracao(0,2 ou 0,5):'))
	c = float(input('Digite a Comprimento total dos cordoes:'))
	C = (102 - a) / (1 + b )
	W = C - c
	print('O projeto usara {} patch cords!'.format(W))