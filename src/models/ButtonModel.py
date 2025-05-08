import pygame

class ButtonModel:
    def __init__(self, texto, x,y, largura,altura, cor, cor_texto, fonte, acao=None, cor_borda=None, espessura_borda=0, raio_borda=0):
        self.texto = texto
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor 
        self.cor_texto = cor_texto,
        self.fonte = fonte
        self.acao = acao
        self.cor_borda = cor_borda
        self.espessura_borda = espessura_borda
        self.raio_borda = raio_borda


    def desenhar(self, tela):
        if self.cor_borda and self.espessura_borda > 0:
            pygame.draw.rect(tela, self.cor_borda, self.rect, border_radius=self.raio_borda)
            inner_rect = self.rect.inflate(-2 * self.espessura_borda, -2 * self.espessura_borda)
            pygame.draw.rect(tela, self.cor, inner_rect, border_radius=self.raio_borda)
        else:
            pygame.draw.rect(tela, self.cor, self.rect, border_radius=self.raio_borda)


        texto_render = self.fonte.render(self.texto, True, self.cor_texto)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        tela.blit(texto_render, texto_rect)

    def clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                if self.acao:
                    self.acao()
