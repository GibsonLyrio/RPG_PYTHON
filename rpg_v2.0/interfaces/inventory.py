from itens.equipaveis import Item

# Lógica do inventário
class Inventario:
    def __init__(self):
        self.SLOTS = []
        self.slots_max = 5
        self.add_successful = None

    def add_item(self, item: Item):
        # Ciclo de busca se o item já está no inventário
        nome = item.get('nome')
        quantia = item.get('quantia')
        encontrado = False
        
        # ADICIONA quantia do item
        for slot in self.SLOTS:
            if slot['nome'] == nome:
                slot['quantia'] += quantia
                encontrado = True
                break

        # ADICIONA item caso tenha espaço
        if not encontrado:
            if len(self.SLOTS) < self.slots_max:
                self.SLOTS.append({'nome': nome, 'quantia': quantia})
                self.add_successful = True
            else:
                print('Inventário cheio')
                self.add_successful = False

    def sub_item(self, item: Item):
        # Ciclo de busca se o item já está no inventário
        nome = item.get('nome')
        quantia = item.get('quantia')
        encontrado = False
        
        for slot in self.SLOTS:
            if slot['nome'] == nome:
                slot['quantia'] -= quantia
                if slot['quantia'] <= 0:
                    self.SLOTS.remove(slot)
                encontrado = True
                break

        if not encontrado:
            print(f'O item "{nome}" não foi encontrado no seu invetário')
    
    def exibir_inventario(self):
        n = 1

        print(f'\n╭―――――――――――――――――――――――――――╮')
        print(f'│ Inventário atual: ({len(self.SLOTS):2}/{self.slots_max:2}) │')
        print(f'╰――╥―――――――――――――――――――――╥――╯')

        print(f'╭――╨―――――――――――――――――――――╨―――――――――――――――――――――――╮')
        for item in self.SLOTS:
            print(f'│ {n}° -> item: {item.get('nome'):20} | quantia: {item.get('quantia'):2} │')
            n += 1
        print('╰――――――――――――――――――――――――――――――――――――――――――――――――╯\n')
# ----

inventario = Inventario()

# # Teste:
# item1 = {
#     'nome': 'Água',
#     'quantia': 1
# }
# item2 = {
#     'nome': 'Poção de mana',
#     'quantia': 9
# }
# print(f'\nInvetário inicial: {inventario.SLOTS}\n')

# inventario.add_item(item1)  # adicionando 1 agua pela primeira vez
# inventario.add_item(item1)  # adicionando +1 agua
# inventario.add_item(item1)  # adicionando +1 agua
# inventario.add_item(item2)  # adicionando 1 pocao de mana pela primeira vez

# inventario.exibir_inventario()

# inventario.sub_item(item1)  # REMOVENDO 1 agua pela primeira vez
# inventario.sub_item(item1)  # REMOVENDO 1 agua
# inventario.sub_item(item1)  # REMOVENDO 1 agua -> deverá ser exlcuído
# inventario.sub_item(item1)  # REMOVENDO 1 agua -> deverá retornar que não encontrou

# inventario.exibir_inventario()
# # ----
