# input_box.py
import pygame

class InputBox:
    def __init__(self, x, y, w, h, text='', password=False, bg_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('black')
        self.color_active = pygame.Color('#002f86')
        self.color = self.color_inactive
        self.text = ''
        self.bg_color = bg_color
        self.placeholder = text
        self.txt_surface = pygame.font.SysFont(None, 32).render(self.placeholder, True, self.color)
        self.active = False
        self.password = password
        self.font = pygame.font.SysFont(None, 32)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
            if self.active and not self.text:
                self.txt_surface = self.font.render('', True, self.color)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(self.text)
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        self.update_text()

    def update_text(self):
        if self.text:
            display_text = '*' * len(self.text) if self.password else self.text
        else:
            display_text = '' if self.active else self.placeholder
        self.txt_surface = self.font.render(display_text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)  # fundo branco
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
