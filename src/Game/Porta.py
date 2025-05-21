import customtkinter as ctk

class Porta:
    def __init__(self, estado: bool = False):
        self.estado = estado

    def esta_aberta(self) -> bool:
        return self.estado

    def set_porta(self, estado: bool):
        self.estado = estado