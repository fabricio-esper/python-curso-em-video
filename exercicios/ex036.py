c = float(input("Qual é o valor da Casa? BRL "))
s = float(input("Qual é o seu salário? BRL "))
y = float(input("E em quantos anos você irá pagar? "))

p = c / (y*12)

print(f"O Valor da prestação será de BRL {p:.2f}")
if p >= 0.3*s:
    print("Desculpe, mas excede 30% do seu salário, então será negado.")
else:
    print("Ok! Será possível realizar o empréstimo.")
