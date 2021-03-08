print("-="*11)
print("     Cálculo de IMC")
print("-="*11)

m = float(input("Qual é o seu peso em kg? "))
h = float(input("Qual é sua altura em m? "))

imc = m / (h**2)
print(f"Seu IMC é igual a {imc:.2f}")

if imc < 18.5:
    print("Abaixo de 18.5: Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Entre 18.5 e 25: Peso Ideal")
elif imc >= 25 and imc < 30:
    print("Entre 25 e 30: Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Entre 30 e 40: Obesidade")
else:
    print("Acima de 40: Obesidade mórbida")