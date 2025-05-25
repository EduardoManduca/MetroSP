class UserModel:
    def __init__(self, email=None, senha=None):
        self.email = email
        self.senha = senha
    
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getSenha(self):
        return self.senha
    def setSenha(self, senha):
        self.senha = senha

