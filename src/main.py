from models.UserModel import UserModel
from DataBase.LoginDAO import LoginDAO

usuario = UserModel("Caio", "123")
uDAO = LoginDAO()
resultado = uDAO.login(usuario)

if resultado:
    print(True)
else:
    print(False)


