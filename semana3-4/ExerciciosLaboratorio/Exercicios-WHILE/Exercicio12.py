# Crie um programa que diga se o número informado pelo usuário é primo ou não.

num = int(input("Digite um valor inteiro para descobrir se ele é primo: "))

isPrimo = True
cont = 2

while cont < num:
  if num % cont == 0:
    isPrimo = False
    break
  cont += 1


if isPrimo:
  print("É primo!")
else:
  print("Não é primo!")
