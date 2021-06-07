NUM = SOMA = CONT = 0

while True:
    NUM = int(input('Digite um número inteiro [999 para parar]: '))
    if NUM == 999:
        break
    SOMA += NUM
    CONT += 1
print(f'Foram digitados {CONT} números e a soma entre eles foi de {SOMA}.')
