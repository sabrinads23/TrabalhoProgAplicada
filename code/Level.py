import pygame
from code.Background import Background
from code.Player import Player
from code.Const import WIN_WIDTH, WIN_HEIGHT
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

class Level:
    def __init__(self, window):
        self.window = window
        self.background = Background('BACKGROUND', (WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.player = Player((WIN_WIDTH / 2, WIN_HEIGHT - 43))  # Posição inicial do jogador
        self.running = True
        self.paused = False

    def run(self):
        # Carrega e toca a música do nível
        pygame.mixer.music.load('./asset/musicalevel.wav')
        pygame.mixer.music.play(-1)  # Loop infinito

        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            if not self.paused:  # Apenas atualiza e renderiza se o jogo não estiver pausado
                self.update()
                self.render()
            clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = True  # Pausa o jogo
                    if self.confirm_exit():  # Exibe a caixa de diálogo
                        self.running = False
                    self.paused = False  # Retorna ao jogo se não sair

    def update(self):
        keys = pygame.key.get_pressed()  # Obtém o estado das teclas pressionadas
        self.player.move(keys, WIN_WIDTH)  # Atualiza a posição do jogador com base nas teclas

    def render(self):
        self.window.fill((0, 0, 0))  # Limpa a tela com preto
        self.window.blit(self.background.surf, self.background.rect)  # Desenha o fundo
        self.player.draw(self.window)  # Desenha o jogador

        # Renderiza a mensagem no canto superior direito
        font = pygame.font.SysFont("Lucida Sans Typewriter", 9)
        esc_message = font.render("ESC para sair do jogo", True, (255, 255, 255))
        self.window.blit(esc_message, (WIN_WIDTH - esc_message.get_width() - 10, 20))

        pygame.display.flip()  # Atualiza a tela


    def confirm_exit(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 20)
        prompt = font.render("Deseja voltar ao menu e perder a pontuação?", True, (255, 255, 255))
        option_yes = font.render("Sim (ENTER)", True, (0, 255, 0))
        option_no = font.render("Não (ESC)", True, (255, 0, 0))

        while True:
            self.window.fill((146, 204, 209))
            self.window.blit(prompt, (WIN_WIDTH // 2 - prompt.get_width() // 2, WIN_HEIGHT // 2 - 50))
            self.window.blit(option_yes, (WIN_WIDTH // 2 - option_yes.get_width() // 2, WIN_HEIGHT // 2))
            self.window.blit(option_no, (WIN_WIDTH // 2 - option_no.get_width() // 2, WIN_HEIGHT // 2 + 40))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER para confirmar
                        return True
                    if event.key == K_ESCAPE:  # ESC para cancelar
                        return False
