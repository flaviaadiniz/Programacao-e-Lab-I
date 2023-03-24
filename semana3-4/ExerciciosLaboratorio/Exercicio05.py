# . Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final, # imprima quantos torcedores
# torcem para o Grêmio.

i = 0
torcedoresGremio = 0

while i <= 10:
    resposta = input("Digite o seu time: ")
    if resposta == "Grêmio" or resposta == "Gremio":
        torcedoresGremio += 1
    i += 1

print("O número de pessoas que torce para o Grêmio é:", torcedoresGremio)
