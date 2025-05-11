num = [int(input('Digite uma lista de números: ').split())]
def soma(lista):
    return lista[0] + lista[-1]
result = soma(num)
print('A soma é:', result)