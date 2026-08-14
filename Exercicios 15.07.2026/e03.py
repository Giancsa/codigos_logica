"""Questão 3 – Lista de frutas 

Crie uma lista contendo pelo menos 5 frutas. 
Depois: 
Exiba a lista completa. 
Exiba apenas a primeira fruta. 
Exiba apenas a última fruta. 
Adicione algumas frutas e exiba a última, independentemente da quantidade. """

frutas = ["banana", "maçã", "morango", "abacaxi", "melancia"]
print(frutas)
print(frutas[0])
print(frutas[4])
frutas.extend(["pessêgo", "pera", "abacaxi"])
print("A lista contém até o momento", frutas)
print("O ultimo item da lista é:", frutas[-1])