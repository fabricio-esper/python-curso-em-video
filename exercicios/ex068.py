from random import randint

VAL = COMPUT = RES = CONT = 0

print('=-'*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*12)

while True:
    VAL = int(input('Digite um Valor: '))
    COMPUT = randint(0, 10)
    RES = VAL + COMPUT
    ESC = ' '
    while ESC not in 'PI':
        ESC = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você Jogou {VAL} e o computador {COMPUT}. Total de {RES} ', end='')
    print('DEU PAR' if RES % 2 == 0 else 'DEU ÍMPAR')
    if ESC == 'P':
        if RES % 2 ==0:
            print('Você VENCEU!')
            CONT += 1
        else:
            print('Você PERDEU!')
            break
    elif ESC == 'I':
        if RES % 2 == 1:
            print('Você VENCEU!')
            CONT += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {CONT} vezes')
