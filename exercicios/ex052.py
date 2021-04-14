p = int(input('Digite um número inteiro: '))
for n in range(0,100):
    if p % p == 0 and p % n != 0 and p % 1 == 0:
        print(f'O número {p} é primo')
    else:
        print(f'O número {p} não é primo')
