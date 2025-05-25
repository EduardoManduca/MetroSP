class NewUserModel:
    def __init__ (self, email, tipo, senha):
        self.email = email
        self.tipo = tipo
        self.senha = senha
    
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email

    def get_tipo(self):
        return self.tipo
    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_senha(self):
        return self.senha
    def set_senha(self, senha):
        self.senha = senha