class Equipamentos:
    def __init__ (self, estado=True):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado
