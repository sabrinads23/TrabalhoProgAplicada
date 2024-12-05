import pygame

class Player:
    def __init__(self, position):
        self.surf = pygame.image.load('./asset/gato-1.png').convert_alpha()
        self.rect = self.surf.get_rect(center=position)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
