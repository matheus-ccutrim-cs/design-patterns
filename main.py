from modelos import Empresa
from antes import PedidoCondicional
from strategy import Pedido, selecionar_politica


class TelaPedido:
    def calcular_antes(self, empresa, valor):
        return PedidoCondicional(valor, empresa).calcular_total()

    def calcular_depois(self, empresa, valor):
        politica = selecionar_politica(empresa.obter_porte())
        return Pedido(valor, politica).calcular_total()


if __name__ == "__main__":
    tela = TelaPedido()
    for porte in ("startup", "pme", "enterprise", "outro"):
        empresa = Empresa("Empresa exemplo", porte)
        antes = tela.calcular_antes(empresa, "5000")
        depois = tela.calcular_depois(empresa, "5000")
        print(f"{porte:10} | antes: R$ {antes:.2f} | Strategy: R$ {depois:.2f}")
