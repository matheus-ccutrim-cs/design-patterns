from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Empresa:
    nome: str
    porte: str

    def obter_porte(self):
        return self.porte.strip().lower()


def validar_valor(valor):
    valor = Decimal(str(valor))
    if not valor.is_finite() or valor < 0:
        raise ValueError("O valor deve ser finito e não negativo.")
    return valor
