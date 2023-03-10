# Crie um programa que pede para o usuário digitar 5 números inteiros e imprime as seguintes informações:
# - a soma de todos os números
# - o produto de todos os números

print("Vamos trabalhar com 5 números!")
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))
num4 = int(input("Digite o número 4: "))
num5 = int(input("Digite o número 5: "))

soma = num1 + num2 + num3 + num4 + num5
produto = num1 * num2 * num3 * num4 * num5

print("A soma dos 5 números é igual a", soma)
print("O produto dos 5 números é igual a:", produto)
