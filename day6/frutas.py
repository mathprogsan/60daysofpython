frutas = ['maça','banana','laranja','limão','jabuticaba']
for fruta in frutas:
    print(fruta)

while True:
    fruta = input("Digite a fruta desejada: ")
    if fruta == "sair":
        break
    else:
        frutas.append(fruta)
print(frutas)