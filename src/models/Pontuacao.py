class Pontuacao:
    def __init__(self, email, pontos):
        self.email = email
        self.pontos = pontos
    
    def set_email(self, email):
        self.email = email

    def set_pontos(self, pontos):
        self.pontos = pontos
        
    def get_email(self):
        return self.email
    
    def get_pontos(self):
        return self.pontos
    