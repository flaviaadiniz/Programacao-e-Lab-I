# . Crie um programa que pede para o usuário digitar 2 valores inteiros via teclado (val1 e val2). Se nenhum
# dos valores for negativo, escreva os números pares entre o menor e o maior valor.

val1 = int(input("Digite um valor inteiro: "))
val2 = int(input("Digite outro valor inteiro: "))

if val1 >= 0 and val2 >= 0:
    menor = val1
    maior = val2

    if val1 > val2:
        menor = val2
        maior = val1

    cont = menor

    while cont <= maior:
        if cont % 2 == 0:
            print(cont)
        cont += 1
else:
    print("Erro! Número negativo detected!")