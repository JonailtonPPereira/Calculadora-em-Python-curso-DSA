# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

chose = 0
while chose != " ": #Alterar esse valor de 0 para que faça sentido para operação
    chose = int(input("Selecione o número da operação desejada 1.Soma/2.Subtração/3.Multiplicação/4.Divisão/0.Finalizar: "))

    if chose == 1:
        resultado = 0
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        resultado = x + y
        print(resultado)
              
    elif chose == 2:
        resultado = 0
        x = int(input("Digite o Minuendo: "))
        y = int(input("Digite o subtraendo: "))
        resultado = x - y
        print(resultado)

    elif chose == 3:
        resultado = 0
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        resultado = x * y
        print(resultado)

    elif chose == 4:
        resultado = 0
        x = int(input("Digite o dividendo: "))
        y = int(input("Digite o divisor: "))
        resultado = x / y
        print(resultado)

    elif chose == 0:
        print("Operação finalizada com sucesso")
        exit(1)

    chose = int(input("Selecione o número da operação desejada 1.Soma/2.Subtração/3.Multiplicação/4.Divisão/0.Finalizar: "))