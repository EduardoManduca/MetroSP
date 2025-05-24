from DataBase.ConnectionFactory import ConnectionFactory
from models.UserModel import UserModel

class LoginDAO:
    def login(self, usuario: UserModel) -> bool:

        # Abrir conexão
        conn = ConnectionFactory.getConnection()
        
        # Fazer Requisição
        cursor = conn.cursor()
        email = usuario.getEmail()
        senha = usuario.getSenha()
        cursor.execute(
            "SELECT * FROM usuario WHERE Email = %s AND Senha = %s", (email, senha,)
        )
        
        # Guardar resultado
        row = cursor.fetchone()

        # Fechar conexão
        cursor.close()
        conn.close()
        
        # Retornar resultado
        if row:
            return True
        return False
