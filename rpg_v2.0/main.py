from entities.player import player
from interfaces.inventory import inventario
from itens.equipaveis import equipamento, Arma
from entities.animals import animals, Lobo, Javali, Urso


# Teste:

arma1 = Arma(
    tipo='arma',
    dano='fisico',
    nome='Varinha torta',
    dano_fisico=20,
    dano_magico=0,
    preco=40,
)

equipamento.criar_arma(arma1)

lobo1 = Lobo(
    tipo='lobo',
    hp=80,
    hp_max=80,
    dano_fisico=30,
    drop='Pele de Lobo'
)
animals.criar_lobo(lobo1)

player.batalhar_animal(lobo1, 1)

# ----
