# Uma determinada disciplina possui apenas 3 avaliações:

# - o trabalho, que vale 10% da nota
# - a prova, que vale 60% da nota
# - o teste, que vale 30% da nota

# Crie um programa que pede para o usuário digitar as notas de cada avaliação e que imprima a nota final
# do aluno.

print("Vamos calcular a sua média final na disciplina!")
print("Para isso, preciso saber as suas 3 notas.")

trabalho = float(input("Digite a nota do trabalho: "))
prova = float(input("Digite a nota da prova: "))
teste = float(input("Digite a nota do teste: "))

mediaFinal = ((trabalho * 0.1) + (prova * 0.6) + (teste * 0.3))

print("A sua média final é %.2f" % mediaFinal)

