from ADU import ADU
from Chave_CBTC import Chave_CBTC
from ChaveReversora import ChaveReversora
from Porta import Porta

class Etapas:
    def __init__(self):
        self.adu = ADU()
        self.chave_cbtc = Chave_CBTC()
        self.chave_reversora = ChaveReversora()
        self.porta = Porta()
        
    def get_adu(self):
        return self.adu.estado

    def get_chave_cbtc(self):
        return self.chave_cbtc.estado

    def get_chave_reversora(self):
        return self.chave_reversora.estado

    def get_porta(self):
        return self.porta.estado

test = Etapas()
print(test.get_adu())
print(test.get_chave_cbtc())
print(test.get_chave_reversora())
print(test.get_porta())