class PainelExterno:
    def __init__(self, isolamento: bool = False):
        self.isolamento = isolamento
        
    def get_estado(self) -> bool:
        return self.isolamento
    
    def set_estado(self, estado: bool):
        self.isolamento = estado