import pygame

class Food:
    def __init__(self, food_type, position, size=(50, 50)):
        """
        Cria uma comida com um tipo específico, posição e tamanho ajustável.
        :param food_type: Tipo da comida (ex: 'C1', 'V1').
        :param position: Posição inicial da comida (x, y).
        :param size: Tamanho da comida (largura, altura).
        """
        self.type = food_type
        self.image_path = f'./asset/{food_type}.png'
        self.surf = pygame.image.load(self.image_path).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, size)  # Redimensiona a imagem
        self.rect = self.surf.get_rect(topleft=position)

    def update(self):
        """Atualiza a posição da comida (fazendo-a cair)."""
        self.rect.y += 5  # Velocidade de queda (ajuste conforme necessário)

    def is_out_of_screen(self, screen_height):
        """Verifica se a comida saiu da tela."""
        return self.rect.top > screen_height
