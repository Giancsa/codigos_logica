'''Criar um cadastro a partir do cpf recebendo dados do usuário (CPF, NOME, NASCIMENTO, EMAIL, TELEFONE)
e consultar dos dados no dicionário através do e-mail'''
import re
regex_cpf = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
regex_nascimento = r"^\d{2}/\d{2}/\d{4}$"
regex_email = regex_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

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
            
            Nascimeno = input("Digite sua data de nascimento(DD/MM/AAAA): ")
            val_nasc = re.fullmatch(regex_nascimento, Nascimeno)
            while val_nasc == None:
              print("Formato de nascimento inválido!")
              Nascimeno = input("Digite sua data de nascimento novamente: ")
              val_nasc = re.fullmatch(regex_nascimento, Nascimeno)
            else:
              email = input("Digite seu E-mail para cadastro: ")
              val_email = re.fullmatch (regex_email, email)
              while val_email == None:
                email = print("Formato de E-mail inválido, digite novamente: ")
                val_email = re.fullmatch (regex_email, email)