import customtkinter as ctk

class Botao(ctk.CTkButton):
    def __init__(
        self,
        master=None,
        texto="Clique aqui",
        comando=None,
        largura=120,
        altura=32,
        cor_fundo=None,
        cor_texto=None,
        fonte=None,
        borda=0,
        cor_borda=None,
        **kwargs
    ):
        super().__init__(
            master,
            text=texto,
            command=comando,
            width=largura,
            height=altura,
            fg_color=cor_fundo,
            text_color=cor_texto,
            font=fonte,
            border_width=borda,
            border_color=cor_borda,
            **kwargs
        )