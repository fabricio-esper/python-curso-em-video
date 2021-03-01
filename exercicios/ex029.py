V = float(input("Qual é a velocidade atual do carro? "))
if V > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print(f"Você deve pagar uma multa de R${(V-80)*7:.2f}!")
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("Tudo certo! Dirija com segurança!")
