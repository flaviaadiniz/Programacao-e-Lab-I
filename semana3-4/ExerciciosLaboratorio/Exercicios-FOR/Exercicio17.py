# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo # teclado. Ao final, imprima
# apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

solteiras = []
casadas = []
divorciadas = []
viuvas = []

for i in range(1, 21):
    nome = input("Nome: ")
    estadoCivil = input("Estado civil: ")

    if estadoCivil.lower() == "solteira" or estadoCivil.lower() == "solteiro":
        solteiras.append(nome)
    elif estadoCivil.lower() == "casada" or estadoCivil.lower() == "casado":
        casadas.append(nome)
    elif estadoCivil.lower() == "divorciada" or estadoCivil.lower() == "divorciado":
        divorciadas.append(nome)
    elif estadoCivil.lower() == "viúva" or estadoCivil.lower() == "viúvo":
        viuvas.append(nome)

print()
print("Solteiras:", solteiras)
print("Casadas:", casadas)
print("Divorciadas:", divorciadas)
print("Viúvas:", viuvas)
