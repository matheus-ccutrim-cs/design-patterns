from decimal import Decimal
from modelos import Empresa, validar_valor


class PedidoCondicional:
    def __init__(self, valor, empresa: Empresa):
        self.valor = validar_valor(valor)
        self.empresa = empresa

    def calcular_total(self):
        porte = self.empresa.obter_porte()
        if porte == "startup":
            desconto = self.valor * Decimal("0.10")
        elif porte == "pme":
            desconto = self.valor * Decimal("0.15")
        elif porte == "enterprise":
            desconto = self.valor * Decimal("0.20")
        else:
            desconto = Decimal("0")
        return (self.valor - desconto).quantize(Decimal("0.01"))
