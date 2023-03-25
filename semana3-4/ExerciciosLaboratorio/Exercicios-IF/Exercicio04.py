# Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:

# • Digite 1 para somar dois valores
# • Digite 2 para subtrair dois valores
# • Digite 3 para multiplicar dois valores
# • Digite 4 para dividir dois valores
# • Digite 5 para realizar uma potência entre dois valores
# • Digite 6 para realizar uma radiciação entre dois valores
# • Digite qualquer outro número para sair

# De acordo com a opção informada pelo usuário, solicite os valores necessários para o usuário e imprima na tela
# o resultado da operação realizada.

import math

print("Vamos fazer cálculos matemáticos! :)")
print("Digite 1 para somar dois valores")
print("Digite 2 para subtrair dois valores")
print("Digite 3 para multiplicar dois valores")
print("Digite 4 para dividir dois valores")
print("Digite 5 para realizar uma potência entre dois valores")
print("Digite 6 para realizar uma radiciação entre dois valores")
print("Digite qualquer outro número para sair\n")

opcao = int(input("Digite a sua escolha: "))

if opcao == 1:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da soma é:", valor1 + valor2)

elif opcao == 2:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da subtração é:", valor1 - valor2)

elif opcao == 3:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da multiplicação é:", valor1 * valor2)

elif opcao == 4:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da divisão é:", valor1 / valor2)

elif opcao == 5:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da potenciação é:", math.pow(valor1, valor2))

elif opcao == 6:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("O resultado da radiciação é: %.2f" % (valor1 ** (1/valor2)))

else:
    print("Encerrando o programa...")
