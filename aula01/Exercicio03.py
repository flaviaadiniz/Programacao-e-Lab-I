# Crie um programa que pede para o usuário digitar 5 números inteiros e os armazene, respectivamente, nas
# variáveis A, B, C, D e E. Em seguida, faça o que se pede:

# - sabendo que B e C são, respectivamente, a base e a altura de um triângulo, imprima a sua área
# - sabendo que A, B, C e D formam um retângulo, imprima o seu perímetro
# - sabendo que E é o valor do raio de um círculo, imprima a área deste círculo

import math

print("Vamos trabalhar com 5 números novamente!")
A = int(input("Digite o número A: "))
B = int(input("Digite o número B: "))
C = int(input("Digite o número C: "))
D = int(input("Digite o número D: "))
E = int(input("Digite o número E: "))

areaTriangulo = (B * C) / 2
perimetroRetangulo = A + B + C + D
areaCirculo = math.pi * (E * E)

print("A área do triângulo com base", B, "e altura", C, "é igual a", areaTriangulo)
print("O perímetro do retângulo com lados", A, ",", B, ",", C, "e", D, "é igual a", perimetroRetangulo)
print("A área do círculo com raio", E, "é igual a %.2f" % areaCirculo)





