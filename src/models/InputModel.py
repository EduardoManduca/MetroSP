import pygame

class InputModel:
    def __init__(self, x, y, w, h, fonte, cor_fundo=(255, 255, 255), cor_texto=(0, 0, 0),
                 cor_borda_inativa=(150, 150, 150), cor_borda_ativa=(0, 120, 255),
                 espessura_borda=2, raio_borda=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.fonte = fonte
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.cor_borda_inativa = cor_borda_inativa
        self.cor_borda_ativa = cor_borda_ativa
        self.espessura_borda = espessura_borda
        self.raio_borda = raio_borda

        self.texto = ""
        self.ativo = False
        self.render_texto = self.fonte.render(self.texto, True, self.cor_texto)

    def handle_event(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Ativa se clicar dentro da caixa
            if self.rect.collidepoint(evento.pos):
                self.ativo = True
            else:
                self.ativo = False

        elif evento.type == pygame.KEYDOWN and self.ativo:
            if evento.key == pygame.K_RETURN:
                print(self.texto)  # ou qualquer ação
                self.texto = ""
            elif evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                self.texto += evento.unicode

            self.render_texto = self.fonte.render(self.texto, True, self.cor_texto)

    def desenhar(self, tela):
        cor_borda = self.cor_borda_ativa if self.ativo else self.cor_borda_inativa

        pygame.draw.rect(tela, cor_borda, self.rect, border_radius=self.raio_borda)
        inner_rect = self.rect.inflate(-2 * self.espessura_borda, -2 * self.espessura_borda)
        pygame.draw.rect(tela, self.cor_fundo, inner_rect, border_radius=self.raio_borda)

        texto_rect = self.render_texto.get_rect(midleft=(inner_rect.x + 5, inner_rect.centery))
        tela.blit(self.render_texto, texto_rect)

    def get_text(self):
        return self.texto

