# Crie um programa que imprima a soma dos valores pares e a soma dos valores ímpares entre dois números
# quaisquer digitados pelo usuário.

valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))

inicio = 0
fim = 0

if valor1 < valor2:
    inicio = valor1
    fim = valor2
else:
    inicio = valor2
    fim = valor1

somaImpares = 0
somaPares = 0

while inicio <= fim:
    if inicio % 2 == 0:
        somaPares += inicio
    else:
        somaImpares += inicio
    inicio += 1


print("A soma de todos os números pares entre", valor1, "e", valor2, "é:", somaPares)
print("A soma de todos os números ímpares entre", valor1, "e", valor2, "é:", somaImpares)


