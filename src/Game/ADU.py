class ADU:
    def __init__(self):
        self.estado = "desativada"

    def ativar(self):
        self.estado = "ativada"

    def desativar(self):
        self.estado = "desativada"

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
