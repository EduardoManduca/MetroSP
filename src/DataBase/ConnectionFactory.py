import mysql.connector

class ConnectionFactory:
    @staticmethod
    def getConnection():
        return mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "senha123",
            database = "BD"
        )
