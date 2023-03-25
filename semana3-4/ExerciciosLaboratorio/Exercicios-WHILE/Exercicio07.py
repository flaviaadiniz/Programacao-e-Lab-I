# Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar e armazena
# em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros, e para cada
# número digitado imprima na tela se o número é negativo, positivo ou zero.

print("Vamos verificar se números são positivos, negativos ou iguais a zero!")
quant = int(input("Quantos números você quer analisar? "))

print()

i = 0
while i < quant:
    num = int(input("Digite o primeiro número: "))
    if num == 0:
        print(num, "é igual a zero!\n")
    elif num < 0:
        print(num, "é um número negativo!\n")
    else:
        print(num, "é um número positivo!\n")
    i += 1

print("--- Programa finalizado ---")
