import random
import string

def geradorSenhas(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    while len(senha) < tamanho:
        senha += random.choice(caracteres)

    print(f"Sua senha ficou assim {senha}")

try:
    comprimento = int(input("Quantidade de caracteres da sua senha: "))
    geradorSenhas(comprimento)
except ValueError:
    print("Número inválido. Escreva um número inteiro.")
