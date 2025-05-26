class PortaLacrada:
    def __init__(self, estado: bool = False):
        self.estado = estado
        
    def get_estado(self) -> bool:
        return self.estado
    
    def set_estado(self, estado: bool):
        self.estado = estado

