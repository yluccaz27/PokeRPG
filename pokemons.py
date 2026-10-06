import random
import efetividades

class Pokemon:
    def __init__(self, nome, tipo, vida, dano, speed):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.dano = dano
        self.speed = speed

    def ataque(self, valor_tipo):
        dano = random.randint(1, 4)
        crit = random.randint(1,2)
        dano *= valor_tipo
        if crit==1:
            dano*=2
            print("Critou!")
        return dano

    def tomar_dano(self, dano):
        self.vida -= dano

        return self.vida


class Batalha:
    def __init__(self, pokemon_player, pokemon_rival):
        self.pokemon_player = pokemon_player
        self.pokemon_rival = pokemon_rival

    def batalhar(self):
        pokemon_rival = self.pokemon_rival
        pokemon_player = self.pokemon_player

        if pokemon_rival.speed > pokemon_player.speed:
            print("Rival primeiro.")
            valor_tipo = efetividades.verifica_efetividade(pokemon_rival.tipo, pokemon_player.tipo)
            dano_rival = pokemon_rival.atacar(valor_tipo)
            pokemon_player.tomar_dano(dano_rival)


        elif pokemon_player.speed > pokemon_rival.speed:
            print("Oce primeiro fi.")
            valor_tipo = efetividades.verifica_efetividade(pokemon_player.tipo, pokemon_rival.tipo)
            dano_player = pokemon_player.atacar(valor_tipo)
            pokemon_rival.tomar_dano(dano_player)


        else:
            print("Os dois tem a mesma velocidade, sorteando quem vai primeiro...\n")
            sorteado = random.randint(1,2)
            if sorteado == 1:
                print("player vai primeiro")
                valor_tipo = efetividades.verifica_efetividade(pokemon_player.tipo, pokemon_rival.tipo)
                dano_player = pokemon_player.atacar(valor_tipo)
                pokemon_rival.tomar_dano(dano_player)
            else:
                print("Rival vai primeiro.")
                valor_tipo = efetividades.verifica_efetividade(pokemon_rival.tipo, pokemon_player.tipo)
                dano_rival = pokemon_rival.atacar(valor_tipo)
                pokemon_player.tomar_dano(dano_rival)

