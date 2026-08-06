#Criar um cadastro a partir do cpf
import re
regex_cpf = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"

while True:
    print("Opção 1 = Cadastrar CPF")
    print("Opcção 2 = Consultar CPF")

    opcao = int(input("Digite uma opçao"))
    if opcao == 1:
        cpf = input("Digite seu cpf para cadastro: ")
        if re.fullmatch(regex_cpf, cpf):
                print("CPF válido")
                break
        else:
                print("CPF Inválido, digite novamente: ")
                print("="*30)