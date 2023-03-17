# Uma disciplina possui Grau A e Grau B. A nota do Grau A vale 33% da nota final, enquando a nota do
# Grau B vale 67% da noa final.

# O Grau A possui as seguintes avaliações:
# - atividade prática: 45% da nota do Grau A
# - atividade teórica: 55% da nota do Grau A

# O Grau B possui as seguintes avaliações:
# - prova em laboratório: 60% da nota do Grau B
# - teste teórico: 20% da nota do Grau B
# - trabalho extraclasse: 20% da nota do Grau B

# Crie um programa que solicite as notas de cada avaliação e imprima na tela a nota final da disciplina.


print("Vamos calcular a sua nota final na disciplina de Programação I")
print()

print("Primeiro, precisamos das notas das atividades do Grau A.")
atPratica = float(input("Digite a nota da atividade prática: "))
atTeorica = float(input("Digite a nota da atividade teórica: "))
grauA = (atPratica * 0.45) + (atTeorica * 0.55)
print()

print("Agora precisamos das notas das atividades do Grau B.")
provaLab = float(input("Digite a nota da prova em laboratório: "))
testeTeorico = float(input("Digite a nota do teste teórico: "))
trabExtra = float(input("Digite a nota do trabalho extraclasse: "))
grauB = (provaLab * 0.6) + (testeTeorico * 0.2) + (trabExtra * 0.2)
print()

notaFinal = (grauA * 0.33) + (grauB * 0.67)

print("A nota final da disciplina é %.2f" % notaFinal)




