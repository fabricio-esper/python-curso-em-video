print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundp segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima \033[32mPODEM FORMAR\033[m triângulos")
else:
    print("Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulos")
