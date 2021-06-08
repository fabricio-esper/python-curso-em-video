IDADE = CONTI = CONTS = CONTM = 0 

while True:
    IDADE = int(input('Idade: '))
    if IDADE >= 18:
        CONTI += 1
    SEXO = ' '
    while SEXO not in 'MF':
        SEXO = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if SEXO == 'M':
        CONTS += 1
    if SEXO == 'F' and IDADE < 20:
        CONTM += 1
    FIM = ' '
    while FIM not in 'SN':
        FIM = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if FIM == 'N':
        break
print(f'{CONTI} pessoas tem mais de 18 anos.')
print(f'{CONTS} homens foram cadastrados.')
print(f'{CONTM} mulheres tem menos de 20 anos.')
