import pygame
import pygame_gui
from models.ButtonModel import ButtonModel

pygame.init()
janela = pygame.display.set_mode((600, 400))
gerenciador_ui = pygame_gui.UIManager((600, 400))

botao = ButtonModel(gerenciador_ui, (220,150), (200,50), "jogar")
botao.get()

relogio = pygame.time.Clock()
executando = True

while executando:
    tempo_delta = relogio.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        gerenciador_ui.process_events(evento)

    gerenciador_ui.update(tempo_delta)
    janela.fill((0, 0, 0))
    gerenciador_ui.draw_ui(janela)
    pygame.display.update()
