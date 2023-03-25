# . Crie um programa que solicita ao usuário que ele defina sua senha. A senha # deve ser um texto (string)
# composto apenas por dígitos e deve ter entre 5 e 10 valores. O usuário tem apenas 6 chances de definir
# corretamente a senha. Caso ele defina corretamente a senha nas tentativas que ele tem, imprima uma mensagem de
# sucesso. Caso ele não defina a senha corretamente, imprima uma mensagem de insucesso.
# Dica: na aula aprendemos a ver se uma string é formada apenas por dígitos e aprendemos a descobrir o tamanho
# do texto digitado.

print("Vamos criar uma senha contendo entre 5 e 10 dígitos.")

for i in range(1, 7):
    senha = input("Digite sua senha: ")
    if 4 < senha.__len__() < 11 and senha.isdigit():
        print("Senha criada com sucesso!")
        break
    else:
        print("A senha não atende os requisitos, tente novamente!")



