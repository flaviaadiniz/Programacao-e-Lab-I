#  Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido pela média aritmética
#  das notas. Os conceitos são:
# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO".


def getconceito(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        print("ERRO!")

    else:

        media = (nota1 + nota2 + nota3) / 3
        conceito = ""

        if 0.0 < media <= 4.0:
            conceito = "D"
        elif 4.0 < media <= 7.0:
            conceito = "C"
        elif 7.0 < media <= 9.0:
            conceito = "B"
        elif 9.0 < media <= 10.0:
            conceito = "A"

        return conceito


print("Conceito:", getconceito(9.8, 7.2, 8))
