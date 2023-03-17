# Variáveis

idade = 38
x = "Teste"

print("Variável idade =", idade)
print("Variável x =", x)
print()

# input recebe dados via teclado e salva na variável indicada, sempre em formato STRING:
nome = input("Digite seu nome: ")
print("Seu nome é:", nome)
print()

# para salvar dados de outro tipo, colocar o tipo na frente de input:
preco = float(input("Digite o preço do produto: "))
print("O preço é ", preco)
print("-------------------------------------------------")

precoProduto1 = float(input("Digite o preço do produto 1: "))
precoProduto2 = float(input("Digite o preço do produto 2: "))

precoTotal = precoProduto1 + precoProduto2
print("Preço total:", precoTotal)
print("Preço médio dos produtos:", precoTotal / 2)

desconto = precoTotal * 0.1
print("O valor do desconto é de", desconto)
print("O valor final dos 2 produtos é de", precoTotal - desconto)

