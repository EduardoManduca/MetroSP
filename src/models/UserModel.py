class UserModel:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.nome = email
    
    def getSenha(self):
        return self.senha
    def setSenha(self, senha):
        self.senha = senha

