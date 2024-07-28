from pydantic import BaseModel

# Definindo as classes de dados:
class Animal (BaseModel):
    tipo: str
    hp: int
    hp_max: int
    dano_fisico: int
    drop: str

class Lobo(Animal):
    pass
class Javali(Animal):
    pass
class Urso(Animal):
    pass
# ----

# classe de gerenciamento de coleções:
class Animals:
    def __init__(self):
        self.LISTA_ALL_ANIMALS=[]
        self.LISTA_ALL_LOBO=[]
        self.LISTA_ALL_JAVALI=[]
        self.LISTA_ALL_URSO=[]

    def criar_lobo(self, lobo: Lobo):
        if not isinstance(lobo, Lobo):
            raise TypeError(f'Esperado um objeto do tipo Lobo, mas recebeu{type(lobo)}')
        self.LISTA_ALL_LOBO.append(lobo)
        self.LISTA_ALL_ANIMALS.append(lobo)
        return True

    def criar_javali(self, javali: Javali):
        if not isinstance(javali, Javali):
            raise TypeError(f'Esperado um objeto do tipo Javali, mas recebeu{type(javali)}')
        self.LISTA_ALL_JAVALI.append(javali)
        self.LISTA_ALL_ANIMALS.append(javali)
        return True

    def criar_urso(self, urso: Urso):
        if not isinstance(urso, Urso):
            raise TypeError(f'Esperado um objeto do tipo Urso, mas recebeu{type(urso)}')
        self.LISTA_ALL_URSO.append(urso)
        self.LISTA_ALL_ANIMALS.append(urso)
        return True
    
    def tomar_dano(self, target: Animal, dano):
        target.hp -= dano
        if target.hp <= 0:
            self.die(target)
            target.hp = 0

    def die(self, target: Animal):
        print(f'O {target.tipo} foi derrotado e dropou {target.drop}')

    def dar_dano(self, atacante: Animal):
        return atacante.dano_fisico
    
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

    def exibir_hp(self, target: Animal):
        if target.tipo == 'lobo':
            print(f'\nLobo━━━┓')
        if target.tipo == 'javali':
            print(f'\nJavali━┓')
        if target.tipo == 'urso':
            print(f'\nUrso━━━┓')
        self.calc_bar(
            'HP',
            '▮',
            '▯',
            max=target.hp_max,
            atual=target.hp,
            cor='\033[31m'
        )
        print('━━━━━━━┛\n')
# ----

# Criando instancia da classe:
animals = Animals()
# ----

# Testes:
# lobo1 = Lobo(
#     tipo='lobo',
#     hp=100,
#     hp_max=200,
#     dano_fisico=15,
#     drop='Pele de Lobo'
# )

# print(lobo1)
# animals.criar_lobo(lobo1)
# print(animals.LISTA_ALL_ANIMALS)

# animals.exibir_hp(lobo1)
# ----
