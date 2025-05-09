import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função de login (placeholder)
def login():
    user = entry_id.get()
    senha = entry_senha.get()
    print(f"ID: {user}, Senha: {senha}")  # Substituir por lógica real depois

# Janela principal
root = tk.Tk()
root.title("Login - Metrô SP")
root.geometry("1300x700")
root.resizable(False, False)

# ===== Fundo com imagem =====
bg_img = Image.open("fundo.png")  # Renomeie sua imagem para esse nome ou ajuste aqui
bg_img = bg_img.resize((1300, 700))
bg_photo = ImageTk.PhotoImage(bg_img)

canvas = tk.Canvas(root, width=1300, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ===== Logo =====
logo_img = Image.open("logo metro.jpeg")  # Extraia o logo do topo e salve como imagem separada
logo_img = logo_img.resize((200, 60))  # Ajuste conforme necessário
logo_photo = ImageTk.PhotoImage(logo_img)
canvas.create_image(250, 70, image=logo_photo, anchor="center")

# ===== Label Login =====
label_login = tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg="#FFFFFF")
canvas.create_window(250, 150, window=label_login)

# ===== Campo ID =====
entry_id = ttk.Entry(root, width=30)
entry_id.insert(0, "ID")
canvas.create_window(501, 368, window=entry_id)

# ===== Campo Senha =====
entry_senha = ttk.Entry(root, width=30, show="*")
entry_senha.insert(0, "Senha")
canvas.create_window(501, 453, window=entry_senha)

# ===== Botão Entrar =====
btn_entrar = tk.Button(root, text="Entrar", bg="#0033CC", fg="white", font=("Arial", 10), width=20, command=login)
canvas.create_window(501, 590, window=btn_entrar)

root.mainloop()
