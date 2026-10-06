from pokemons import Pokemon
import random
from efetividades import efetividade, verifica_efetividade

#Criação dos Objetos.
p1 = Pokemon("Charmander", "Fogo", 30, 0, 80)
p2 = Pokemon("Bulbassauro", "Planta", 30, 0, 90)
p3 = Pokemon("Squirtle", "Agua", 30, 0, 60)

escolha = 0

PokeList = {
    1 : p1,
    2 : p2,
    3 : p3
}
#Criando o primeiro Pokemon.
print("Olá, escolha seu Pokemon:")
escolha = int(input(f"\n1- Charmander\n2- Bulbassauro\n3- Squirtle\n"))
while escolha != 1 and escolha != 2 and escolha !=3:
    print(f"Não é possivel processar a escolha {escolha}")
    print("Por favor, escolha seu Pokemon:")
    escolha = int(input(f"\n1- Charmander\n2- Bulbassauro\n3- Squirtle\n"))

print(f"Você escolheu {PokeList[escolha].nome} do tipo {PokeList[escolha].tipo}")
idr, pokerival = random.choice(list(PokeList.items()))

while idr == escolha:
    idr, pokerival = random.choice(list(PokeList.items()))

print(f"O pokemon rival é: {pokerival.nome} do tipo {pokerival.tipo}")
##Define os pokemons e os chama por nomes que serão encontrados na função de batalhar.
pokemon_player = PokeList[escolha]
pokemon_rival = pokerival

#Definindo os tipos dos Pokemons.
tipo_rival = pokerival.tipo
tipo_player = PokeList[escolha].tipo

valor_player = verifica_efetividade(tipo_player, tipo_rival)
valor_rival = verifica_efetividade(tipo_rival, tipo_player)

if valor_player > valor_rival:
    print(f"Seu {PokeList[escolha].nome} é super efetivo!")
elif valor_player < valor_rival:
    print(f"Seu {PokeList[escolha].nome} não é efetivo.")
else:
    print("Não existe efetividade nessa luta!")

print("==============Battle==============")
cont = 1

while cont == 1 :
        if pokerival.speed > PokeList[escolha].speed:
                print(f"o {pokerival.nome} do rival ataca primeiro.")
                dano_rival = pokerival.ataque(valor_rival)
                print(f"{PokeList[escolha].nome} recebeu {dano_rival}")
                PokeList[escolha].tomar_dano(pokerival.dano)
                print(f"Sua vida atual: {PokeList[escolha].vida}")
                print("Sua vez.")
                dano_player = PokeList[escolha].ataque(valor_player)
                print(f"{pokerival.nome} recebeu {dano_player}!")
                pokerival.tomar_dano(PokeList[escolha].dano)
                cont = int(input("Deseja continuar? 1. Sim / 2.Nâo"))
                if PokeList[escolha].vida <= 0:
                    cont = 2
                elif pokerival.vida <= 0:
                    cont = 2
        else:
                print(f"{PokeList[escolha].nome} ataca primeiro.")
                dano_player = PokeList[escolha].ataque(valor_player)
                print(f"{pokerival.nome} recebeu {dano_player}")
                pokerival.tomar_dano(dano_player)
                print("Vez do Rival")
                dano_rival = pokerival.ataque(valor_rival)
                print(f"{PokeList[escolha].nome} recebeu {dano_rival}")
                PokeList[escolha].tomar_dano(dano_rival)
                print(f"Sua vida atual: {PokeList[escolha].vida}")
                cont = int(input("Deseja continuar? 1. Sim / 2.Nâo"))
                if PokeList[escolha].vida <= 0:
                    cont = 2
                elif pokerival.vida <= 0:
                    cont = 2

if PokeList[escolha].vida <= 0:
    print("Rival venceu!")
else:
    print("Você venceu!")
