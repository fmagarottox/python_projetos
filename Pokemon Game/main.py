from pessoa import *
from pokemon import *

def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nesta jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas:")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("Escolha o seu pokemon: ")
        if escolha == "1":
            player.capturar_pokemon(pikachu)
            break
        elif escolha == "2":
            player.capturar_pokemon(charmander)
            break
        elif escolha == "3":
            player.capturar_pokemon(squirtle)
            break
        else:
            print("Nenhuma opção encontrada!")


player = Player("Filipe")
escolher_pokemon_inicial(player)
player.mostrar_pokemons()
