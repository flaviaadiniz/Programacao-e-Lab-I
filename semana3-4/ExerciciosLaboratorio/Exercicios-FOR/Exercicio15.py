# Crie um programa que imprime a tabuada de um número qualquer digitado pelo usuário.

num = int(input("Digite um número inteiro para ver a sua tabuada: "))

for i in range(1, 11):
    print(i, "x", num, "=", i * num)

