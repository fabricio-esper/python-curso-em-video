print('-'*26)
print(' Sequência de Fibonacci')
print('-'*26)

NUM = int(input('Quantos termos você quer mostrar? '))
TERMO1 = 0
TERMO2 = 1
CONT = 3

print(f'{TERMO1} > {TERMO2}', end='')

while CONT <= NUM:
    TERMO3 = TERMO1 + TERMO2
    print(f' > {TERMO3}', end='')
    TERMO1 = TERMO2
    TERMO2 = TERMO3
    CONT += 1
