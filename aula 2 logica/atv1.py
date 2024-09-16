idade = int(input("Digite sua idade"))
habilitação = int(input("Você tem habilitação? digite 1 para SIM e 2 para NÃO"))

if idade >= 18 and habilitação == 1:
    print("você é maior de idade e tem habilitação")
    exit()
elif idade < 18 and habilitação == 2:
    print("Você é menor de idade e não tem habilitação")
    exit()
elif idade < 18 and habilitação == 1:
    print("Você tem habilitação e é menor de idade")
    exit()
else:
    print("Você é maior de idade e não tem habilitação")



