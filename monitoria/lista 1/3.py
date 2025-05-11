altura = float(input("Digite sua aoltura (Em metros): "))
peso = float(input("Digite seu peso (Em Kg): "))
imc = float(peso / altura**2)

print("Seu imc é" , round(imc,2))

if(imc < 18.5):
    print("Você está abaixo do peso")
elif(imc > 24.9):
    print("Você está acima do peso")
else:
    print("Seu peso está ideal")