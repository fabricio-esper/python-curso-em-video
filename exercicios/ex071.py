print('='*15)
print('BANCO GENÉRICO')
print('='*15)

VAL = int(input('Que valor você quer sacar? R$'))
TOTAL = VAL
CED = 50
TOTCED = 0

while True:
    if TOTAL >= CED:
        TOTAL -= CED
        TOTCED += 1
    else:
        if TOTCED > 0:
            print(f'Total de {TOTCED} cédulas de R${CED}')
        if CED == 50:
            CED = 20
        elif CED == 20:
            CED = 10
        elif CED == 10:
            CED = 1
        TOTCED = 0
        if TOTAL == 0:
            break
