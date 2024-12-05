import pygame

class Background:
    def __init__(self, name, position):
        self.surf = pygame.image.load(f'./asset/BACKGROUND.jpg').convert_alpha()
        self.rect = self.surf.get_rect(center=position)
