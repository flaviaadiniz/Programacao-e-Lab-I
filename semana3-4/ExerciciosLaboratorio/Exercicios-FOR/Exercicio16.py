# Sabendo que uma string é uma lista de letras, peça para o usuário digitar um texto e imprima na tela a
# quantidade de vogais que existem no texto.

texto = input("Digite um texto: ")
vogais = 0

for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogais += 1

print(vogais)
