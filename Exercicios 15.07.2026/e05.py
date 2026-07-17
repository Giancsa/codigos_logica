"""Questão 5 – Sistema de notas: 

Crie uma variável chamada nota. 
Utilize if...elif...else para classificar: 
Nota - Resultado 
9 a 10 - Excelente 
7 a 8.9 - Aprovado 
5 a 6.9 - Recuperação 
Menor que 5 - Reprovado """

nota = float(input("Digite a nota do aluno: "))
while nota >10:
    nota = float(input("Nota maior que a permitida, digite novamente "))
if nota >=9:
    print("Excelente")
elif nota >=7:
    print("Aprovado")
else:
    print("Rcuperação")

