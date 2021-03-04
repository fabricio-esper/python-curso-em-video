print("Escreva dois números inteiros.")
x = int(input("primeiro número: "))
y = int(input("segundo número: "))

if x > y:
    print(f"O {x} é maior que {y}")
elif y > x:
    print(f"O {y} é maior que {x}")
else:
    print("Os dois valores são iguais.")