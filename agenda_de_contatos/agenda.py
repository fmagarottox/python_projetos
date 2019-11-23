AGENDA = {}

# AGENDA['Filipe'] = {
#     'telefone': '96474-1997',
#     'email': 'filipemagarottosc@gmail.com',
#     'endereco': 'Rua Tiradentes'
# }
#
# AGENDA['Ana'] = {
#     'telefone': '91234-5678',
#     'email': 'ana@gmail.com',
#     'endereco': 'Vila Cardoso'
# }

def mostrar_agenda():
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>> Agenda vazia')


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("E-mail:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
        print('---------------------------------')
    except KeyError:
        print(">>> Contato inexistente.")
    except Exception as error:
        print(">>> Erro inesperado ocorreu: ")
        print(error)


def incluir_editar_contato(contato):
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print()
    print('>>>> Contato "{}" adicionado com sucesso.'.format(contato))
    print()


def exportar_contatos():
    try:
        with open('agenda.csv', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('Nome: {}\nTelefone: {}\nE-mail: {}\nEndereco: {}\n\n'.format(contato, telefone, email, endereco))
        print("Contatos exportados com sucesso.")
    except Exception as error:
        print("Algum erro ocorreu ao exportar contatos")
        print(error)


def importar_contatos(filename):
    try:
        with open(filename, 'r') as arquivo:
            linhas = arquivo.readlines()
            print('\n')
            for linha in linhas:
                print(linha[0:-1])
    except FileNotFoundError:
        print(">>> Arquivo não encontrado")
    except Exception as error:
        print(">>> Erro inesperado ocorreu!")
        print(error)

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print()
        print(">>> Contato {} excluido com sucesso.".format(contato))
        print()
    except KeyError:
        print(">>> Contato inexistente.")
    except Exception as error:
        print(">>> Erro inesperado ocorreu: ")
        print(error)


def mostrar_menu():
    print('---------------------------------')
    print("1 - Mostrar a agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - editar contato")
    print("5 - exluir contato")
    print("6 - Exportar contatos para CSV")
    print("7 - Importar contatos")
    print("0 - Encerrar programa")
    print('---------------------------------')

while True:
    mostrar_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_agenda()
    elif opcao == '2':
        contato = input('Digite o contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            if AGENDA[contato]:
                print(">>> Contato já existente.")
        except:
            incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input('Digite o nome do contato:')
        try:
            if AGENDA[contato]:
                incluir_editar_contato(contato)
        except:
            print(">>> Contato inexistente.")
    elif opcao == '5':
        contato = input('Digite o contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '7':
        filename = input("Digite o nome do arquivo: ")
        importar_contatos(filename)
    elif opcao == '0':
        print('\n>>> Encerrando o programa..')
        print('Até mais')
        break
    else:
        print("Opção inválida!")







