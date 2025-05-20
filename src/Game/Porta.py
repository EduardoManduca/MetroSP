class Porta:
    def __init__(self, estado: bool = False):
        self.estado = estado

    def abrir(self):
        self.estado = True

    def fechar(self):
        self.estado = False

    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado

