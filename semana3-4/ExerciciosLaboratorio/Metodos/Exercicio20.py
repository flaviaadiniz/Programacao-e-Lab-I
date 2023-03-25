#  Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros). O método deve retornar
#  verdadeiro se val1 for divisível por val2 e falso caso contrário.

def verdadeiroOuFalso(val1, val2):
    if val1 % val2 == 0:
        return True
    else:
        return False


print(verdadeiroOuFalso(6, 3))
