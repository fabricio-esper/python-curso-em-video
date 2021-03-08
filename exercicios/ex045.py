print("Vamos jogar Pedra, Papel e tesoura!")
from random import randint
n = randint(1,3)
print("Pedra = 1")
print("Papel = 2")
print("Tesoura = 3")
r = int(input("Escolha: "))

if n == 1:
    print("PEDRA!!")
elif n == 2:
    print("PAPEL!!")
elif n == 3:    
    print("TESOURA!!")

if n == 1 and r == 1 or n == 2 and r == 2 or n == 3 and r == 3:
    print("Isso é um empate!!")
elif n == 1 and r == 2 or n == 2 and r == 3 or n == 3 and r == 1:
    print("Você ganhou!!")
elif n == 1 and r == 3 or n == 3 and r == 2 or n == 2 and r == 1:
    print("Você perdeu!!")
else:
    print("Opção inválida.")