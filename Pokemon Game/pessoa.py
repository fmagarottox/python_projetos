from pokemon import *
import random

NOMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
             "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilon"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp")
]

class Pessoa:

    LISTA = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
             "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
    ]

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemon(s) de {}: ".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("Você não tem nenhum pokemon. ")


class Player(Pessoa):
    tipo = "player"

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):

        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))


        super().__init__(nome=nome, pokemons=pokemons)






