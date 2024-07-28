from pydantic import BaseModel, Field

# Definindo classe pai ITEM:
class Item(BaseModel):
    nome: str
    quantia: int = Field(default=1)

# Definindo classe de armadura/arma:
class Armadura(Item):
    tipo: str
    defesa_fisica: int = Field(default=0)
    defesa_magica: int = Field(default=0)
    preco: float = Field(default=0)

class Arma(Item):
    tipo: str
    dano: str
    dano_fisico: int = Field(default=0)
    dano_magico: int = Field(default=0)
    preco: float = Field(default=0)
# ----

# Classe de gerenciamento de Equipamentos:
class Equipamentos:
    def __init__(self):
        self.LISTA_EQUIPADOS=[]

    def criar_armadura(self, armadura: Armadura):
        new_armadura = {
            'nome': armadura.nome,
            'quantia': armadura.quantia,
            'tipo': armadura.tipo,
            'defesa_fisica': armadura.defesa_fisica,
            'defesa_magica': armadura.defesa_magica,
            'preco': armadura.preco,
        }
        self.LISTA_EQUIPADOS.append(new_armadura)

    def criar_arma(self, arma: Arma):
        new_arma = {
            'nome': arma.nome,
            'quantia': arma.quantia,
            'tipo': arma.tipo,
            'dano': arma.dano,
            'dano_fisico': arma.dano_fisico,
            'dano_magico': arma.dano_magico,
            'preco': arma.preco,
        }
        self.LISTA_EQUIPADOS.append(new_arma)
# ----

# Iniciando instancias:
equipamento = Equipamentos()
# ----

# # Testes:
# item1 = Armadura(
#     tipo='capacete',
#     nome='Capuz de mago',
#     defesa_fisica=0,
#     defesa_magica=7,
#     preco=36,
# )
# arma1 = Arma(
#     tipo='arma',
#     dano='fisico',
#     nome='Varinha torta',
#     dano_fisico=0,
#     dano_magico=15,
#     preco=40,
# )

# equipamento.criar_armadura(item1)
# equipamento.criar_arma(arma1)

# print(equipamento.LISTA_EQUIPADOS)

# capacete = [item for item in equipamento.LISTA_EQUIPADOS if item['tipo']=='capacete'][0]
# print('')
# print(type(capacete))
# # ----
