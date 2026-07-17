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

print("Vamos fazer seu cadastro")
print("============================")
#CRIAÇÃO DE SENHA
usuario = input("Digite o usuário desejado: ")
senha = input("Agora digite a senha: ")
senha2 = input("Digite a senha novamente: ")
while senha != senha2:
    senha = input("Senha não confere, digite novamente: ")
    senha2= input("Confirme novamente: ")
else:
    print("================================")
    print("Conta cadastrada com sucesso")
print("================================")
print("=======ACESSO AO SISTEMA========")

#CONFIRMAÇÃO DE LONGIN
usuario_login = input("Digite o usuario para acesso: ")
senha_acesso = input("Digite sua senha: ")

while senha_acesso != senha2 or usuario_login != usuario:
    print("Usuário ou senha inválido, digite novamente:")
    usuario_login = input("Digite o usuario para acesso: ")
    senha_acesso = input("Digite sua senha: ")
else: 
    print("============================")
    print("   Acesso liberado!")
    print("============================")

print("senha: ", senha, "senha_acesso: ", senha_acesso)