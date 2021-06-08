TOT = QNT = MENOR = CONT = 0
PROB = ''

while True:
    PRO = str(input('Nome do produto: '))
    PRE = float(input('Preço: R$'))
    CONT += 1
    TOT += PRE
    if PRE > 1000:
        QNT += 1
    if CONT == 1 or PRE < MENOR:
        MENOR = PRE
        PROB = PRO
    FIM = ' '
    while FIM not in 'SN':
        FIM = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if FIM == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi de R${TOT:.2f}')
print(f'Temos {QNT} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {PROB} que custa R${MENOR:.2f}')
