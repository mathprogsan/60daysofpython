def podeDirigir(idade):
    if idade >=28:
        return True
    else:
        return False

try:
    input_user = int(input("Digite sua idade: "))
    print(podeDirigir(input_user))
except ValueError:
    print("Você não digitou um valor inteiro.")