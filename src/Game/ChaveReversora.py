class ChaveReversora:
    def __init__(self, estado= "Neutro"):
        self.estado = estado

    def estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado
