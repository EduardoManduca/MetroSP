from DataBase.ConnectionFactory import ConnectionFactory
from models.UserModel import UserModel

class DeleteUserDAO:
    def __init__(self):
        self.connection = ConnectionFactory.getConnection()
    
    def delete_user(self, user: UserModel) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM usuario WHERE email = %s", (user.getEmail(),))
            self.connection.commit()
            cursor.close()
            return True
        
        except Exception as e:
            print(e)
            return False
        