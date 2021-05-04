from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é sua opção? '))
    if op == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')