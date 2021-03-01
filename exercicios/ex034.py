s = float(input("Qual é o seu salário? R$"))
if s <= 1250:
    print(f"Seu novo salário é de R${s+(0.15*s):.2f}")
else:
    print(f"Seu novo salário é de R${s+(0.10*s):.2f}")
