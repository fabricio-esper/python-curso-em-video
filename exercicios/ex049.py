n = int(input('Digite um número para ver sua tabuada: '))

print("-" * 12)
for t in range(0,11):
    print(f"{n} x {t:2} = {n*t}")
print("-" *12)
