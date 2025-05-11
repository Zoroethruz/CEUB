sexo = str(input("Digite seu sexo: ").lower())
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de contribuição: "))

if sexo == "masculino" :
    if idade >= 64 and tempo >= 35:
        print("Pode aposentar")
    else:
        print("Não pode aposentar")
else:
    if idade >= 59 and tempo >= 30:
        print("Pode aposentar")
    else:
        print("Não pode aposentar")