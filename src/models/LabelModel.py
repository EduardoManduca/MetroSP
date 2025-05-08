import pygame

class LabelModel:
    def __init__(self, texto, x, y, fonte, cor=(0, 0, 0)):
        self.texto = texto
        self.x = x
        self.y = y
        self.fonte = fonte
        self.cor = cor
        self.atualizar_surface()

    def atualizar_surface(self):
        self.surface = self.fonte.render(self.texto, True, self.cor)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def set_texto(self, novo_texto):
        self.texto = novo_texto
        self.atualizar_surface()

    def desenhar(self, tela):
        tela.blit(self.surface, self.rect)

