# Crie um programa que pede para o usuário digitar números positivos via teclado. Quando o usuário digitar um
# número negativo, informe a média de todos os números que ele informou.

soma = 0
loops = 0

i = int(input("Digite um número: "))

while i > 0:
    soma += i
    loops += 1
    i = int(input("Digite um número: "))

media = soma / loops

print("A média de todos os números digitados é:", media)
