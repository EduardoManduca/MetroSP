import customtkinter as ctk
from PIL import Image, ImageTk
from DataBase.SingUpDAO import SingUpDAO
from models.NewUserModel import NewUserModel
from models.UserModel import UserModel
from models.Pontuacao import Pontuacao
from DataBase.LoginDAO import LoginDAO
from DataBase.DeleteUserDAO import DeleteUserDAO
from DataBase.RankingDAO import RankingDAO
from Game.ChaveServico import ChaveServico
from Game.Porta import Porta
from Game.ChaveReversora import ChaveReversora
from Game.Chave_CBTC import Chave_CBTC
from Game.PainelExterno import PainelExterno
from Game.PortaFalha import PortaFalha
from Game.PortaLacrada import PortaLacrada
from Game.Equipamentos import Equipamentos
from Game.Pontos import Pontos
from Game.Tela import Tela
from Game.PAComunicado import PAComunicado
from Game.CCOComunicado import CCOComunicado

# Configuração inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
ponto = Pontos()
rDAO = RankingDAO()
email_usuario = Pontuacao("email", 0)  # Inicializa com um email fictício e 0 pontos
cont1 = 0
cont2 = 0
cont3 = 0


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

cco = CCOComunicado()
def mensagem_cco():
    cco.set_estado(True)
    
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
    
    # Centralizar os dois labels verticalmente na janela
    label_mensagem1 = ctk.CTkLabel(mensagem, text="CCO Informado!", font=('Arial', 20, "bold"))
    label_mensagem2 = ctk.CTkLabel(mensagem, text="Permissão para verificar falha", font=('Arial', 20, "bold"))

    # Calcula a posição y para centralizar os dois labels juntos
    altura_total_labels = 40 + 40 + 10  # altura dos dois labels + espaçamento
    y_inicio = (250 - altura_total_labels) // 2

    label_mensagem1.place(relx=0.5, y=y_inicio + 20, anchor="center")
    label_mensagem2.place(relx=0.5, y=y_inicio + 70, anchor="center")
    
    mensagem.after(3000, mensagem.destroy)
    
    mensagem.mainloop()

def mensagem_isolamento_errado():
    ponto.sub_pontos(3)
    
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
    
    label_mensagem = ctk.CTkLabel(mensagem, text="Porta errada!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    mensagem.after(3000, mensagem.destroy)
    
    mensagem.mainloop()

def mensagem_isolamento_correto():
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
    
    label_mensagem1 = ctk.CTkLabel(mensagem, text="Porta correta!", font=('Arial', 20, "bold"))
    label_mensagem2 = ctk.CTkLabel(mensagem, text="Porta isolada!", font=('Arial', 20, "bold"))
    label_mensagem1.place(relx=0.5, y=150, anchor="center")
    label_mensagem2.place(relx=0.5, y=180, anchor="center")

    mensagem.after(3000, mensagem.destroy)

    mensagem.mainloop()

def mensagem_erro_cadastro():
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
    
    label_mensagem = ctk.CTkLabel(mensagem, text="Erro!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    mensagem.after(3000, mensagem.destroy)
    
    mensagem.mainloop()
    
def mensagem_sucesso_cadastro():
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
    
    label_mensagem = ctk.CTkLabel(mensagem, text="Sucesso!", font=('Arial', 20, "bold"))
    label_mensagem.place(relx=0.5, y=150, anchor="center")
    
    mensagem.after(3000, mensagem.destroy)
    
    mensagem.mainloop()

# ================================ Verifica Porta ===================================
porta = Porta()
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
    
# ================================ Verifica Chave Reversora ===================================
chave = ChaveReversora()

def aciona_chave_reversora():
    if chave.estado == "Neutro":
        return chave_reversora_neutro
    elif chave.estado == "Frente":
        return chave_reversora_frente
    else:
        return chave_reversora_neutro

def verifica_chave_reversora():
    func = aciona_chave_reversora()
    func()
    
# ================================ Verifica Chave CBTC ===================================
chave_cbtc = Chave_CBTC()
def aciona_chave_cbtc():
    if chave_cbtc.estado == "AM":
        return chave_cbtc_am
    elif chave_cbtc.estado == "MCS":
        return chave_cbtc_mcs
    elif chave_cbtc.estado == "RM":
        return chave_cbtc_rm
def verifica_chave_cbtc():
    func = aciona_chave_cbtc()
    func()

# =============================== Verifica Painel externo ===================================
obj_painel = PainelExterno()

def aciona_painel_externo():
    if not obj_painel.get_estado():
        return painel_externo_aberto
    else:
        return painel_externo_aberto_porta_isolada
        ponto.add_pontos(1)

def verifica_painel_externo():
    func = aciona_painel_externo()
    func()
    
# =============================== Verifica porta falha fechada ===================================

obj_porta_falha = PortaFalha()
def aciona_porta_falha():
    if obj_porta_falha.get_estado():
        return porta_falha
    else:
        return porta_falha_fechada

def verifica_porta_falha():
    func = aciona_porta_falha()
    func()

# ================================ Verifica porta lacrada ===================================

obj_porta_lacrada = PortaLacrada()
def aciona_porta_lacrada():
    if obj_porta_lacrada.get_estado():
        return lado_fora_porta_lacrada
    else:
        return lado_fora

def verifica_porta_lacrada():
    func = aciona_porta_lacrada()
    func()

# =============================== Verifica luz Porta Lacrada ===================================

luz_porta_lacrada = PortaLacrada()
def aciona_luz_porta_lacrada():
    if luz_porta_lacrada.get_estado():
        return boteira_porta_fechada
    else:
        return boteira_porta_aberta
    
def verifica_luz_porta_lacrada():
    func = aciona_luz_porta_lacrada()
    func()

# =============================== Verifica chave de servico ===================================

chave_servico = ChaveServico()
def aciona_chave_servico():
    if chave_servico.get_estado():
        return painel_direita
    else:
        return painel_direita_sem_chave

def verifica_chave_servico():
    func = aciona_chave_servico()
    func()

# ===============================  Verifica equipamentos ===================================

obj_equipamentos = Equipamentos()
def aciona_equipamentos():
    if obj_equipamentos.get_estado():
        return equipamentos
    else:
        return equipamentos_pegos

def verifica_equipamentos():
    func = aciona_equipamentos()
    func()

# ================================ PA ===================================
estadoPA = PAComunicado()

# ================================ Pontuação ===================================



def reversora_cbtc():
    if chave.estado == "Frente" and chave_cbtc.estado == "RM":
        ponto.add_pontos(1)
    if chave.estado == "Frente" and chave_cbtc.estado == "AM":
        ponto.sub_pontos(2)
    if chave.estado == "Ré":
        ponto.sub_pontos(3)

def voltar_reversora():
    if chave.estado == "Neutro" and chave_cbtc.estado == "RM":
        ponto.add_pontos(1)
    else:
        ponto.sub_pontos(1)

def ponto_pa():
    if estadoPA.get_estado():
        ponto.add_pontos(1)
        
def ponto_porta():
    if not porta.esta_aberta():
        ponto.add_pontos(2)

def ponto_cco():
    if cco.get_estado():
        ponto.add_pontos(1)
    if estadoPA.get_estado():
        ponto.add_pontos(1)

def ponto_equipamento():
    if obj_equipamentos.get_estado():
        ponto.add_pontos(2)
    if chave_servico.get_estado():
        ponto.add_pontos(2)
    ponto.add_pontos(1)

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
            tipo_usuario = uDAO.verifica_tipo_usuario(usuario.getEmail())
            if tipo_usuario == "supervisor":
                tela_supervisor()
            elif tipo_usuario == "maquinista":
                global email_usuario
                email_usuario.setEmail(usuario.getEmail())
                abrir_menu()

            else:
                mensagem()
        else:
            print(False)
            mensagem()

    btn_login = ctk.CTkButton(app, text="Entrar", width=349, height=53, corner_radius=10, fg_color="#001489",font=("Arial", 14), command=login)
    btn_login.place(relx=0.5, y=590, anchor="center")

def tela_supervisor():
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo_menu.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # ====== Botões ======
    
    # Botão para sair no canto inferior esquerdo
    

    btn_ranking = ctk.CTkButton(
        app,
        text="Ranking",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=tela_ranking
    )
    btn_ranking.place(relx=0.5, y=400, anchor="center")
    
    btn_adicionar_maquinista = ctk.CTkButton(
        app,
        text="Adicionar Maquinista",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=tela_adicionar_maquinista
    )
    btn_adicionar_maquinista.place(relx=0.5, y=484, anchor="center")

    btn_remover_maquinista = ctk.CTkButton(
        app,
        text="Remover Maquinista",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=tela_remover_maquinista
    )
    btn_remover_maquinista.place(relx=0.5, y=576, anchor="center")

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
    btn_sair.place(relx=0.5, y=664, anchor="center")
    
def tela_ranking():
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # ====== Tabela de Ranking ======
    # Frame da tabela de ranking (aumentado)
    tabela_ranking = ctk.CTkFrame(app, width=800, height=400, corner_radius=15, fg_color="#f5f6fa")
    tabela_ranking.place(relx=0.5, y=350, anchor="center")

    # Cabeçalho estilizado
    cabecalho = ctk.CTkLabel(
        tabela_ranking,
        text="Ranking",
        font=("Arial", 30, "bold"),
        text_color="#001489"
    )
    cabecalho.pack(pady=(30, 15))

    # Cabeçalho das colunas
    header_frame = ctk.CTkFrame(tabela_ranking, fg_color="transparent")
    header_frame.pack(fill="x", padx=50)
    ctk.CTkLabel(header_frame, text="Posição", font=("Arial", 20, "bold"), width=100, anchor="w").grid(row=0, column=0)
    ctk.CTkLabel(header_frame, text="Usuário", font=("Arial", 20, "bold"), width=350, anchor="w").grid(row=0, column=1)
    ctk.CTkLabel(header_frame, text="Pontuação", font=("Arial", 20, "bold"), width=150, anchor="w").grid(row=0, column=2)

    # Dados fictícios para exemplo
    
    dados = rDAO.get_ranking()  # Espera-se que retorne uma lista de dicionários com "usuario" e "pontuacao"

    # Linhas da tabela
    for i, dado in enumerate(dados):
        cor_fundo = "#eaf0fb" if i % 2 == 0 else "#f5f6fa"
        linha = ctk.CTkFrame(tabela_ranking, fg_color=cor_fundo)
        linha.pack(fill="x", padx=50, pady=3)
        posicao = f"{i+1}º"
        ctk.CTkLabel(linha, text=posicao, font=("Arial", 18), width=100, anchor="w").grid(row=0, column=0)
        ctk.CTkLabel(linha, text=dado["Email"], font=("Arial", 18), width=350, anchor="w").grid(row=0, column=1)
        ctk.CTkLabel(linha, text=f'{dado["Pontos"]} pontos', font=("Arial", 18), width=150, anchor="w").grid(row=0, column=2)

    # ====== Botões ======
    botao_sair = ctk.CTkButton(
        app,
        text="Sair",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=tela_supervisor
    )
    botao_sair.place(relx=0.5, y=596, anchor="center")

def tela_ranking_maquinista():
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # ====== Tabela de Ranking ======
    # Frame da tabela de ranking (aumentado)
    tabela_ranking = ctk.CTkFrame(app, width=800, height=400, corner_radius=15, fg_color="#f5f6fa")
    tabela_ranking.place(relx=0.5, y=350, anchor="center")

    # Cabeçalho estilizado
    cabecalho = ctk.CTkLabel(
        tabela_ranking,
        text="Ranking",
        font=("Arial", 30, "bold"),
        text_color="#001489"
    )
    cabecalho.pack(pady=(30, 15))

    # Cabeçalho das colunas
    header_frame = ctk.CTkFrame(tabela_ranking, fg_color="transparent")
    header_frame.pack(fill="x", padx=50)
    ctk.CTkLabel(header_frame, text="Posição", font=("Arial", 20, "bold"), width=100, anchor="w").grid(row=0, column=0)
    ctk.CTkLabel(header_frame, text="Usuário", font=("Arial", 20, "bold"), width=350, anchor="w").grid(row=0, column=1)
    ctk.CTkLabel(header_frame, text="Pontuação", font=("Arial", 20, "bold"), width=150, anchor="w").grid(row=0, column=2)

    # Dados fictícios para exemplo
    global rDAO
    dados = rDAO.get_ranking()  # Espera-se que retorne uma lista de dicionários com "usuario" e "pontuacao"

    # Linhas da tabela
    for i, dado in enumerate(dados):
        cor_fundo = "#eaf0fb" if i % 2 == 0 else "#f5f6fa"
        linha = ctk.CTkFrame(tabela_ranking, fg_color=cor_fundo)
        linha.pack(fill="x", padx=50, pady=3)
        posicao = f"{i+1}º"
        ctk.CTkLabel(linha, text=posicao, font=("Arial", 18), width=100, anchor="w").grid(row=0, column=0)
        ctk.CTkLabel(linha, text=dado["Email"], font=("Arial", 18), width=350, anchor="w").grid(row=0, column=1)
        ctk.CTkLabel(linha, text=f'{dado["Pontos"]} pontos', font=("Arial", 18), width=150, anchor="w").grid(row=0, column=2)

    # ====== Botões ======
    botao_sair = ctk.CTkButton(
        app,
        text="Sair",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=abrir_menu
    )
    botao_sair.place(relx=0.5, y=596, anchor="center")

# ================================ Tela Adicionar Maquinista ===================================
def tela_adicionar_maquinista():
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Campo Email
    entry_email = ctk.CTkEntry(app, width=349, height=53, placeholder_text="Email", corner_radius=10, border_color="#001489",font=("Arial", 14))
    entry_email.place(relx=0.5, y=168, anchor="center")
    
    # Campo Tipo
    entry_tipo = ctk.CTkEntry(app, width=349, height=53, placeholder_text="Tipo", corner_radius=10, border_color="#001489",font=("Arial", 14))
    entry_tipo.place(relx=0.5, y=253, anchor="center")
    
    # Campo Senha
    entry_senha = ctk.CTkEntry(app, width=349, height=53, placeholder_text="Senha", corner_radius=10, border_color="#001489",show="*", font=("Arial", 14))
    entry_senha.place(relx=0.5, y=338, anchor="center")
    
    # =========== Botões =============
    
    def cria_usuario():
        user = NewUserModel(entry_email.get(), entry_tipo.get(), entry_senha.get())
        uDAO = SingUpDAO()
        resultado = uDAO.create_user(user)

        if resultado:
            mensagem_sucesso_cadastro()
        else:
            mensagem_erro_cadastro()
    
    btn_adicionar = ctk.CTkButton(
        app,
        text="Adicionar Maquinista",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=cria_usuario
    )
    btn_adicionar.place(relx=0.5, y=450, anchor="center")
    


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
        command=tela_supervisor
    )
    btn_sair.place(relx=0.5, y=550, anchor="center")

    
def tela_remover_maquinista():
    for winget in app.winfo_children():
        winget.destroy()
    
    # ============ Fundo =============
    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Campo email
    entry_email = ctk.CTkEntry(app, width=349, height=53, placeholder_text="Email", corner_radius=10, border_color="#001489",font=("Arial", 14))
    entry_email.place(relx=0.5, y=168, anchor="center")
    
    def deletar():
        usuario = UserModel(entry_email.get(), "")
        uDAO = DeleteUserDAO()
        resultado = uDAO.delete_user(usuario)

        if resultado:
            mensagem_sucesso_cadastro()
        else:
            mensagem_erro_cadastro()
    
    # ============= Botoes =============
    btn_remover_maquinista = ctk.CTkButton(
        app,
        text="Remover Maquinista",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=deletar
    )
    btn_remover_maquinista.place(relx=0.5, y=450, anchor="center")
    
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
        command=tela_supervisor
    )
    btn_sair.place(relx=0.5, y=550, anchor="center")
    
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

    btn_ranking = ctk.CTkButton(
        app,
        text="Ranking",
        width=349,
        height=53,
        font=("Arial", 20),
        corner_radius=10,
        fg_color="#001489",
        hover_color="#001a73",
        text_color="white",
        command=tela_ranking_maquinista
    )
    btn_ranking.place(relx=0.5, y=508, anchor="center")

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
        command=verifica_chave_servico
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
    botao_ddu.place(x=150, y=270)
    
    def botao_ddu_porta_lacrada():
        botao_adu.destroy()
        
        novo_botao_ddu = ctk.CTkButton(
            app,
            text="DDU",
            width=60,
            height=30,
            fg_color="white",
            text_color="black",
            font=("Arial", 20),
            hover=False,
            command=ddu_porta_lacrada
        )
        novo_botao_ddu.place(x=150, y=270)
        return novo_botao_ddu
    
    if obj_porta_lacrada.get_estado():
        botao_ddu_porta_lacrada()
    
    botao_vdu = ctk.CTkButton(
        app,
        text="VDU",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=vdu
    )
    botao_vdu.place(x=1000, y=250)

    botao_chave_reversora = ctk.CTkButton(
        app,
        text="Chave Reversora",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=verifica_chave_reversora
    )
    botao_chave_reversora.place(x=350, y=400)
    
    botao_modulo_comunicacao = ctk.CTkButton(
        app,
        text="Comunicação",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=modulo_comunicacao
    )
    botao_modulo_comunicacao.place(x=300, y=220)
    
    def botao_finalizar():
        botao_finalizar = ctk.CTkButton(
            app,
            text="Finalizar",
            width=60,
            height=30,
            fg_color="white",
            text_color="black",
            font=("Arial", 20),
            hover=False,
            command=fim_simulacao
        )
        botao_finalizar.place(relx=0.98, rely=0.02, anchor="ne")
        
    if obj_porta_lacrada.get_estado():
        botao_finalizar()

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
    
def ddu_porta_lacrada():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/DDU_porta_lacrada.jpg").resize((1300, 700))
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

def vdu():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/vdu.jpg").resize((1300, 700))
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

def chave_reversora_neutro():
    chave.set_estado("Neutro")
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/reversora_neutro.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # ============ Botões =============
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    # ============ Botões =============
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
    
    botao_frente = ctk.CTkButton(
        app,
        text="Frente",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_reversora_frente
    )
    botao_frente.place(x=950, y=300)
    
    botao_neutro = ctk.CTkButton(
        app,
        text="Neutro",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_reversora_neutro
    )
    botao_neutro.place(x=950, y=400)
    
    botao_re = ctk.CTkButton(
        app,
        text="Ré",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
    )
    botao_re.place(x=950, y=500)

def chave_reversora_frente():
    chave.set_estado("Frente")
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/reversora_frente.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    # ============ Botões =============
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

    botao_frente = ctk.CTkButton(
        app,
        text="Frente",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_reversora_frente
    )
    botao_frente.place(x=950, y=300)
    
    botao_neutro = ctk.CTkButton(
        app,
        text="Neutro",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_reversora_neutro
    )
    botao_neutro.place(x=950, y=400)
    
    

    botao_re = ctk.CTkButton(
        app,
        text="Ré",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
    )
    botao_re.place(x=950, y=500)

def modulo_comunicacao():
    for widget in app.winfo_children():
        widget.destroy()
    
    img_fundo = Image.open("./imgs/Simulacao/modulo_comunicacao.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
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
    
    botao_PA = ctk.CTkButton(
        app,
        text="PA",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=PA
    )
    botao_PA.place(x=150, y=100)
    
    botao_CCO = ctk.CTkButton(
        app,
        text="CCO",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_cco
    )
    botao_CCO.place(x=150, y=350)
    
def PA():
    estadoPA.set_estado(True)
    for widget in app.winfo_children():
        widget.destroy()
    
    img_fundo = Image.open("./imgs/Simulacao/PA.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    app.after(3000, modulo_comunicacao)

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
    botao_fechar_porta.place(x=600, y=450)

    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30,30)
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
        command=falhaPorta
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
        command=porta_saida
    )
    seta_esquerda.place(x=10, y=320)

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
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30,30)
    )
    
    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_saida
    )
    seta_esquerda.place(x=10, y=320)

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
    botao_abrir_porta.place(x=600, y=340)

def porta_saida(): 
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/porta_saida.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    if chave_servico.get_estado() == False:
        seta_cima = ctk.CTkButton(
            app,
            text="",
            width=60,
            height=60,
            image=imagem_seta_cima,
            fg_color="transparent",
            hover_color="#e0e0e0",
            command=verifica_porta_lacrada
        )
        seta_cima.place(relx=0.5, rely=0.05, anchor="n")
    else:
        seta_cima = ctk.CTkButton(
            app,
            text="",
            width=60,
            height=60,
            image=imagem_seta_cima,
            fg_color="transparent",
            hover_color="#e0e0e0",
            command=fim_simulacao_erro_chave
        )
        seta_cima.place(relx=0.5, rely=0.05, anchor="n")

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

def painel_direita():
    global cont1
    cont1 += 1
    if cont1 == 2:
        ponto.add_pontos(1)
    chave_servico.set_estado(True)
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/painel_direito_com_chave.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30,30)
    )
    
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_equipamentos
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
        command=falhaPorta
    )
    seta_esquerda.place(x=10, y=320)
    
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_cbtc
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

    botao_retirar_chave = ctk.CTkButton(
        app,
        text="Retirar Chave",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=painel_direita_sem_chave
    )
    botao_retirar_chave.place(x=600, y=350)

def painel_direita_sem_chave():
    
    chave_servico.set_estado(False)
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/painel_direito_sem_chave.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_equipamentos
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
        command=falhaPorta
    )
    seta_esquerda.place(x=10, y=320)
    
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_cbtc
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")
    
    botao_colocar_chave = ctk.CTkButton(
        app,
        text="Colocar Chave",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=painel_direita
    )
    botao_colocar_chave.place(x=600, y=350)
    
def equipamentos():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/equipamentos.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_servico
    )
    seta_esquerda.place(x=10, y=320)
    
    botao_pegar_equipamentos = ctk.CTkButton(
        app,
        text="Pegar Equipamentos",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=equipamentos_pegos
    )
    botao_pegar_equipamentos.place(x=600, y=300)

def equipamentos_pegos():
    obj_equipamentos.set_estado(False)
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/sem_equipamentos.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_servico
    )
    seta_esquerda.place(x=10, y=320)

def chave_cbtc_am():
    chave_cbtc.set_estado("AM")
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/cbtc_am.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_servico
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")
    
    botao_mcs = ctk.CTkButton(
        app,
        text="MCS",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_mcs
    )
    botao_mcs.place(x=950, y=300)
    
    botao_rm = ctk.CTkButton(
        app,
        text="RM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_rm
    )
    botao_rm.place(x=950, y=400)
    
    botao_am = ctk.CTkButton(
        app,
        text="AM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_am
    )
    botao_am.place(x=950, y=500)

def chave_cbtc_mcs():
    chave_cbtc.set_estado("MCS")
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/cbtc_mcs.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_servico
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")

    botao_mcs = ctk.CTkButton(
        app,
        text="MCS",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_mcs
    )
    botao_mcs.place(x=950, y=300)
    
    botao_rm = ctk.CTkButton(
        app,
        text="RM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_rm
    )
    botao_rm.place(x=950, y=400)
    
    botao_am = ctk.CTkButton(
        app,
        text="AM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_am
    )
    botao_am.place(x=950, y=500)
    
def chave_cbtc_rm():
    chave_cbtc.set_estado("RM")
    print(chave_cbtc.estado)

    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/cbtc_rm.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    
    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_chave_servico
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")

    botao_mcs = ctk.CTkButton(
        app,
        text="MCS",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_mcs
    )
    botao_mcs.place(x=950, y=300)
    
    botao_rm = ctk.CTkButton(
        app,
        text="RM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_rm
    )
    botao_rm.place(x=950, y=400)
    
    botao_am = ctk.CTkButton(
        app,
        text="AM",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=chave_cbtc_am
    )
    botao_am.place(x=950, y=500)
   
def lado_fora():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/lado_fora.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_saida
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_porta_falha
    )
    seta_direita.place(relx=0.95, rely=0.5, anchor="e")

def lado_fora_porta_lacrada():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/lado_fora_porta_lacrada.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_saida
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_lacrada
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")

def porta_falha():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/porta.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )

    # ============ Botões =============
    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=lado_dentro_falha
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")
    
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=vao
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=lado_fora
    )
    seta_esquerda.place(relx=0.05, rely=0.5, anchor="w")

    # Exibe o botão "Fechar Porta" apenas se o painel externo estiver aberto (estado True)
    if obj_painel.get_estado():
        botao_fechar_porta = ctk.CTkButton(
            app,
            text="Fechar Porta",
            width=60,
            height=30,
            fg_color="white",
            text_color="black",
            font=("Arial", 20),
            hover=False,
            command=porta_falha_fechada
        )
        botao_fechar_porta.place(relx=0.5, rely=0.5, anchor="center")

def porta_falha_fechada():
    ponto.add_pontos(4)
    obj_porta_falha.set_estado(False)
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/porta_fechada.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )

    # ============ Botões =============
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=lado_fora
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")
    
    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=painel_externo
    )
    seta_esquerda.place(relx=0.05, rely=0.5, anchor="w")
    
    botao_colocar_lacre = ctk.CTkButton(
        app,
        text="Colocar Lacre",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=porta_lacrada
    )
    botao_colocar_lacre.place(relx=0.5, rely=0.5, anchor="center")
 
def porta_lacrada():
    ponto.add_pontos(2)
    
    obj_porta_lacrada.set_estado(True)
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo2 = Image.open("./imgs/Simulacao/lacre_3.jpg").resize((1300, 700))
    bg_image2 = ImageTk.PhotoImage(img_fundo2)

    bg_label2 = ctk.CTkLabel(app, image=bg_image2, text="")
    bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=lado_fora_porta_lacrada
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")

def vao():
    ponto.add_pontos(1)
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/vao.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_cima = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_cima.png"),
        size=(30, 30)
    )
    imagem_seta_esquerda = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_esquerda.png"),
        size=(30, 30)
    )

    # ============ Botões =============
    seta_cima = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_cima,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_falha
    )
    seta_cima.place(relx=0.5, rely=0.05, anchor="n")
    
    seta_esquerda = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_esquerda,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=painel_externo
    )
    seta_esquerda.place(relx=0.05, rely=0.5, anchor="w")

def lado_dentro_falha():
    ponto.add_pontos(1)
    
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/lado_dentro_falha.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    imagem_seta_baixo = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_baixo.png"),
        size=(30, 30)
    )
    
    # ============ Botões =============
    seta_baixo = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_baixo,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=porta_falha
    )
    seta_baixo.place(relx=0.5, rely=0.95, anchor="s")
    

def painel_externo():
    global cont2
    cont2 += 1
    if cont2 == 2:
        ponto.add_pontos(1)
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/painel_externo.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    imagem_seta_direita = ctk.CTkImage(
        light_image=Image.open("./imgs/Simulacao/seta_direita.png"),
        size=(30, 30)
    )
    # ============ Botões =============
    seta_direita = ctk.CTkButton(
        app,
        text="",
        width=60,
        height=60,
        image=imagem_seta_direita,
        fg_color="transparent",
        hover_color="#e0e0e0",
        command=verifica_porta_falha
    )
    seta_direita.place(relx=0.95, rely=0.5, anchor="e")
    
    botao_abrir_painel = ctk.CTkButton(
        app,
        text="Abrir Painel",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=verifica_painel_externo
    )
    botao_abrir_painel.place(relx=0.5, rely=0.95, anchor="s")

def painel_externo_aberto():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/Simulacao/painel_externo_aberto.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    botao_fechar_painel = ctk.CTkButton(
        app,
        text="Fechar Painel",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=painel_externo
    )
    botao_fechar_painel.place(relx=0.5, rely=0.95, anchor="s")

    # ============ Isolamento de portas =============
    isoalar_porta1 = ctk.CTkButton(
        app,
        text="Isolar Porta 1",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_isolamento_errado
    )
    isoalar_porta1.place(x=1000, y=100)
    isoalar_porta2 = ctk.CTkButton(
        app,
        text="Isolar Porta 2",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=painel_externo_aberto_porta_isolada
    )
    isoalar_porta2.place(x=1000, y=150)
    isoalar_porta3 = ctk.CTkButton(
        app,
        text="Isolar Porta 3",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_isolamento_errado
    )
    isoalar_porta3.place(x=1000, y=200)
    isoalar_porta4 = ctk.CTkButton(
        app,
        text="Isolar Porta 4",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=mensagem_isolamento_errado
    )
    isoalar_porta4.place(x=1000, y=250)
    
def painel_externo_aberto_porta_isolada():
    ponto.add_pontos(3)
    
    obj_painel.set_estado(True)
    
    for widget in app.winfo_children():
        widget.destroy()
        
    # mensagem_isolamento_correto()

    img_fundo = Image.open("./imgs/Simulacao/painel_externo_aberto_porta_isolada.jpg").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    botao_fechar_painel = ctk.CTkButton(
        app,
        text="Fechar Painel",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=painel_externo
    )
    botao_fechar_painel.place(relx=0.5, rely=0.95, anchor="s")

# ============ Fim da simulação =============

def fim_simulacao():
    
    reversora_cbtc()
    voltar_reversora()
    ponto_pa()
    ponto_porta()
    ponto_cco()
    ponto_equipamento()
    
    cco.set_estado(False)
    estadoPA.set_estado(False)
    chave.set_estado("Neutro")
    chave_cbtc.set_estado("AM")
    obj_equipamentos.set_estado(True)
    chave_servico.set_estado(True)
    porta.set_porta(True)
    obj_porta_falha.set_estado(True)
    obj_porta_lacrada.set_estado(False)

    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Label de fim da simulação
    # Label de fim da simulação estilizado
    label_fim = ctk.CTkLabel(
        app,
        text="Simulação Concluída!",
        font=("Arial", 36, "bold"),
        text_color="#001489",
        fg_color="#eaf0fb",
        corner_radius=20,
        width=500,
        height=60
    )
    label_fim.place(relx=0.5, rely=0.38, anchor="center")

    # Label Pontos estilizado
    label_pontos = ctk.CTkLabel(
        app,
        text=f"{ponto.get_pontos()} Pontos",
        font=("Arial", 32, "bold"),
        text_color="#228B22",
        fg_color="#f5f6fa",
        corner_radius=20,
        width=350,
        height=50
    )
    label_pontos.place(relx=0.5, rely=0.5, anchor="center")

    botao_sair = ctk.CTkButton(
        app,
        text="Sair",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=abrir_menu
    )
    botao_sair.place(relx=0.5, rely=0.95, anchor="s")
    
    ponto.set_pontos(0)

def fim_simulacao_erro_chave():
    for widget in app.winfo_children():
        widget.destroy()

    img_fundo = Image.open("./imgs/fundo.png").resize((1300, 700))
    bg_image = ImageTk.PhotoImage(img_fundo)

    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    cco.set_estado(False)
    estadoPA.set_estado(False)
    chave.set_estado("Neutro")
    chave_cbtc.set_estado("AM")
    obj_equipamentos.set_estado(True)
    chave_servico.set_estado(True)
    porta.set_porta(True)
    obj_porta_falha.set_estado(True)
    obj_porta_lacrada.set_estado(False)
    ponto.set_pontos(0) 

    global rDAO
    rDAO.set_pontuacao()
    # Label de fim da simulação
    label_fim = ctk.CTkLabel(
        app,
        text="Simulação Finalizada!",
        font=("Arial", 36, "bold"),
        text_color="#001489",
        fg_color="#eaf0fb",
        corner_radius=20,
        width=500,
        height=60
    )
    label_fim.place(relx=0.5, rely=0.38, anchor="center")

    # Label Pontos estilizado
    label_pontos = ctk.CTkLabel(
        app,
        text=f"Erro: Você saiu sem a chave de serviço!",
        font=("Arial", 32, "bold"),
        text_color="#FF0000",
        fg_color="#f5f6fa",
        corner_radius=20,
        width=600,
        height=50
    )
    label_pontos.place(relx=0.5, rely=0.5, anchor="center")

    botao_sair = ctk.CTkButton(
        app,
        text="Sair",
        width=60,
        height=30,
        fg_color="white",
        text_color="black",
        font=("Arial", 20),
        hover=False,
        command=abrir_menu
    )
    botao_sair.place(relx=0.5, rely=0.95, anchor="s")

main()
app.mainloop()