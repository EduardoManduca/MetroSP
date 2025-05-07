import pygame_gui
import pygame

class ButtonModel:
    def __init__(self, manager, pos, size, text, id=None, tooltip=None, container=None):
        
        self.rect = pygame.Rect(pos, size)
        self.button = pygame_gui.elements.UIButton(
            relative_rect = self.rect,
            text = text,
            manager = manager,
            container = container,
            object_id = id,
            tool_tip_text = tooltip
        )
    
    def get(self):
        return self.button
