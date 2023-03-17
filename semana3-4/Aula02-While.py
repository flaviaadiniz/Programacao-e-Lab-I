# Loops - WHILE

num = int(input("Digite um número de 1 a 10: "))

while num <= 10:
    print(num)
    num += 1

print("\n-------------------------------------------------------------------------")

i = 0
while i < 10:
    print("Valor de i:", i)
    i += 1

print("\n-------------------------------------------------------------------------")

op = int(input("Digite 3 para sair: "))

while op != 3:
    print("Opção digitada:", op, "\nVocê não saiu\n")
    op = int(input("Digite 3 para sair: "))
print("Saindo...")







