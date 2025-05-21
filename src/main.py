import customtkinter as ctk
from PIL import Image, ImageTk
from models.UserModel import UserModel
from DataBase.LoginDAO import LoginDAO
from models.Botao import Botao
from Game.Porta import Porta

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


# ================================ Mensagem de erro ===================================
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

# =============================== Mensagem da porta ===================================
def mensagem_porta_aberta():
    mensagem = ctk.CTk()
    mensagem.geometry("300x250")
    mensagem.title("Mensagem")
    mensagem.resizable(False, False)

    # Centralizar a janela na tela
    largura_tela = mensagem.winfo_screenwidth()
    altura_tela = mensagem.winfo_screenheight()
    largura_janela = 300
    altura_janela = 250
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)
    mensagem.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    label_mensagem = ctk.CTkLabel(mensagem, text="Porta já está aberta!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    btn_tentar_novamente = ctk.CTkButton(
        mensagem,
        text="Tentar novamente",
        width=100,
        height=50,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=lambda: mensagem.destroy()
    )
    btn_tentar_novamente.place(relx=0.5, y=200, anchor="center")
    
    mensagem.mainloop()

def mensagem_porta_fechada():
    mensagem = ctk.CTk()
    mensagem.geometry("300x250")
    mensagem.title("Mensagem")
    mensagem.resizable(False, False)

    # Centralizar a janela na tela
    largura_tela = mensagem.winfo_screenwidth()
    altura_tela = mensagem.winfo_screenheight()
    largura_janela = 300
    altura_janela = 250
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)
    mensagem.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    label_mensagem = ctk.CTkLabel(mensagem, text="Porta já está fechada!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    btn_tentar_novamente = ctk.CTkButton(
        mensagem,
        text="Tentar novamente",
        width=100,
        height=50,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=lambda: mensagem.destroy()
    )
    btn_tentar_novamente.place(relx=0.5, y=200, anchor="center")
    
    mensagem.mainloop()

# ================================ Verifica Porta ===================================
def aciona_boteira_porta():
    if porta.esta_aberta():
        return boteira_porta_aberta
    else:
        return boteira_porta_fechada
    
def verifica_porta():
    func = aciona_boteira_porta()
    func()

# ================================ Verifica DDU ===================================
def aciona_ddu():
    if porta.esta_aberta():
        return ddu_portas_abertas
    else:
        return ddu_portas_fechadas
def verifica_ddu():
    func = aciona_ddu()
    func()
# ================================ Tela Login ===================================   
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


# ============================ Tela Simulador =============================

porta = Porta()
porta.set_porta(False)

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
    
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=lambda: print("Seta direita clicada")
    )
    seta_direita.place(x=1230, y=320)

    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_porta
    )
    seta_esquerda.place(x=10, y=320)
    
    botao_adu = ctk.CTkButton(
        app,
        text="ADU",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=ADU
    )
    botao_adu.place(x=560, y=250)
    
    botao_ddu = ctk.CTkButton(
        app,
        text="DDU",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=verifica_ddu
    )
    
    
    botao_ddu.place(x=200, y=270)

def ADU():
    for winget in app.winfo_children():
        winget.destroy()
        
    img_fundo = Image.open("./imgs/Simulacao/ADU.png").resize((1300,700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # imagem_seta_cima = ctk.CTkImage(
    #     light_image=Image.open("./imgs/Simulacao/seta_cima.jpg"),
    #     size=(30, 30)
    # )
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30,30)
    )
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=falhaPorta
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

def ddu_portas_abertas():
    for winget in app.winfo_children():
        winget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/DDU_porta_aberta.jpg").resize((1300,700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=falhaPorta
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

def ddu_portas_fechadas():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/DDU_porta_fechada.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=falhaPorta
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

def boteira_porta_fechada():
    porta.set_porta(False)
    for widget in app.winfo_children():
        widget.destroy()

    # ============ Fundo =============
    img_fundo = Image.open("./imgs/Simulacao/boteira.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ============ Botões =============
    botao_abrir_porta = ctk.CTkButton(
        app,
        text="Abrir Portas",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=boteira_porta_aberta
    )
    botao_abrir_porta.place(x=560, y=300)
    
    botao_fechar_porta = ctk.CTkButton(
        app,
        text="Fechar Portas",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_porta_fechada
    )
    botao_fechar_porta.place(x=600, y=430)

    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30,30)
    )
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=falhaPorta
    )
    seta_direita.place(x=1230, y=320)

# =========================== Boteira Porta Aberta ============================
# Aqui você pode adicionar a lógica para o que acontece quando a porta está aberta
def boteira_porta_aberta():
    porta.set_porta(True)
    for widget in app.winfo_children():
        widget.destroy()

    # ============ Fundo =============
    img_fundo = Image.open("./imgs/Simulacao/boteira_porta_aberta.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ============ Botões =============

    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30,30)
    )
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=falhaPorta
    )
    seta_direita.place(x=1230, y=320)
    
    botao_fechar_porta = ctk.CTkButton(
        app,
        text="Fechar Portas",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=boteira_porta_fechada
    )
    botao_fechar_porta.place(x=600, y=430)

    botao_abrir_porta = ctk.CTkButton(
        app,
        text="Abrir Portas",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_porta_aberta
    )
    botao_abrir_porta.place(x=560, y=300)

main()
app.mainloop()