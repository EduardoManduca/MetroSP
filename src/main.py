from models.UserModel import UserModel
from DataBase.LoginDAO import LoginDAO

usuario = UserModel("Caio", 123)
uDAO = LoginDAO()
uDAO.login(usuario)

if uDAO:
    print(True)
else:
    print(False)


