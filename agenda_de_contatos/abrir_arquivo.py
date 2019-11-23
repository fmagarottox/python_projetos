try:
    with open('nomes.txt', 'w') as arquivo:
        arquivo.write('Filipe Magarotto')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)