from DataBase.ConnectionFactory import ConnectionFactory
from models.UserModel import UserModel

class RankingDAO:
    def __init__(self):
        self.connection = ConnectionFactory.getConnection()

    def get_ranking(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pontos ORDER BY Pontos DESC")
        
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return result