print("Vamos jogar Pedra, Papel e tesoura!")
from random import randint
n = randint(0,2)
itens = ("Pedra", "Papel", "Tesoura")
print("""Pedra = 0
Papel = 1
Tesoura = 2""")
r = int(input("Escolha: "))

print("-="*11)
print(f"Computador jogou {itens[n]}")
print(f"Jogador jogou {itens[r]}")
print("-="*11)

if n == 0 and r == 0 or n == 1 and r == 1 or n == 2 and r == 2:
    print("Isso é um empate!!")
elif n == 0 and r == 1 or n == 1 and r == 2 or n == 2 and r == 0:
    print("Você ganhou!!")
elif n == 0 and r == 2 or n == 2 and r == 1 or n == 1 and r == 0:
    print("Você perdeu!!")
else:
    print("Opção inválida.")
