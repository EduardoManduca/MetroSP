# main.py
import pygame
import sys
from ButtonModel import Button
from InputBox import InputBox

# Inicializa o Pygame
pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Login Metrô")
clock = pygame.time.Clock()

# Carregamento das imagens
background = pygame.image.load("fundo.png")
background = pygame.transform.scale(background, (1300, 700))
logo = pygame.image.load("Logo metro.jpeg")
logo = pygame.transform.scale(logo, (300, 80))

# Cria os componentes
input_id = InputBox(501, 368, 200, 53, 'ID')
input_senha = InputBox(501, 453, 549, 53, 'Senha', password=True)
botao = Button(501, 590, 349, 53, "Entrar")

font = pygame.font.SysFont(None, 20)
titulo = font.render("Login", True, (0, 0))

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        input_id.handle_event(event)
        input_senha.handle_event(event)
        botao.handle_event(event)

    input_id.update()
    input_senha.update()

    screen.blit(background, (0, 0))
    screen.blit(logo, (441, 46))
    screen.blit(titulo, (435, 271))

    input_id.draw(screen)
    input_senha.draw(screen)
    botao.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
