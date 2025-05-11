classe = str(input("Digite sua classe: "))
lvl = int(input("Digite seu nível: "))
item = bool(input("Você tem um item especial? ").lower())
sim = True
if item == sim:
    if lvl >= 30:
        print("Você é um" , classe , "maior")
    else: 
        print("Você é um" , classe , "menor")
else:
    print("Você é apenas um" , classe)