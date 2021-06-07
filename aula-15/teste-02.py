NUM = SOMA = 0

while True:
    NUM = int(input('Digite um número: '))
    if NUM == 999:
        break
    SOMA += NUM
print(f'A soma vale {SOMA}')
