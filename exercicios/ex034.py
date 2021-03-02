s = float(input("Qual é o seu salário? R$"))
if s <= 1250:
    print(f"Seu novo salário é de \033[32mR${s+(0.15*s):.2f}\033[m")
else:
    print(f"Seu novo salário é de  \033[32mR${s+(0.10*s):.2f}\033[m")
