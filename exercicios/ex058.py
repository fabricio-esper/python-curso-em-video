from random import randint

comput = randint(0, 10)

print('Tente descobrir o numero entre 0 a 10 que estou "pensando"')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('Mais.. tente mais uma vez')
        elif jogador > comput:
            print('Menos.. tente mais uma vez')
print(f'Acertou com {palpites} tentativas')
