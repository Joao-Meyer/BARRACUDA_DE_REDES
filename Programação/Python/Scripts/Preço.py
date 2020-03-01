a = float(input('Digite o valor da compra:'))
if a < 200:
    print('Digite 1 para pagamento a vista')
    print('Digite 2 para pagamento a prazo')
    print('Digite 3 para pagamento com GLUB-GLUB')
    while True:
        b = input('Forma de Pagamento:')
        if b == '1':
            print('O valor a ser pago é de R${:.2f}'.format(a))
            break
        elif b == '2':
            print('O valor a ser pago é de R${:.2f}'.format(a / 0.90))
            break
        elif b == '3':
            print('O valor a ser pago é de R${} \nVOLTE SEMPRE!!!!!'.format(a - a))
            break
        else:
            print('Forma de pagamento inválida')
            print('Tente novamente')
elif a > 200:
    print('Digite 1 para pagamento a vista')
    print('Digite 2 para pagamento a prazo')
    while True:
        b = input('Forma de Pagamento:')
        if b == '1':
            print('O valor a ser pago é de R${:.2f}'.format(a))
            break
        elif b == '2':
            print('O valor a ser pago é de R${:.2f}'.format(a / 0.90))
            break
        else:
            print('Forma de pagamento inválida')
            print('Tente novamente')

