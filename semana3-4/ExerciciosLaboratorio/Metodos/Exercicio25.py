# Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string) e retorna
# a menor string da lista (com menos caracteres).

nomes = ["Flávia", "Roberta", "Marcela", "Angela", "Ana", "Eduarda"]


def menorpalavra(lista):
    string = lista[0]
    tamanhostring = len(string)

    for item in lista:
        tamanhoitem = len(item)

        if tamanhoitem < tamanhostring:
            string = item

    return string


print(menorpalavra(nomes))

