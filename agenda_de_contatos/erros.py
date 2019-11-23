'''
1) Erros em tempo de compilação
2) Erros em tempo de execução
3) Erros de lógica
'''
while True:
    try:
        a = int(input('Digite o numero A: ')) #ValueError
        b = int(input('Digite o numeri B: '))

        if a == 0:
            print("Divisão por zero não pode ser feita.")
        else:
            print(a / b)  # ZeroByDivisionError
    except ValueError:
        print("Digite apenas números")
    except ZeroDivisionError:
        print("Divisão por zero não pode ser feita.")
    except Exception as error:
        print("Erro desconhecido. Contate a equipe.")
        print(error)
