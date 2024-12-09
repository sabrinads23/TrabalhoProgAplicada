import pygame

class Food:
    def __init__(self, name, position, size=(50, 50)):
        self.name = name
        self.image = pygame.image.load(f'./asset/{name}.png')
        self.image = pygame.transform.scale(self.image, size)  # Redimensiona a imagem
        self.surf = self.image  # Superfície a ser desenhada
        self.rect = self.surf.get_rect(topleft=position)

    def update(self):
        self.rect.y += 5  # Velocidade de queda

    def is_out_of_screen(self, screen_height):
        return self.rect.top > screen_height
