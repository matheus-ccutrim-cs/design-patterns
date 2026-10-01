import unittest
from decimal import Decimal
from modelos import Empresa
from main import TelaPedido
from strategy import Pedido, DescontoPme


class TestDescontos(unittest.TestCase):
    def test_resultados_e_equivalencia(self):
        tela = TelaPedido()
        esperados = {"startup": "4500.00", "pme": "4250.00",
                     "enterprise": "4000.00", "outro": "5000.00"}
        for porte, esperado in esperados.items():
            with self.subTest(porte=porte):
                empresa = Empresa("Teste", porte)
                self.assertEqual(tela.calcular_antes(empresa, 5000), Decimal(esperado))
                self.assertEqual(tela.calcular_depois(empresa, 5000), Decimal(esperado))

    def test_zero_e_normalizacao(self):
        tela = TelaPedido()
        empresa = Empresa("Teste", " PME ")
        self.assertEqual(tela.calcular_depois(empresa, 100), Decimal("85.00"))
        self.assertEqual(tela.calcular_depois(empresa, 0), Decimal("0.00"))

    def test_valor_invalido(self):
        for valor in (-1, "NaN", "Infinity"):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                Pedido(valor, DescontoPme())


if __name__ == "__main__":
    unittest.main()
