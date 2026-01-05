from datetime import date, datetime

class Medicamentos:

    def __init__(self, id = 0, nome = '', validade = 0, lote = 0 ):
        self._id = id
        self._nome = nome
        self._validade = datetime.strptime(validade, "%d/%m/%Y").date()
        self._lote = lote

def esta_vencido(self, _validade):
    dia = int(_validade[0:2])
    mes= int(_validade[3:5])
    ano = int(_validade[6:10])

    dia_atual = date.today().day
    mes_atual = date.today().month
    ano_atual = date.today().year

    if ano < ano_atual or (ano == ano_atual and mes < mes_atual) or (ano == ano_atual and mes == mes_atual and dia < dia_atual):
        return True
        



        