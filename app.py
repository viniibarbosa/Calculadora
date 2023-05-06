print("***Calculadora***", end="\n")

calcular_novamente = True
encerrar = False
while(calcular_novamente != False and encerrar != True):
    print("Por favor, selecione a operação desejada na calculadora, digitando o número correspondente:", "(1) Adição","(2) Subtração", "(3) Multiplicação", "(4) Divisão", "(5) Sair", sep="\n")
    opcao_calculadora = int(input("Opção desejada: "))
    
    if(opcao_calculadora == 1):
        print("***Adição***",sep="\n" ,end="\n")
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))
        print("--------------------------------")
        print("O resultado da adição {} + {} = {}".format(num1, num2, num1+num2))
        opcao_valida = False
        while(opcao_valida != True):
            print("--------------------------------")
            print("Gostaria de continuar usando a calculadora?", "(1) Sim","(2) Não", sep="\n")
            opcao_encerrar = int(input("Opção desejada: "))
            if(opcao_encerrar == 1):
                opcao_valida = True
                encerrar = False
            elif(opcao_encerrar == 2):
                opcao_valida = True
                encerrar = True
        
    if(opcao_calculadora == 2):
        print("***Subtração***", sep="\n" ,end="\n")
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o número diminuído: "))
        print("--------------------------------")
        print("O resultado da subtração {} - {} = {}".format(num1, num2, num1-num2))
        opcao_valida = False
        while(opcao_valida != True):
            print("--------------------------------")
            print("Gostaria de continuar usando a calculadora?", "(1) Sim","(2) Não", sep="\n")
            opcao_encerrar = int(input("Opção desejada: "))
            if(opcao_encerrar == 1):
                opcao_valida = True
                encerrar = False
            elif(opcao_encerrar == 2):
                opcao_valida = True
                encerrar = True
        
    if(opcao_calculadora == 3):
        print("***Multiplicação***", sep="\n" ,end="\n")
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))
        print("--------------------------------")
        print("O resultado da multiplicação {} * {} = {}".format(num1, num2, num1*num2))
        opcao_valida = False
        while(opcao_valida != True):
            print("--------------------------------")
            print("Gostaria de continuar usando a calculadora?", "(1) Sim","(2) Não", sep="\n")
            opcao_encerrar = int(input("Opção desejada: "))
            if(opcao_encerrar == 1):
                opcao_valida = True
                encerrar = False
            elif(opcao_encerrar == 2):
                opcao_valida = True
                encerrar = True
        
    if(opcao_calculadora == 4):
        print("***Divisão***", sep="\n" ,end="\n")
        num1 = int(input("Digite o dividendo: "))
        num2 = int(input("Digite o divisor: "))
        print("--------------------------------")
        print("O resultado da divisão {} / {} = {}".format(num1, num2, num1/num2))
        opcao_valida = False
        while(opcao_valida != True):
            print("--------------------------------")
            print("Gostaria de continuar usando a calculadora?", "(1) Sim","(2) Não", sep="\n")
            opcao_encerrar = int(input("Opção desejada: "))
            if(opcao_encerrar == 1):
                opcao_valida = True
                encerrar = False
            elif(opcao_encerrar == 2):
                opcao_valida = True
                encerrar = True

    if(opcao_calculadora == 5): 
        opcao_valida = True
        encerrar = True

    
print("Fim!")