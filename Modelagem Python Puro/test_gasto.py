import unittest
from gasto import Gasto, CategoriaGasto
from should_dsl import should

class TestGasto(unittest.TestCase):

    def test_it_has_atributes(self):
        categoria_gasto = CategoriaGasto(descricao='Bala', peso=10)
        gasto = Gasto('7 Bello', categoria_gasto, 5, 1.80)
        gasto.descricao |should| equal_to("7 Bello")
        gasto.categoria_gasto |should| be(categoria_gasto)
        gasto.quantidade |should| equal_to(5)
        gasto.valor_total |should| equal_to(1.80)

class TestCategoriaGasto(unittest.TestCase):

    def test_it_has_atributes(self):
        categoria_gasto = CategoriaGasto(descricao='Bala', peso=10)
        categoria_gasto.descricao |should| equal_to('Bala')
        categoria_gasto.peso |should| equal_to(10)

if __name__ == "__main__":
   unittest.main()
