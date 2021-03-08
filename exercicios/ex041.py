print("-="*20)
print("Confederação Nacional de Natação")
print("-="*20)

from datetime import date
a = date.today().year
n = int(input("Em que ano você nasceu? "))
i = a - n

if i <= 9:
    print(f"{i} anos: MIRIM")
elif i > 9 and i <=14:
    print(f"{i} anos: INFANTIL")
elif i > 14 and i <= 19:
    print(f"{i} anos: JUNIOR")
elif i == 20:
    print(f"{i} anos: SÊNIOR")
else:
    print(f"{i} anos: MASTER") 
