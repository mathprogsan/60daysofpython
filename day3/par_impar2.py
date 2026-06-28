entrada = input("Digite um número: ")

try:
    numero = int(entrada)    
    if numero % 2 == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é ímpar!")
except ValueError:
    print("Essa entrada não é um número inteiro.")