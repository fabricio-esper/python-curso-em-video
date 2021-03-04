from datetime import date
a = date.today().year
n = int(input("Em que ano você nasceu? "))
i = a - n 

if i > 18:
    print(f"Você tem {i}, já passou {i - 18} ano(s) do seu alistamento.")
elif i == 18:
    print(f"Você tem {i}, está na época de se alistar.")
else:
    print(f"Você tem {i}, falta {18 - i} ano(s) para chegar a sua vez de se alistar.")
