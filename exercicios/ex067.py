while True:
    VAL = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if VAL < 0:
        break
    for CONT in range(1, 11):
        print(f'{VAL} x {CONT} = {VAL*CONT}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
