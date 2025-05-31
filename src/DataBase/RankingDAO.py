from DataBase.ConnectionFactory import ConnectionFactory
from models.UserModel import UserModel
from models.Pontuacao import Pontuacao

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
    
    def set_pontuacao(self, pontuacao: Pontuacao):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE pontos SET Pontos = %s WHERE Email = %s", (pontuacao.get_pontos(), pontuacao.get_email()))

        self.connection.commit()
        cursor.close()
        
    def criar_pontuador(self, pontuacao: Pontuacao):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO pontos (Email, Pontos) VALUES (%s, %s)", (pontuacao.get_email(), pontuacao.get_pontos()))

        self.connection.commit()
        cursor.close()