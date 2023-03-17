# Range - cria listas dentro do range estipulado (excluindo o último valor)

range(1, 10)  # cria uma lista com números de 1 até 9
range(2, 5)  # cria uma lista com números de 2 a 4

for i in range(1, 10):
    print(i)

print("\n--------------------------------------------------------\n")

minhaLista = [] #  cria uma lista vazia

minhaLista.append("Frankensetein") #  append adiciona item na lista
minhaLista.append("O Sol Brilha para Todos")
minhaLista.append("Harry Potter")

for livro in minhaLista:
    print(livro)
