import subprocess
import os

#APAGAR TELA
def cls():
    #Limpa a tela
    if os.name == "nt":
        #Se o sistema é Windows 
        subprocess.run("cls", shell=True)
    else:
        #Outros S.O, Linux e MacOS
        subprocess.run("clear", shell=True)

#CONTA MULTIPLICAÇÃO
def multiplication():
    cls()
    print("\n[MULTIPLICAÇÃO]")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    cls()
    result = num1*num2
    print("\n[RESULTADO]\n")
    print(f"{num1} x {num2} =", result)
    print()
    opcao = input("Deseja fazer outra multiplicação? S/N ")
    if opcao.upper() == "S":
        multiplication()
    else:
        main()
    
#Conta divisão    
def division():
    cls()
    print("\n[DIVISÃO]")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
     
    while num2 ==0:
     num2 = float(input("Zero não pode ser um divisor, digite novamente!: "))
     cls()
    else:
        cls()
        result = num1/num2
        print("\n[RESULTADO]\n")
        print(f"{num1} / {num2} =",result)
        print()
    opcao = input("Deseja fazer outra divisão? S/N ")
    if opcao.upper() == "S":
            division()
    else:
        main()

    
#Conta adição
def addition():
    cls()
    print("\n[ADIÇÃO]")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    cls()
    result = num1+num2
    print("\n[RESULTADO]\n")
    print(f"{num1} + {num2} =", result)
    print()
    opcao = input("Deseja fazer outra adição? S/N ")
    if opcao.upper() == "S":
            addition()
    else:
        main()
    
#Conta subtração
def subtraction ():
    cls()
    print("\n[SUBTRAÇÃO]")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    cls()
    result = num1-num2
    print("\n[RESULTADO]")
    print(f"{num1} - {num2} =", result)
    print()
    opcao = input("Deseja fazer outra adição? S/N ")
    if opcao.upper() == "S":
        addition()
    else:
        main()

#Tabuada
def tabuada():
    cls()
    numero = int(input("Digite o numero desejado para tabuada: "))
    num2 = int(input("Digite até quanto a tabuada irá: "))
    cls()
    print("\n[RESULTADO]")
    for x in range (num2 + 1): 
     print(f"{x} x {numero} = {x*numero}")
    

    opcao = input("\nDeseja fazer outra tabuada? S/N")
    if opcao.upper() == "S":
        tabuada()
    else:
        main()

def main(error=str()):
    #Programa principal
    while True:
        cls()
        print("\n[CALCULADORA: ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO] e TABUADA\n")

        print('''Digite a opção desejada: 
        
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Tabuada
        6 - Encerrar o programa e fechar\n''')

        if error:
            print("-----ERRO!! DIGITE UMA OPÇÃO VÁLIDA!-----")

        opcao = input("\nDigite uma opção: ")

        match opcao:
            case "1":
                addition()
            case "2":
                subtraction()
            case "3":
                multiplication()
            case "4":
                division()
            case "5":
                tabuada()    
            case "6":
                cls()
                print("Programa encerrado, obrigado por usar\n")
                exit()
            case _:
                error = "Opção inválida, digite novamente!"
                main(error)
            

main()



