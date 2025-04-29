class UserModel:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getSenha(self):
        return self.senha
    def setSenha(self, senha):
        self.senha = senha

