# Crie um programa que solicita informações completas do endereço do usuário (como nome da rua, cep
# bairro, etc). Depois disto, seu programa deve imprimir na tela as informações do endereço do usuário
# de forma clara e organizada.

print("Vamos cadastrar o seu endereço!")
rua = input("Digite o nome da sua rua: ")
numero = int(input("Digite o número da casa ou prédio/apartamento: "))
bairro = input("Digite o nome do seu bairro: ")
cep = input("Digite o seu CEP: ")
cidade = input("Digite o nome da sua cidade: ")
estado = input("Digite o nome do seu estado: ")

print()

print("----------- Seu endereço: -----------")
print("Rua " + rua + ",", numero)
print("Bairro: " + bairro)
print("CEP: " + cep)
print("Bairro: " + bairro)
print("Cidade/Estado: " + cidade + "/" + estado)
