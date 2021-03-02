from datetime import date
A = int(input("Digite um ano qualquer (0 para o ano atual): "))
if A == 0:
    A = date.today().year
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print(f"O Ano {A} \033[32mé\033[m BISSEXTO")
else:
    print(f"O Ano {A} \033[31mnão é\033[m BISSEXTO")
