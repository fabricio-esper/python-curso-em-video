NUM = QNT = SOMA = 0

NUM = int(input('Digite um número [999 para parar]: '))

while NUM != 999:
    SOMA += NUM
    QNT += 1
    NUM = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {QNT} números e a soma entre eles foi {SOMA}')
