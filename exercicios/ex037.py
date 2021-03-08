n = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
o = int(input("Sua opção: "))
if o == 1:
    print(f"{n} convertido para binário é igual a {bin(n)[2:]}")
elif o == 2:
    print(f"{n} convertido para octal é igual a {oct(n)[2:]}")
elif o == 3:
    print(f"{n} convertido para hexadecimal é igual a {hex(n)[2:]}")
else:
    print("Opção inválida. Tente novamente.")