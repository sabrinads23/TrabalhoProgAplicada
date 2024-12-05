import pygame
from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION, C_YELLOW, C_ORANGE, C_BROW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/BACKMENU.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        # Carregar e tocar a música do menu em looping
        pygame.mixer_music.load('./asset/musicamenu.wav')
        pygame.mixer_music.play(-1)  # -1 significa looping infinito

        while True:
            # Desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "FAT-CAT", C_ORANGE, (WIN_WIDTH / 2, 160))

            # Desenha as opções
            for i, option in enumerate(MENU_OPTION):
                color = C_ORANGE if i != menu_option else C_BROW
                self.menu_text(20, option, color, (WIN_WIDTH / 2, 210 + 30 * i))

            instruction_text = "Use as setas < > do teclado para mover o gato na direção das comidas."
            self.menu_text(10, instruction_text, C_WHITE, (WIN_WIDTH / 2, 289))

            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size, text, text_color, text_center_pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
