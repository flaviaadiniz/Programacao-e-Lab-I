# Crie um método que recebe um valor por parâmetro (assuma que será uma string) e retorna a quantidade de
# letras ou outros caracteres que não sejam espaço que existem neste texto.

def numeroletras(palavra):
    caracteres = 0
    for letra in palavra:
        if letra != " ":
            caracteres += 1
    return caracteres


print(numeroletras("I love Java"))

