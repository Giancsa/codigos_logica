"""Questão 7 – Acesso ao sistema (operador AND) 

Crie as variáveis: 
usuario = "admin" 
senha = "1234" 
Utilize o operador and para verificar se: 
usuário é "admin" 
senha é "1234" 
Se ambas as condições forem verdadeiras: 
Acesso permitido. 
Caso contrário: 
Acesso negado. """

#BASE DE DADOS
bd_usuarios = ["admin", "admin1", "admin2"]

#CRIAÇÃO DE SENHA
print("=" *30)
print("Vamos fazer seu cadastro")
print("=" *30)

usuario = input("Digite o usuário desejado: ")
while usuario in bd_usuarios:
    print("Nome de usuário já existe, escolha outro")
    usuario = input("Digite o usuário desejado: ")
senha = input("Agora digite a senha: ")
senha2 = input("Digite a senha novamente: ")
while senha != senha2:
    senha = input("Senha não confere, digite novamente: ")
    senha2= input("Confirme novamente: ")
else:
    print("=" *30)
    print("Conta cadastrada com sucesso")
    print("=" *30)
print("=======ACESSO AO SISTEMA========")
bd_usuarios.append(usuario)
print(bd_usuarios)

#CONFIRMAÇÃO DE LONGIN
usuario_login = input("Digite o usuario para acesso: ")
senha_acesso = input("Digite sua senha: ")

while not (senha_acesso == senha and usuario_login == usuario):
    print("Usuário ou senha inválido, digite novamente:")
    usuario_login = input("Digite o usuario para acesso: ")
    senha_acesso = input("Digite sua senha: ")
else: 
    print("=" *30)
    print("   Acesso liberado!")
    print("=" *30)