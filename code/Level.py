import pygame
from code.Background import Background
from code.Player import Player
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Level:
    def __init__(self, window):
        self.window = window
        self.background = Background('BACKGROUND', (WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.player = Player((100, WIN_HEIGHT - 50))
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

    def render(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.background.surf, self.background.rect)
        self.window.blit(self.player.surf, self.player.rect)
        pygame.display.flip()
