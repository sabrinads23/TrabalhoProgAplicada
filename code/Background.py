#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Surface
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = self.surf = pygame.image.load('./asset/BACKGROUND.png').convert_alpha()  # Carrega a imagem do fundo
        self.rect = self.surf.get_rect(left=0, top=0)  # Define a posição do fundo

    def move(self):
        # Nenhuma movimentação necessária, pois o fundo é estático
        pass
