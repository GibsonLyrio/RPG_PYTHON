from pydantic import BaseModel, Field
from itens.equipaveis import equipamento
from entities.animals import animals, Animal


# Definindo classe players
class Players(BaseModel):
    name: str
    hp: int = Field(default=0)
    hp_max: int = Field(default=0)
    mana: int = Field(default=0)
    mana_max: int = Field(default=0)
    energia: int = Field(default=0)
    energia_max: int = Field(default=0)
    dano_fisico: int = Field(default=0)
    dano_magico: int = Field(default=0)
    level: int = Field(default=0)
    exp: int = Field(default=0)
    exp_max: int = Field(default=0)
    skills: dict = Field(default_factory=dict)
    skills_points: int = Field(default=0)
    coins: int = Field(default=0)
    inventory: dict = Field(default_factory=dict)
    equipament: list = Field(default=[])
# ----

# Classe de gerenciamento do player
class Player:
    def __init__(self):
        self.name = 'Gibson'
        self.hp = 100
        self.hp_max = 100
        self.mana = 50
        self.mana_max = 50
        self.energia = 50
        self.energia_max = 50
        self.dano_fisico = 5
        self.dano_magico = 5
        self.level = 1
        self.exp = 0
        self.exp_max = 30
        self.skills = self.initialize_skills()
        self.skills_points = 0
        self.coins = 0
        self.inventory = {}
        self.equipament = equipamento.LISTA_EQUIPADOS

    def initialize_skills(self):
        return {
            'destreza': 0,
            'vigor': 0,
            'inteligência': 0,
            'sorte': 0,
            'magias': 0,
            'treinamento': 0,
            'santidade': 0,
            'pele_de_aço': 0,
        }
    
    def calc_dano_fisico(self):
        arma_equipada = [item for item in self.equipament if item['tipo']=='arma'][0]
        if arma_equipada.get('dano') == 'fisico':
            dano_arma = arma_equipada.get('dano_fisico')
            dano = dano_arma * (1 + (self.skills.get('treinamento') / 10))
        else:
            dano = self.dano_fisico * (1 + (self.skills.get('treinamento') / 10))
        return(dano)

    def calc_dano_magico(self):
        arma_equipada = [item for item in self.equipament if item['tipo']=='arma'][0]
        if arma_equipada.get('dano') == 'magico':
            dano_arma = arma_equipada.get('dano_magico')
            dano = dano_arma * (1 + (self.skills.get('magias') / 10))
        else:
            dano = self.dano_magico * (1 + (self.skills.get('magias') / 10))
        return(dano)

    def dar_dano(self):
        arma_equipada = [item for item in self.equipament if item['tipo']=='arma'][0]
        if arma_equipada.get('dano') == 'fisico':
            dano_dado = self.calc_dano_fisico()
            self.energia -= 5
            return dano_dado
        elif arma_equipada.get('dano') == 'magico':
            dano_dado = self.calc_dano_magico()
            self.mana -= 5
            return dano_dado
        
    def tomar_dano(self, dano):
        if self.hp > 0:
            self.hp -= dano
            if self.hp <= 0:
                self.die()
                self.hp = 0

    def die(self):
        print(f'Você morreu!')

    def batalhar_animal(self, target: Animal, ataques):
        for x in range(ataques):
            if player.hp > 0 and target.hp > 0:
                print('Inicio do round ----------')
                animals.tomar_dano(target, dano = player.dar_dano())
                if target.hp <= 0:
                    player.exibir_all()
                    animals.exibir_hp(target)
                    print('Fim do round ----------\n')
                else:
                    player.tomar_dano(dano = animals.dar_dano(target))
                    player.exibir_all()
                    animals.exibir_hp(target)
                    print('Fim do round ----------\n')

    def calc_bar(self, nome, bar_cheia, bar_vazia, max, atual, cor):
        # Confere se algum atributo tem 4 digitos:
        quad_digito = max >= 1000
        # Se tiver, exibe formatado para 4 digitos
        if quad_digito:
            print(f'{cor}{nome:7}\033[m╂{cor}({atual:4}/{max:4}) ', end='')
        # Se não, exibe formatado para 3 digitos
        if not quad_digito:
            print(f'{cor}{nome:7}\033[m╂{cor}({atual:3}/{max:3}) ', end='')
        
        # Cálculos de proporção da barra
        bar_max = int(max / 10)
        bar_atual = int(atual / 10)
        if bar_max <= 50:
            for bar in range(bar_atual):
                print(f'{bar_cheia}', end='')
            for bar in range(bar_max-bar_atual):
                print(f'{bar_vazia}', end='')
            print(end='\033[m\n')
        else:
            bar_max = 50
            bar_atual = int(atual / ((max/100) * 2))
            for bar in range(bar_atual):
                print(f'{bar_cheia}', end='')
            for bar in range(bar_max-bar_atual):
                print(f'{bar_vazia}', end='')
            print(end='\033[m\n')

    def exibir_hp(self):
        self.calc_bar(
            'HP',
            '▮',
            '▯',
            max=self.hp_max,
            atual=self.hp,
            cor='\033[31m'
        )

    def exibir_mana(self):
        self.calc_bar(
            'Mana',
            '▮',
            '▯',
            max=self.mana_max,
            atual=self.mana,
            cor='\033[34m'
        )

    def exibir_energia(self):
        self.calc_bar(
            'Energia',
            '▪',
            '▫',
            max=self.energia_max,
            atual=self.energia,
            cor='\033[33m'
        )

    def exibir_exp(self):
        self.calc_bar(
            'Exp',
            '▪',
            '▫',
            max=self.exp_max,
            atual=self.exp,
            cor='\033[32m'
        )

    def exibir_all(self):
        print('\nPlayer━┓')
        self.exibir_hp()
        self.exibir_mana()
        self.exibir_energia()
        self.exibir_exp()
        print('━━━━━━━┛\n')
# ----
# Criando instancia de player para exportar
player = Player()
# ----

# Testando:
# player.exibir_all()
# ----
