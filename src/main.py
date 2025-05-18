import customtkinter as ctk
from PIL import Image, ImageTk
from models.UserModel import UserModel
from DataBase.LoginDAO import LoginDAO
from models.Botao import Botao

# Configuração inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ======================================= Tela Login ======================================= 
LARGURA = 1300
ALTURA = 700

app = ctk.CTk()
app.geometry(f"{LARGURA}x{ALTURA}")
app.title("Simulador Metro SP")
app.resizable(False, False)

# Centralizar janela
largura = app.winfo_screenwidth()
altura = app.winfo_screenheight()

x = (largura // 2) - (LARGURA // 2)
y = (altura // 2) - (ALTURA // 2)

app.geometry(f"{LARGURA}x{ALTURA}+{x}+{y}")

def mensagem():
    popup = ctk.CTk()
    popup.geometry("300x250")
    popup.title("Erro ao Logar")
    popup.resizable(False, False)

    label_mensagem = ctk.CTkLabel(popup, text="Usuario ou senha incorretos!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    btn_tentar_novamente = ctk.CTkButton(
        popup,
        text="Tentar novamente",
        width=100,
        height=50,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=lambda: popup.destroy()
    )
    btn_tentar_novamente.place(relx=0.5, y=200, anchor="center")
    
    popup.mainloop()
    
# Fundo com imagem
def main():
    for winget in app.winfo_children():
        winget.destroy()
    bg_img = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Logo do metrô 
    logo_img = Image.open("./imgs/Logo metro.jpeg").resize((250, 80))
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = ctk.CTkLabel(app, image=logo_photo, text="")
    logo_label.place(relx=0.5, y=150, anchor="center")

    # Label "Login" 
    login_label = ctk.CTkLabel(app, text="Login", font=("Arial", 28, "bold"))
    login_label.place(relx=0.5, y=250, anchor="center")

    # Campo ID 
    entry_id = ctk.CTkEntry(app, width=349, height=53, placeholder_text="ID", corner_radius=10, border_color="#001489",font=("Arial", 14))
    entry_id.place(relx=0.5, y=368, anchor="center")

    # Campo Senha 
    entry_senha = ctk.CTkEntry(app, width=349, height=53, placeholder_text="Senha", corner_radius=10, border_color="#001489",show="*", font=("Arial", 14))
    entry_senha.place(relx=0.5, y=453, anchor="center")

    # Botão Entrar 
    def login():
        print(f"ID: {entry_id.get()}, Senha: {entry_senha.get()}")
        usuario = UserModel(entry_id.get(), entry_senha.get())
        uDAO = LoginDAO()
        resultado = uDAO.login(usuario)
        
        if resultado:
            print(True)
            abrir_menu()
        else:
            print(False)
            mensagem()

    btn_login = ctk.CTkButton(app, text="Entrar", width=349, height=53, corner_radius=10, fg_color="#001489",font=("Arial", 14), command=login)
    btn_login.place(relx=0.5, y=590, anchor="center")

# =============================================================================================

# ============================= Tela Menu =============================
def abrir_menu():
    for winget in app.winfo_children():
        winget.destroy()

    # ======== Fundo =========
    img_fundo = Image.open("./imgs/fundo_menu.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ====== Botões ======
    btn_iniciar = ctk.CTkButton(
        app,
        text="Iniciar",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=abriTreinamento
    )
    btn_iniciar.place(relx=0.5, y=420, anchor="center")

    btn_historico = ctk.CTkButton(
        app,
        text="Histórico",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=lambda: print("Histórico clicado")
    )
    btn_historico.place(relx=0.5, y=508, anchor="center")
    
    btn_sair = ctk.CTkButton(
        app,
        text="Sair",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=main
    )
    btn_sair.place(relx=0.5, y=596, anchor="center")


# ================================ Tipo de Falha ===================================
def abriTreinamento(): 
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo_menu.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    btn_falha_porta = ctk.CTkButton(
        app,
        text="Falha de Porta",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=falhaPorta
    )
    btn_falha_porta.place(relx=0.5, y=420, anchor="center")
    
    btn_voltar = ctk.CTkButton(
        app,
        text="Voltar",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=abrir_menu
    )
    btn_voltar.place(relx=0.5, y=508, anchor="center")

def falhaPorta():
    for winget in app.winfo_children():
        winget.destroy()
    
    # =========== Fundo ==============
    img_fundo = Image.open("./imgs/Simulacao/Painel.jpg").resize((1300,700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ============ Botões =============
    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30,30)
    )
    
    btn_seta_d = Botao(
        app,
        text="",
        image=imagem_seta_direita,
        width=60, height=60
    )
    btn_seta_d.pack(side="right", padx=10, pady=5)
    
    btn_seta_d = Botao(
        app,
        text="",
        image=imagem_seta_esquerda,
        width=60, height=60
    )
    btn_seta_d.pack(side="left", padx=10, pady=5)
    
    acesso_painel = Botao(
        app,
        text="",
        fg_color="yellow",
        width=100, height=50
    )
    acesso_painel.place(relx=0.5, y=420, anchor="center")
    
main()
app.mainloop()