D = float(input("Qual é a distância da viagem em Km? "))
print(f"O preço da viagem é de R${D * 0.5 if D <= 200 else D * 0.45:.2f}")