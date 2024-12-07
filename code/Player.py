import pygame
from code.Entity import Entity
from code.Const import ENTITY_SPEED

class Player(Entity):
    def __init__(self, position):
        super().__init__('PLAYER', position)  # Nome do jogador é 'PLAYER'
  # Inicializa o jogador com uma imagem associada ao nome 'PLAYER'

    def update(self, keys):
        """
        Atualiza a posição do jogador com base nas teclas pressionadas.
        """
        if keys[pygame.K_LEFT]:  # Movimento para a esquerda
            self.rect.x -= ENTITY_SPEED[self.name]
        if keys[pygame.K_RIGHT]:  # Movimento para a direita
            self.rect.x += ENTITY_SPEED[self.name]

        # Limitar movimento dentro da tela com margem adicional
        screen_margin = 150
        if self.rect.left < screen_margin:  # Margem esquerda
            self.rect.left = screen_margin
        if self.rect.right > pygame.display.get_surface().get_width() - screen_margin:  # Margem direita
            self.rect.right = pygame.display.get_surface().get_width() - screen_margin
