numero = int(input("Digite o numero desejado para tabuada "))

for x in range (11): 
    print(x, "x", numero, "=", x*numero)
    print(f"{x} x {numero} = {x*numero}")
    print("")