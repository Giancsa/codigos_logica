'''Criar um cadastro a partir do cpf recebendo dados do usuário (CPF, NOME, NASCIMENTO, EMAIL, TELEFONE)
e consultar dos dados no dicionário através do e-mail'''
import re
regex_cpf = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"

while True:

    print("--> Opção 1 = Cadastrar CPF")
    print("--> Opção 2 = Consultar CPF")

    print("")
    opcao = int(input("Digite uma opçao: "))
    print("")
    
    if opcao == 1:
                
          cpf = input("Digite seu cpf para cadastro: ")
          validacao = re.fullmatch(regex_cpf, cpf)
          while validacao == None:
            print("CPF inválido, digite novamente: ")
            cpf = input("Digite seu cpf para cadastro: ")
            validacao = re.fullmatch(regex_cpf, cpf)
          else:
            nome =input("Digite o nome para cadastro: ")