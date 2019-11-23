class Pokemon:
    def __init__(self, especie, tipo, level=1, nome=None):
        self.especie = especie
        self.tipo = tipo
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return

    def atacar(self, pokemon):
        print("{} Atacou {}".format(self.especie, pokemon.especie))


meu_pokemon = Pokemon("fogo", "charmander", level=50, nome="Filipinho")