
efetividade = {
    "Fogo":{
        "Planta" : 2.0,
        "Agua" : 0.5
    },
    "Planta":{
        "Agua": 2.0,
        "Fogo": 0.5
    },
    "Agua":{
        "Fogo": 2.0,
        "Planta": 0.5
    }
}

def verifica_efetividade(tipo_atacante, tipo_defesa):

    valor_tipo = efetividade[tipo_atacante][tipo_defesa]

    return valor_tipo