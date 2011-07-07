import unittest
from pessoa import Pessoa
from gasto import Gasto, CategoriaGasto
from should_dsl import should

class TestPessoa(unittest.TestCase):

    def test_it_has_atributes(self):
        pessoa = Pessoa('Aline', 1.800, 15)
        pessoa.nome |should| equal_to('Aline')
        pessoa.salario |should| equal_to(1.800)
        pessoa.dia_de_pagamento |should| equal_to(15)

    def test_it_has_expenses(self):
        categoria_gasto = CategoriaGasto(descricao='Bala e Chiclete', peso=10)
        gasto = Gasto('7 Bello', categoria_gasto, 5, 1.80)
        gasto2 = Gasto('Trident', categoria_gasto, 1, 2.00)
        pessoa = Pessoa('Aline', 1.800, 15)
        
        pessoa.gastos.append(gasto)
        pessoa.gastos.append(gasto2)
        
        pessoa.gastos[0].descricao |should| equal_to('7 Bello')
        pessoa.gastos[1].descricao |should| equal_to('Trident')

    def test_it_generates_daily_report(self):
        categoria_gasto = CategoriaGasto(descricao='Bala e Chiclete', peso=10)
        gasto = Gasto('7 Bello', categoria_gasto, 5, 1.80)
        gasto2 = Gasto('Trident', categoria_gasto, 1, 2.00)
        pessoa = Pessoa('Aline', 1.800, 15)
        
        pessoa.gastos.append(gasto)
        pessoa.gastos.append(gasto2)

        pessoa.emitir_relatorio_diario() should equal_to()

    def test_it_generates_weekly_report(self):
        pass

    def test_it_generates_monthly_report(self):
        pass

if __name__ == "__main__":
   unittest.main()
