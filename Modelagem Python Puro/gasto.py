class Gasto(object):
    def __init__(self, descricao, categoria_gasto, quantidade, valor_total, fixo=False):
        self.descricao = descricao
        self.categoria_gasto = categoria_gasto
        self.quantidade = quantidade
        self.valor_total = valor_total

class CategoriaGasto(object):
    def __init__(self, descricao, peso):
        self.descricao = descricao
        self.peso = peso
