# Crie um programa que pede para o usuário digitar 20 números com ponto flutuante pelo teclado. Ao final,
# seu programa deve imprimir todos os números digitados. Dica: armazene-os em uma string e concatene os valores
# digitados. No final, imprima a string.

print("Vamos criar uma lista com 20 números!")

i = 0
listaNumeros = []

while i <= 20:
    listaNumeros.append(input("Digite o primeiro número: "))
    i += 1

print(listaNumeros)
