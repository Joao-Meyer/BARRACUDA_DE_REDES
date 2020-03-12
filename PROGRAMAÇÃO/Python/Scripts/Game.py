print('Adventure Python!')
a = (' O\n-|-\n/ \\')
print('Use comandos específicos e com apenas uma palavra.')
print('Por exemplo: andar ,pegar ,atacar')
input('Aperte enter para começar a aventura!')
print('Você acorda em uma sala escura!')
print('Com apenas uma fonte de luz ao fundo dela.')
while True:
    b = input('Você vai andar até a luz ou ficar parado onde está?')
    if (b == 'andar'):
        print('Você anda até a luz!')
        print('E chega a uma ponte bem iluminada pela luz do sol, e ao olhar para baixo não conseguer ver o final do abismo...')
        while True:
            c = input('Você atravessa a ponte, pula no abismo ou fica parado?')
            if (c == 'atravessar'):
                print('Você atravessa a ponte!')
            elif (c == 'pular'):
                print('Você pulou da ponte!')
                print('GAME OVER')
            elif (c == 'ficar'):
                print('Você fica onde está!')
            else:
                print('Use comandos específicos e com apenas uma palavra!')
                erro2 = 'erro'
                erro2.__contains__(erro)
    elif (b == 'ficar'):
        print('Você fica onde está!')
        print('...\nDepois de algum tempo você começa a se perguntar se')
    else:
        print('Use comandos específicos e com apenas uma palavra!')
        erro = 'erro'
        erro.__contains__(erro)