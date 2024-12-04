#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION  # Certifique-se de que MENU_OPTION tenha as opções apropriadas


class Menu:
    def __init__(self, window):
        self.window = window
        # Carregar a imagem de fundo "BACKMENU"
        self.surf = pygame.image.load('./asset/BACKMENU.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # Desenhar a imagem de fundo
            self.window.blit(source=self.surf, dest=self.rect)

            # Adicionar o título "FAT CAT"
            self.menu_text(100, "FAT CAT", C_WHITE, ((WIN_WIDTH / 2), 100))

            # Exibir as opções do menu
            for i, option in enumerate(MENU_OPTION):
                if i == menu_option:
                    # Destacar a opção selecionada
                    self.menu_text(30, option, C_WHITE, ((WIN_WIDTH / 2), 250 + 50 * i))
                else:
                    # Exibir as demais opções
                    self.menu_text(30, option, C_WHITE, ((WIN_WIDTH / 2), 250 + 50 * i))

            pygame.display.flip()

            # Verificar os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar a janela
                    quit()  # Finalizar o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Tecla ENTER
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Exibe o texto na tela com a fonte e cor definidas"""
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
