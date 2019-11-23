class Pokemon:
    def __init__(self, tipo, especie):
        self.elemento = tipo
        self.nome = especie
    def __str__(self):
        return "{} ({})".format(self.nome, self.elemento)

meu_pokemon = Pokemon("Fogo", "Charmander")
pokemon_amigo = Pokemon("Raio", "Pikachu")

print(meu_pokemon)
print(pokemon_amigo)

# while True:
#     duvida = input("Digite o que quer saber: ")
#     if duvida == "elemento":
#         print(meu_pokemon.elemento)
#     elif duvida == "nome":
#         print(meu_pokemon.nome)
#     else:
#         print("Atributo não encontrado!")