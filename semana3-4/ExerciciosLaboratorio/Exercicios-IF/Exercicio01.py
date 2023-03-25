# Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.

valorA = int(input("Digite o valor A: "))
valorB = int(input("Digite o valor B: "))
valorC = int(input("Digite o valor C: "))

menorvalor = 0

if valorA < valorB and valorA < valorC:
    menorvalor = valorA

elif valorB < valorA and valorB < valorC:
    menorvalor = valorB

else:
    menorvalor = valorC

print("O menor valor é", menorvalor)
