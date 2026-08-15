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
    print("\n[MULTIPLICAÇÃO]\n")
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
    
    
     
    
def division():
    cls()
    print("\n[DIVISÃO]\n")
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

    

def addition():
    cls()
    print("\n[ADIÇÃO]\n")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    result = num1+num2
    print(f"{num1} + {num2} =", result)
    print()
    opcao = input("Deseja fazer outra adição? S/N ")
    if opcao.upper() == "S":
            addition()
    else:
        main()
    

def subtraction ():
    cls()
    print("\n[SUBTRAÇÃO]\n")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    cls()
    result = num1-num2
    print(f"{num1} - {num2} =", result)
    print()
    opcao = input("Deseja fazer outra adição? S/N ")
    if opcao.upper() == "S":
        addition()
    else:
        main()

def main(error=str()):
    #Programa principal
    while True:
        cls()
        print("\n[CALCULADORA: ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]\n")

        print('''Digite a opção desejada: 
        
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Encerrar o programa e fechar\n''')

        if error:
            print("-----ERRO DIGITE UMA OPÇÃO VÁLIDA!-----")

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
                cls()
                print("Programa encerrado, obrigado por usar\n")
                exit()
            case _:
                error = "Opção inválida, digite novamente!"
                main(error)
            




main()



