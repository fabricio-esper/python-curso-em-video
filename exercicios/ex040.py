print("Digite suas notas para calcular a média")
n = float(input("Primeira nota: "))
n1 = float(input("Segunda nota: "))

m = (n + n1) / 2
print(f"Média: {m:.1f}")
if m < 5:
    print("\033[31mREPROVADO\033[m")
elif 5 <= m <= 6.9:
    print("DE RECUPERAÇÃO")
else:
    print("\033[32mAPROVADO\033[m")