# Criando métodos
def meuMetodo():
    print("Testando métodos em Python.")


print("Chamando meu método:")
meuMetodo()

print("-----------------------------------------------------------------------")
def somar(a, b):
    print(a+b)


print("Chamando método para somar 2 números:")
somar(2, 3)

print("-----------------------------------------------------------------------")
def metodoComMaisParametros(nome, time, idade):
    print("Seu nome é", nome, ",você torce para o", time, "e tem ", idade, "anos.")

print("Chamando método com mais parâmetros:")
metodoComMaisParametros("Flávia", "Grêmio", 38)

print("-----------------------------------------------------------------------")
def somaComRetorno(a, b):
    return a + b

print("Chamando método soma com retorno:")
soma = somaComRetorno(3,6)
print(soma)

print("-----------------------------------------------------------------------")
def parOuImpar(num):
    if num % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")


parOuImpar(10)
parOuImpar(9)
