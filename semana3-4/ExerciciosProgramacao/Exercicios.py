# Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número", num, "é par!")
else:
    print("O número", num, "é ímpar!")


# Exercício 2: Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido
# por B. Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão
print()

print("Vamos fazer uma divisão!")

numA = int(input("Digite um número inteiro: "))
numB = int(input("Digite outro número inteiro: "))

if numB == 0:
    print("Erro! Não existe divisão por zero!")
else:
    resultado = numA/numB
    print(numA, "/", numB, "= %.2f" % resultado)


# Exercício 3. Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o
# ano informado é bissexto ou não (para simplificar, você pode utilizar apenas a informação de o ano é
# divisível por 4 ou não).
print()

ano = int(input("Digite um ano válido (entre 1 e 2023): "))
if ano % 4 == 0:
    print(ano, "é bissexto!")
else:
    print(ano, "não é bissexto!")


# Exercício 4. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se
# será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, sendo o GA valendo 30%
# e o GB valendo 70%). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o
# cálculo.
print()

print("Vamos calcular sua média!")
grauA = float(input("Digite o Grau A: "))
grauB = float(input("Digite o Grau B: "))

if grauA < 0 or grauB < 0:
    print("Erro! A nota não pode ser menor do que ZERO.")
else:
    media = (grauA * 0.3) + (grauB * 0.7)
    if 7 <= media:
        print("Média final %.2f" % media, ". Aprovado!")
    else:
        print("Média final %.2f" % media, ". Não aprovado, precisa realizar o Grau C.")


# Exercício 5. Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma
# vogal ou uma consoante.
print()

vogais = ["A", "E", "I", "O", "U"]

letra = input("Digite uma letra do alfabeto: ")

if vogais.__contains__(letra):
    print("A letra digitada é uma vogal!")
else:
    print("A letra digitada é uma consoante!")


# Exercício 6. Utilizando while, crie um programa que imprime os números de 0 a 1000.
print()

i = 0
while i <= 1000:
    print(i)
    i += 1


# Exercício 7. Utilizando while, crie um programa que imprime os números pares de 0 a 2000.
print()

i = 0
while i <= 2000:
    if i % 2 == 0:
        print(i)
    i += 1


# Exercício 8. Utilizando while, crie um programa que imprime os números de 0 a 1000 em ordem decrescente
# (ou seja, de 1000 a 0).
print()

i = 1000
while i >= 0:
    print(i)
    i -= 1


# Exercício 9. Utilizando while, crie um programa que solicita para o usuário que ele digite 10 valores inteiros.
# Ao final, imprima a soma de todos os valores digitados.
print()

print("Vamos somar 10 números!")

cont = 0
soma = 0

while cont < 10:
    valor = int(input("Digite um número: "))
    soma += valor
    cont += 1

print("A soma dos 10 valores é:", soma)


# Exercício 10. Utilizando for, crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o 100).
print()

for i in range(1, 101):
    print(i)


# Exercício 11. Utilizando for, crie um programa que imprime a tabuada de um número inteiro digitado pelo usuário.
print()

num = int(input("Digite um número para ver a sua tabuada: "))
cont = 1

for i in range(1, 11):
    result = cont * num
    print(i, "x", num, "=", result)
    cont += 1


# Exercício 12. Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente, solicite que
# ele informe quantos produtos serão adicionados na lista. Depois disto, peça para que o usuário digite os
# produtos que ele vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras do usuário.
print()

itens = int(input("Vamos criar uma lista de compras! Quantos itens deseja adicionar? "))
lista = []

for i in range(0, itens):
    lista.append(input("Digite o item: "))

print("\nLista de compras:")
for i in lista:
    print("-", i)
