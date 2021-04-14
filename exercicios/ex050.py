s = 0
cont = 0
for c in range(1, 7):
    i = int(input(f'Digite o {c} número inteiro: '))
    if i % 2 == 0:
        s += i
        cont += 1
print(f'Você informou {cont} números pares, e a soma dos números pares é {s}')
