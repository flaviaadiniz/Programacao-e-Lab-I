# Conditionals

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")

print()

num2 = int(input("Digite outro número inteiro: "))

if 0 <= num2 <= 10:
    print("O número está entre 0 e 10")
elif 11 <= num2 <= 20:
    print("O número está entre 11 e 20")
elif 21 <= num2 <= 100:
    print("O número está entre 21 e 100")
else:
    print("O número é maior do que 100")
