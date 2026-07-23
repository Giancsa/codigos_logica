"""Questão Desafio 

Crie uma lista contendo nomes de alunos: 
["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"] 
Verifique se um determinado nome está na lista. 
Se estiver: 
Aluno matriculado. 
Caso contrário: 
Aluno não encontrado. 
> Objetivo: utilizar lista, variável, operador in e estrutura if...else 
em uma única solução. """
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

while True:
    print("1 - Cadastrar")
    print("2 - Consultar")
    
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        
        aluno_cadastro = input("Digite o nome do aluno a ser cadastrado: ")
        alunos.append(aluno_cadastro)

    if opcao == "2":

        nome = input("Digite o nome do aluno que deseja consultar: ")
        if nome in alunos:
            print(f"Aluno(a) {nome} Matriculado(a)")
        else:
            print("Aluno não cadastrado, faça o cadastro")