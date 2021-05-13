print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)

TERMO = int(input('Digite o Primeiro Termo de uma PA: '))
RAZAO = int(input('Digite a Razão dessa PA: '))
POSI = 0

while POSI != 10:
    POSI += 1
    print(f'{TERMO}', end='')
    print(' > ' if POSI != 10 else ' ', end='')
    TERMO += RAZAO
print("ACABOU!")
