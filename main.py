import sys

import pygame
from code.Menu import Menu
from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

def main():
    pygame.init()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("FAT-CAT")
    clock = pygame.time.Clock()

    # Menu principal
    menu = Menu(window)
    while True:
        option = menu.run()
        if option == "NEW GAME":
            level = Level(window)
            level.run()
        elif option == "EXIT":
            pygame.quit()
            sys.exit()
        clock.tick(30)

if __name__ == "__main__":
    main()
