import pygame
from code.Entity import Entity
from code.Const import ENTITY_SPEED

class Player(Entity):
    def __init__(self, position: tuple):
        super().__init__('Player', position)

    def move(self, keys, window_width):
        # Atualiza a posição do jogador com base nas teclas pressionadas
        if keys[pygame.K_LEFT]:  # Movimento para a esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[pygame.K_RIGHT]:  # Movimento para a direita
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Limitar o movimento para dentro da tela
        if self.rect.left < 0:  # Limite esquerdo
            self.rect.left = 0
        if self.rect.right > window_width:  # Limite direito
            self.rect.right = window_width
