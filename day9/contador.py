def contador ():
    try:
        limite = int(input("Digite o limite para seu contador: "))
        limite += 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Você atingiu o limite.")
                break
    except ValueError:
        print("Valor inválido. Insira um número inteiro.")

contador()