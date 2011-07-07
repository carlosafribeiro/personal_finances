class Pessoa(object):
    def __init__(self, nome, salario, dia_de_pagamento):
        self.nome = nome
        self.salario = salario
        self.dia_de_pagamento = dia_de_pagamento
        self.gastos_dia = []
        self.gastos_semana = []
        self.gastos_mes = []

    def emitir_relatorio_diario(self):
        pass

    def emitir_relatorio_semanal(self):
        pass

    def emitir_relatorio_mensal(self):
        pass
