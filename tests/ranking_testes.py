import customtkinter as ctk
import sqlite3

DB_NAME = "maquinista_ranking.db"

# --- Configuração do Banco de Dados e Dados de Exemplo ---
def configurar_banco_de_dados_maquinista():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Criar tabela Usuario (adicionamos Nome, Senha é ignorada para ranking)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario (
            idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Email TEXT UNIQUE,
            Tipo TEXT
        )
        """)

        # Criar tabela Historico
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Historico (
            idHistorico INTEGER PRIMARY KEY AUTOINCREMENT,
            idUsuario INTEGER,
            TotalPontos INTEGER DEFAULT 0,
            Acertos INTEGER,
            NumSimulacoes INTEGER,
            MediaPontuacoes REAL,
            FOREIGN KEY (idUsuario) REFERENCES Usuario (idUsuario)
        )
        """)

        # Inserir dados de exemplo se as tabelas estiverem vazias
        cursor.execute("SELECT COUNT(*) FROM Usuario")
        if cursor.fetchone()[0] == 0:
            usuarios_exemplo = [
                ('VelozCondutor', 'vc@email.com', 'Maquinista'),
                ('Expresso Pioneiro', 'ep@email.com', 'Maquinista'),
                ('TrilhoMestre', 'tm@email.com', 'Maquinista'),
                ('SinalVerde', 'sv@email.com', 'Maquinista'),
                ('CargaPesada', 'cp@email.com', 'Maquinista'),
                ('PassageiroVIP', 'pv@email.com', 'Maquinista')
            ]
            cursor.executemany("INSERT INTO Usuario (Nome, Email, Tipo) VALUES (?, ?, ?)", usuarios_exemplo)

            historico_exemplo = [
                (1, 12500), # VelozCondutor
                (2, 11800), # Expresso Pioneiro
                (3, 13000), # TrilhoMestre
                (4, 9500),  # SinalVerde
                (5, 10500), # CargaPesada
                (6, 8000)   # PassageiroVIP
            ]
            # Ajuste para inserir TotalPontos diretamente
            cursor.executemany("INSERT INTO Historico (idUsuario, TotalPontos) VALUES (?, ?)", historico_exemplo)

            conn.commit()
            print("Banco de dados configurado e dados de exemplo inseridos.")
        else:
            print("Banco de dados já configurado.")

    except sqlite3.Error as e:
        print(f"Erro ao configurar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

def buscar_dados_ranking_maquinista(limite=5):
    conn = None
    dados_formatados = []
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        query = """
        SELECT u.Nome, h.TotalPontos
        FROM Usuario u
        JOIN Historico h ON u.idUsuario = h.idUsuario
        ORDER BY h.TotalPontos DESC
        LIMIT ?
        """
        cursor.execute(query, (limite,))
        dados_brutos = cursor.fetchall() # Lista de tuplas: [('Nome1', Pts1), ('Nome2', Pts2)]

        for i, (nome, pontuacao) in enumerate(dados_brutos):
            posicao_str = f"{i+1}º"
            dados_formatados.append((posicao_str, nome, pontuacao))
        
        return dados_formatados # Lista de tuplas: [('1º', 'Nome1', Pts1), ...]

    except sqlite3.Error as e:
        print(f"Erro ao buscar dados do ranking: {e}")
        return []
    finally:
        if conn:
            conn.close()

# --- Interface Gráfica CustomTkinter ---
class RankingAppMaquinista(ctk.CTk):
    def __init__(self, ranking_data):
        super().__init__()

        self.title("Ranking de Maquinistas")
        # self.geometry("450x450") # Ajuste conforme necessário
        self.configure(fg_color=("#ECECEC", "#2B2B2B")) # Cor de fundo da janela

        self.ranking_data = ranking_data

        # Cores
        self.border_color = "royal blue"
        self.line_color = "royal blue" # Usado como fg_color do frame da tabela
        self.header_fg_color = ("#DBDBDB", "#2B2B2B") # Um pouco diferente para cabeçalho
        self.cell_fg_color = ("#F9F9F9", "#343638")
        self.text_color = ("#101010", "#DCE4EE")

        self.criar_interface_ranking()

    def criar_interface_ranking(self):
        # Frame container principal com borda arredondada
        ranking_container_frame = ctk.CTkFrame(self,
                                               corner_radius=15,
                                               border_width=3,
                                               border_color=self.border_color,
                                               fg_color=self.cell_fg_color)
        ranking_container_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título "RANKING"
        label_titulo_ranking = ctk.CTkLabel(ranking_container_frame,
                                            text="RANKING",
                                            font=ctk.CTkFont(size=30, weight="bold"),
                                            text_color=self.border_color)
        label_titulo_ranking.pack(pady=(15, 10))

        # Frame interno para a tabela (vai simular as linhas com seu fg_color)
        table_frame = ctk.CTkFrame(ranking_container_frame, fg_color=self.line_color)
        table_frame.pack(pady=5, padx=10, fill="x")

        # Cabeçalhos da tabela
        headers = ["", "Maquinista", "Pontuação"] # Posição não tem título explícito
        header_font = ctk.CTkFont(size=14, weight="bold")

        for col_idx, header_text in enumerate(headers):
            if col_idx == 0: # Coluna da Posição (menor)
                table_frame.grid_columnconfigure(col_idx, weight=1, minsize=40)
            elif col_idx == 1: # Coluna do Maquinista (maior)
                table_frame.grid_columnconfigure(col_idx, weight=4, minsize=150)
            else: # Coluna da Pontuação
                table_frame.grid_columnconfigure(col_idx, weight=2, minsize=100)

            header_cell = ctk.CTkFrame(table_frame, fg_color=self.header_fg_color, corner_radius=0)
            header_cell.grid(row=0, column=col_idx, sticky="nsew", padx=(0 if col_idx ==0 else 1, 0 if col_idx == len(headers)-1 else 1), pady=(0,1)) # Linha de baixo
            
            label = ctk.CTkLabel(header_cell, text=header_text, font=header_font, text_color=self.text_color, padx=5, pady=5)
            label.pack(expand=True, fill="both")


        # Dados do Ranking
        if not self.ranking_data:
            no_data_label = ctk.CTkLabel(table_frame, text="Nenhum dado no ranking.",
                                         font=ctk.CTkFont(size=12), text_color=self.text_color,
                                         fg_color=self.cell_fg_color)
            no_data_label.grid(row=1, column=0, columnspan=len(headers), sticky="nsew", padx=0, pady=(1,0))
            return

        for row_idx, (posicao, nome, pontuacao) in enumerate(self.ranking_data):
            data_row_real_idx = row_idx + 1 # +1 por causa do cabeçalho

            # Cores para o top 3
            pos_text_color = self.text_color
            pos_font_weight = "normal"
            if posicao == "1º":
                pos_text_color = ("#B8860B", "gold") # DarkGoldenrod para light mode, gold para dark
                pos_font_weight = "bold"
            elif posicao == "2º":
                pos_text_color = ("#708090", "silver") # SlateGray para light, silver para dark
                pos_font_weight = "bold"
            elif posicao == "3º":
                pos_text_color = ("#8B4513", "#CD7F32") # SaddleBrown para light, bronze para dark
                pos_font_weight = "bold"

            celulas_linha = [posicao, nome, str(pontuacao)]
            
            for col_idx, cell_data in enumerate(celulas_linha):
                cell_frame = ctk.CTkFrame(table_frame, fg_color=self.cell_fg_color, corner_radius=0)
                # padx: sem borda externa nas colunas extremas, 1px para internas
                # pady: 1px em cima (se não for a primeira linha de dados), 1px em baixo
                cell_frame.grid(row=data_row_real_idx, column=col_idx, sticky="nsew",
                                padx=(0 if col_idx ==0 else 1, 0 if col_idx == len(headers)-1 else 1),
                                pady=(0 , 1)) # Linha de baixo

                font_weight = pos_font_weight if col_idx == 0 else "normal"
                current_text_color = pos_text_color if col_idx == 0 else self.text_color

                data_label = ctk.CTkLabel(cell_frame,
                                          text=cell_data,
                                          font=ctk.CTkFont(size=12, weight=font_weight),
                                          text_color=current_text_color,
                                          padx=5, pady=5)
                if col_idx == 0: # Posição
                    data_label.pack(expand=True, fill="both")
                elif col_idx == 1: # Nome
                     data_label.configure(anchor="w") # Alinhar nome à esquerda
                     data_label.pack(expand=True, fill="both", padx=(10,5))
                else: # Pontuação
                    data_label.configure(anchor="e") # Alinhar pontuação à direita
                    data_label.pack(expand=True, fill="both", padx=(5,10))

        # Ajustar a última linha para não ter padding inferior extra no table_frame
        # (já que as células têm pady(0,1))
        # Se quiser uma linha azul abaixo de tudo:
        # bottom_line = ctk.CTkFrame(table_frame, fg_color=self.line_color, height=1)
        # bottom_line.grid(row=len(self.ranking_data) + 1, column=0, columnspan=len(headers), sticky="ew")


if __name__ == "__main__":
    ctk.set_appearance_mode("system") # Pode ser "light", "dark"
    ctk.set_default_color_theme("blue") # Pode ser "blue", "dark-blue", "green"

    configurar_banco_de_dados_maquinista()
    dados_para_ranking = buscar_dados_ranking_maquinista(limite=5)

    app = RankingAppMaquinista(ranking_data=dados_para_ranking)
    app.mainloop()