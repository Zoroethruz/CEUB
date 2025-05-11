num = [int(x) for x in input('Digite uma lista de números: ').split()]
def acharmaior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
maiornum = acharmaior(num)
print('O maior é:', maiornum)