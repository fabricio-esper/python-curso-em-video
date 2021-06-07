CONT = 'S'
NUM = SOMA = QNT = MEDIA = MAIOR = MENOR = 0

while CONT in 'Ss':
    NUM = int(input('Digite um número: '))
    SOMA += NUM
    QNT += 1
    if QNT == 1:
        MAIOR = MENOR = NUM
    if NUM < MENOR:
        MENOR = NUM
    CONT = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
MEDIA = SOMA / QNT
print(f'Você digitou {QNT} números e a média foi {MEDIA}')
print(f'O maior valor foi {MAIOR} e o menor foi {MENOR}')
