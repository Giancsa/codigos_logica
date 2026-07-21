bd_usuarios = ["admin", "admin1", "admin2"]

while True:

    print("========================")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Mostrar usuários")
    print("4 - Sair")
    print("========================")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":

     print("Vamos fazer seu cadastro")

    usuario = input("Digite o usuário desejado: ")

    while usuario in bd_usuarios:
        print("Nome de usuário já existe.")
        usuario = input("Digite outro usuário: ")

    senha = input("Digite a senha: ")
    senha2 = input("Confirme a senha: ")

    while senha != senha2:
        print("As senhas não conferem.")
        senha = input("Digite novamente: ")
        senha2 = input("Confirme novamente: ")

    bd_usuarios.append(usuario)

    print("Conta cadastrada com sucesso!")

    elif opcao == "2":

     usuario_login = input("Usuário: ")
     senha_acesso = input("Senha: ")

     while not (usuario_login == usuario and senha_acesso == senha):
        print("Usuário ou senha inválidos.")

        usuario_login = input("Usuário: ")
        senha_acesso = input("Senha: ")

      print("Acesso liberado!")

    