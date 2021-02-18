from random import randint
n1 = randint(1,5)
n2 = int(input("Tente descobrir o numero de 1 a 5 que estou pensando!: "))
if n1 == n2:
    print(f"Voce esta certissimo, o numero e {n1}!")
else:
    print(f"Sinto muito, o numero certo e {n1}!")
