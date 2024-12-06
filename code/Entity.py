import pygame

class Entity:
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/gato-1.png').convert_alpha()
        self.rect = self.surf.get_rect(center=position)

    def draw(self, window):
        window.blit(self.surf, self.rect)
