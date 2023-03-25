# Crie um programa que imprime na tela todos os valores entre dois valores digitados pelo teclado.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

menor = 0
maior = 0

if num1 < num2:
    menor = num1 + 1
    maior = num2
else:
    menor = num2 + 1
    maior = num1

print("Os números entre", menor, "e", maior, "são: ")
for i in range(menor, maior):
    print(i)