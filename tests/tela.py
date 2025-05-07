import pygame
import sys



pygame.init()
tela = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Login Metrô")

USAR_IMAGEM_DE_FUNDO = False  # Altere para False se quiser fundo branco

CAMINHO_IMAGEM = "fundo.png"  # Nome da imagem (adicione no mesmo diretório)

try:
    fundo_img = pygame.image.load(CAMINHO_IMAGEM).convert()
    fundo_img = pygame.transform.scale(fundo_img, tela.get_size())
except pygame.error:
    print(f"[ERRO] Imagem '{CAMINHO_IMAGEM}' não encontrada. Usando fundo branco.")
    USAR_IMAGEM_DE_FUNDO = False

fonte_logo = pygame.font.SysFont("Arial", 36, bold=True)
fonte_titulo = pygame.font.SysFont("Arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("Arial", 20)

# Cores
AZUL = (0, 64, 255)
AZUL_ESCURO = (0, 32, 128)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)


class ButtonModel:
    def __init__(self, pos, size, texto, cor=AZUL_ESCURO, cor_hover=AZUL, texto_cor=BRANCO):
        self.rect = pygame.Rect(pos, size)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.texto_cor = texto_cor
        self.hover = False

    def desenhar(self, tela):
        cor_atual = self.cor_hover if self.hover else self.cor
        pygame.draw.rect(tela, cor_atual, self.rect, border_radius=8)
        texto_render = fonte_texto.render(self.texto, True, self.texto_cor)
        texto_pos = texto_render.get_rect(center=self.rect.center)
        tela.blit(texto_render, texto_pos)

    def checar_hover(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def foi_clicado(self, evento):
        return evento.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(evento.pos)


class InputModel:
    def __init__(self, pos, size, placeholder=""):
        self.rect = pygame.Rect(pos, size)
        self.texto = ""
        self.placeholder = placeholder
        self.ativo = False

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect, border_radius=6)
        pygame.draw.rect(tela, PRETO, self.rect, 2, border_radius=6)
        if self.texto or self.ativo:
            txt_surface = fonte_texto.render(self.texto, True, PRETO)
        else:
            txt_surface = fonte_texto.render(self.placeholder, True, CINZA)
        tela.blit(txt_surface, (self.rect.x + 10, self.rect.y + 8))

    def manipular_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.ativo = self.rect.collidepoint(evento.pos)
        if evento.type == pygame.KEYDOWN and self.ativo:
            if evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            elif evento.key == pygame.K_RETURN:
                self.ativo = False
            else:
                self.texto += evento.unicode

    def get_texto(self):
        return self.texto


# Componentes
input_id = InputModel((200, 150), (200, 35), "ID")
input_senha = InputModel((200, 200), (200, 35), "Senha")
botao_entrar = ButtonModel((200, 260), (200, 45), "Entrar")

# Loop principal
clock = pygame.time.Clock()
rodando = True

while rodando:
    if USAR_IMAGEM_DE_FUNDO:
        tela.blit(fundo_img, (0, 0))
    else:
        tela.fill(BRANCO)


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        input_id.manipular_evento(evento)
        input_senha.manipular_evento(evento)

        if botao_entrar.foi_clicado(evento):
            print("ID:", input_id.get_texto())
            print("Senha:", input_senha.get_texto())

    # Hover do botão
    mouse_pos = pygame.mouse.get_pos()
    botao_entrar.checar_hover(mouse_pos)

    # Logo e título
    logo = fonte_logo.render("METRÔ", True, AZUL_ESCURO)
    tela.blit(logo, logo.get_rect(center=(300, 60)))

    titulo = fonte_titulo.render("Login", True, PRETO)
    tela.blit(titulo, titulo.get_rect(center=(300, 115)))

    # Desenhar componentes
    input_id.desenhar(tela)
    input_senha.desenhar(tela)
    botao_entrar.desenhar(tela)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
