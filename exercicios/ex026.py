frase = input("Digite uma frase: ").upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'Ela aparece em {frase.find("A")+1} e {frase.rfind("A")+1}')
