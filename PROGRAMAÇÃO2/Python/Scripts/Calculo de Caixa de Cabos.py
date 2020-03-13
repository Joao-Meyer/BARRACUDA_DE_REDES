while True:
	a = int(input('Digite o Maior Segmento(m):'))
	b = int(input('Digite o Menor Segmento(m):'))
	c = int(input('Digite a Quantidade de Tomadas:'))
	media = (a+b)/2
	reserva = (media/100*10) + media
	pedireito = (reserva/100*7) + reserva
	tomada = pedireito*c
	caixa = tomada/305
	print('O projeto usara {} caixas de cabos!'.format(caixa))