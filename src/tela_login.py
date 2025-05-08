import pygame
from models.ButtonModel import ButtonModel
from models.InputModel import InputModel
from models.LabelModel import LabelModel

pygame.init()
tela = pygame.display.set_mode((1336, 762))
fundo = pygame.image.load("./imgs/fundo.png").convert()
fundo = pygame.transform.scale(fundo, (1336, 762))

fundo_rect = fundo.get_rect()
tela_rect = tela.get_rect()
fundo_rect.center = tela_rect.center

fonte = pygame.font.SysFont(None, 36)   


botao_entrar = ButtonModel(
    "Entrar",
    501,590,349,53,
    fonte=fonte,
    cor=(0,20,137),
    cor_texto=(255,255,255),
    cor_borda=(0,20,137),
    espessura_borda=4,
    raio_borda=10
)
input_box_id = InputModel(
    501,368,349,53,
    fonte=fonte,
    raio_borda=10,
    espessura_borda=4,
    cor_borda_inativa=(0,20,137),
    cor_borda_ativa=(0,20,137)
)

input_box_senha = InputModel (
    501,453,349,53,
    fonte=fonte,
    raio_borda=10,
    espessura_borda=4,
    cor_borda_inativa=(0,20,137),
    cor_borda_ativa=(0,20,137)
)

label_login = LabelModel(
    "Login",
    635,271,
    fonte=fonte,
    cor=(0,0,0)
)

rodando = True

while rodando:
    tela.blit(fundo,(0,0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        input_box_id.handle_event(evento)
        input_box_id.handle_event(evento)
 
    input_box_id.desenhar(tela)
    input_box_senha.desenhar(tela)
    botao_entrar.desenhar(tela)
    label_login.desenhar(tela)
    pygame.display.flip()

