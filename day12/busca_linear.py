def busca_linear(lista, procurado):
    for i, numero in enumerate(lista):
        if numero == procurado:
            return i
    return -1

lista = [3,4,2,6,5,9,8,11,13,16]
procurado = 16

indice = busca_linear(lista, procurado)

if indice != -1:
    print(f"O número se encontra no índice {indice}.")
else:
    print("Número não encontrado.")