#  Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e retorna a soma de todos
#  os valores entre 0 e o valor recebido. Caso o valor seja negativo, o método deve retornar -1.

def somavalores(val1):
    if val1 > 0:
        soma = 0
        for i in range(0, val1 + 1):
            soma += i
        return soma
    else:
        return -1


print(somavalores(10))
