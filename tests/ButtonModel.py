import pygame

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('#002f86')
        self.text = text
        self.font = pygame.font.SysFont(None, 32)
        self.text_surf = self.font.render(text, True, (255, 255, 255))
        self.clicked = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                print(f"Botão '{self.text}' clicado")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
        text_rect = self.text_surf.get_rect(center=self.rect.center)
        screen.blit(self.text_surf, text_rect)
