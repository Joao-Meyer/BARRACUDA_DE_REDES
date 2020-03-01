print('Adventure Python!')
a = ' O\n-|-\n/ \\'
print('Use comandos específicos e com apenas uma palavra.')
print('Por exemplo: andar ,pegar ,atacar')
input('Aperte enter para começar a aventura!')
print('Você acorda em uma sala escura!')
print('Com apenas uma fonte de luz ao fundo dela.')
while True:
    b = input('Você vai andar até a luz ou ficar parado onde está?')
    if b == 'andar':
        print('Você anda até a luz!')
        print('E chega a uma ponte bem iluminada pela luz do sol, e ao olhar para baixo não consegue ver o final do abismo...')
        while True:
            c = input('Você atravessa a ponte, pula no abismo ou fica parado?')
            if (c == 'atravessar'):
                print('Você atravessa a ponte!')
                print('E chega a uma floresta com uma trilha, pouco aparente, mas ainda sendo possível seguir por meio dela')
            elif (c == 'pular'):
                print('Você pula da ponte e sente seu corpo se chocar contra o chão, com a maioria dos seus ossos quebrados e orgãos internos danificados, sua morte é lenta e dolorosa!')
                print('GAME OVER')
                break
            elif (c == 'ficar'):
                print('Você fica onde está!')
                print('...\nDepois de algum tempo você começa a questionar a sua decisão de ficar parado')
            else:
                print('Verifique se digitou o comando corretamente!')
                print('E use comandos específicos e com apenas uma palavra!')
    elif (b == 'ficar'):
        print('Você fica onde está!')
        print('...\nDepois de algum tempo você começa a questionar a sua decisão de ficar parado')
    else:
        print('Verifique se digitou o comando corretamente!')
        print('E use comandos específicos e com apenas uma palavra!')