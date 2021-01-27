from math import sqrt
co = int(input("Digite o valor do cateto oposto: "))
ca = int(input("Digite o valor do cateto adjacente: "))
h = sqrt((ca**2) + (co**2))
print(f"O valor da hipotenusa desse triângulo retângulo é de {h:.2f}")
