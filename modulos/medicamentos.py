from datetime import date, datetime
import random 

class Medicamentos:

    def criar_id(self):
        return random.randint(1, 10000)
        
    def __init__(self, nome = '', validade = 0, lote = 0 ):
        self._id = self.criar_id()
        self._nome = nome
        self._validade = datetime.strptime(validade, "%m/%Y").date()
        self._lote = lote

    def status(self):
        dias_pra_vencer = (self._validade - date.today()).days

        if dias_pra_vencer < 0:
            return 'vencido'
        elif dias_pra_vencer > 30:
            return 'nao vencido'
        else:
            return "PDV"
        
 


        