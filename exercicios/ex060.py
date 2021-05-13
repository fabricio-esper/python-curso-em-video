# from math import factorial

# NUM = int(input('Digite um número para calcular seu Fatorial: '))
# FAT = factorial(NUM)

# print(f'O fatorial de {NUM} é {FAT}')

NUM = int(input('Digite um número para calcular seu Fatorial: '))
CONT = NUM
FAT = 1

print(f'Calculando {NUM}! = ', end='')

while CONT > 0:
    print(f'{CONT}', end='')
    print(' x ' if CONT > 1 else ' = ', end='')
    FAT *= CONT
    CONT -= 1
print(f'{FAT}')