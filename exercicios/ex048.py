s = 0
for i in range(1,501):
    if i % 2 != 0:
        if i % 3 == 0:
            s += i
    
print(f"A soma entre os números ímpares, multiplos de 3, que estão entre 1 e 500 é {s}")
