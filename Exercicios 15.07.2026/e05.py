"""Questão 5 – Sistema de notas: 

Crie uma variável chamada nota. 
Utilize if...elif...else para classificar: 
Nota - Resultado 
9 a 10 - Excelente 
7 a 8.9 - Aprovado 
5 a 6.9 - Recuperação 
Menor que 5 - Reprovado """

nota = input("Digite a nota do aluno: ")
nota = float(nota.replace(",", "."))
while nota >10:
    nota = (input("Nota maior que a máxima permitida, digite novamente "))
    nota = float(nota.replace(",", "."))

if nota >=9:
    print("Excelente")
elif nota >=7:
    print("Aprovado")
elif nota >=5:
    print("Recuperação")
else:
    print("Reprovado")

