print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)

TERMO = int(input('Digite o Primeiro Termo de uma PA: '))
RAZAO = int(input('Digite a Razão dessa PA: '))
POSI = 0
TOTAL = 0
CONTINUAR = 10

while CONTINUAR != 0:
    TOTAL += CONTINUAR
    while POSI != TOTAL:
        POSI += 1
        print(f'{TERMO}', end='')
        print(' > ' if POSI != TOTAL else ' ', end='')
        TERMO += RAZAO
    print('')
    CONTINUAR = int(input('Quer ver mais quantos termos? '))
print(f'Progressão finalizada com {TOTAL} termos mostrados.')
