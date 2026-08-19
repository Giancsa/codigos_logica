"""Questão Desafio 
Crie uma lista contendo nomes de alunos: 
["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"] 
Verifique se um determinado nome está na lista. 
Se estiver: 
Aluno matriculado. 
Caso contrário: 
Aluno não encontrado. 
> Objetivo: utilizar lista, variável, operador in e estrutura if...else em uma única solução.  """

alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

if input("Digite o nome de um aluno: ") in alunos:
    print("Aluno matriculado")
else:
    print("Aluno não encontrado, vamos fazer a matrícula:")
    alunos.append(input("Digite o nome do aluno: "))
    print("Aluno cadastrado com sucesso" , alunos)