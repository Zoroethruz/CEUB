n = input("Dá uns número ae> ").split()
cont = 0
for lista in n:
 if int(lista) % 2 == 0:
    cont += 1
print(f"Número de pares: {cont}")