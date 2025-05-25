from DataBase.ConnectionFactory import ConnectionFactory
from models.NewUserModel import NewUserModel

class SingUpDAO:
    def __init__(self):
        self.connection = ConnectionFactory.getConnection()

    def create_user(self, user: NewUserModel) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO usuario (email, tipo, senha) VALUES (%s, %s, %s)",(user.get_email(), user.get_tipo(), user.get_senha(),))
            self.connection.commit()
            cursor.close()
            return True
        
        except Exception as e:
            print(e)
            return False

    def get_user(self, email: str) -> NewUserModel:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return NewUserModel(*row)
        return None

    def update_user(self, user: NewUserModel):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET senha = ?, email = ?, tipo = ? WHERE email = ?",
                       (user.get_senha(), user.get_email(), user.get_tipo(), user.get_email()))
        self.connection.commit()
        cursor.close()

    def delete_user(self, email: str):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE email = ?", (email,))
        self.connection.commit()
        cursor.close()
