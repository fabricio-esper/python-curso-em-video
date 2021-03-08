p = float(input("Qual é o preço do produto? "))
print("Qual é a condição de pagamento?")
print("1- à vista no dinheiro/cheque: 10% de desconto")
print("2- à vista no cartão: 5% de desconto")
print("3- em até 2x no cartão: preço normal")
print("4- 3x ou mais no cartão: 20% de juros")
r = int(input("insira: "))

if r == 1:
    d = p - (0.1*p)
    op = str(input("dinheiro ou cheque? "))
    print(f"O pagamento à vista no {op} c/ desconto de 10% fica {d:.2f} BRL")
elif r == 2:
    d = p - (0.05*p)
    print(f"O pagamento à vista no cartão c/ desconto de 5% fica {d:.2f} BRL")
elif r == 3:
    par = p / 2
    print(f"O pagamento em 2x no cartão ficará {par:.2f} BRL a parcela")
elif r == 4:
    q = int(input("Vai pagar em quantas vezes? "))
    par = (p + (0.2*p)) / q
    print(f"O pagamento em {q}x no cartão ficará c/ juros {par:.2f} BRL a parcela")
