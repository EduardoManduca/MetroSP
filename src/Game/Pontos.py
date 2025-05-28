class Pontos:
    def __init__(self):
        self.pontos = 0

    def add_pontos(self, pontos):
        self.pontos += pontos
    def sub_pontos(self, pontos):
        self.pontos -= pontos
    
    def get_pontos(self):
        return self.pontos
    def set_pontos(self,pontos):
        self.pontos = pontos