from abc import ABC, abstractmethod
from decimal import Decimal
from modelos import validar_valor


class PoliticaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: Decimal) -> Decimal:
        """Retorna o valor do desconto, não o total do pedido."""


class DescontoStartup(PoliticaDesconto):
    def calcular(self, valor):
        return valor * Decimal("0.10")


class DescontoPme(PoliticaDesconto):
    def calcular(self, valor):
        return valor * Decimal("0.15")


class DescontoEnterprise(PoliticaDesconto):
    def calcular(self, valor):
        return valor * Decimal("0.20")


class SemDesconto(PoliticaDesconto):
    def calcular(self, valor):
        return Decimal("0")


def selecionar_politica(porte):
    politicas = {
        "startup": DescontoStartup,
        "pme": DescontoPme,
        "enterprise": DescontoEnterprise,
    }
    return politicas.get(porte.strip().lower(), SemDesconto)()


class Pedido:
    def __init__(self, valor, politica: PoliticaDesconto):
        self.valor = validar_valor(valor)
        self.politica = politica

    def calcular_total(self):
        desconto = self.politica.calcular(self.valor)
        return (self.valor - desconto).quantize(Decimal("0.01"))
