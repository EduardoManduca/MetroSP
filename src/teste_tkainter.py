import customtkinter as ctk
from PIL import Image, ImageTk

# Configuração inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1300x700")
app.title("Login - Metrô SP")
app.resizable(False, False)

# Fundo com imagem
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

btn_login = ctk.CTkButton(app, text="Entrar", width=349, height=53, corner_radius=10, fg_color="#001489",font=("Arial", 14), command=login)
btn_login.place(relx=0.5, y=590, anchor="center")

app.mainloop()

