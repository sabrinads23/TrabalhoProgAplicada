import random

import pygame
from code.Background import Background
from code.Food import Food
from code.Player import Player
from code.Const import WIN_WIDTH, WIN_HEIGHT
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

class Level:
    def __init__(self, window):
        self.window = window
        self.background = Background('BACKGROUND', (WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.player = Player((WIN_WIDTH / 2, WIN_HEIGHT - 43))
        self.foods = []  # Lista para armazenar as comidas
        self.running = True
        self.paused = False  # Inicializa o estado de pausa como False
        self.spawn_food_event = pygame.USEREVENT + 1  # Evento para spawnar comidas
        pygame.time.set_timer(self.spawn_food_event, 1500)  # Intervalo inicial (1,5 segundos)

        pygame.time.set_timer(self.spawn_food_event, 1000)  # Tempo para spawnar comidas (ms)

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
                    self.paused = not self.paused  # Alterna o estado de pausa
                    if self.paused:  # Se pausado, confirma a saída
                        if self.confirm_exit():
                            self.running = False
                        else:
                            self.paused = False  # Cancela a pausa se escolher continuar
            if event.type == self.spawn_food_event and not self.paused:  # Spawna uma nova comida se não estiver pausado
                self.spawn_food()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Atualiza a posição das comidas
        for food in self.foods[:]:
            food.update()
            if food.is_out_of_screen(WIN_HEIGHT):  # Remove comidas que saíram da tela
                self.foods.remove(food)

    def render(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.background.surf, self.background.rect)
        self.window.blit(self.player.surf, self.player.rect)

        # Desenha as comidas
        for food in self.foods:
            self.window.blit(food.surf, food.rect)

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

    def spawn_food(self):
        """
        Cria uma comida em uma posição aleatória na parte superior da tela.
        """
        screen_margin = 150  # Margem para não spawnar muito próximo às bordas
        x_position = random.randint(screen_margin, WIN_WIDTH - screen_margin)
        food_type = random.choice(['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6'])
        size = (40, 40)  # Defina o tamanho da comida aqui (largura, altura)
        food = Food(food_type, (x_position, 0), size)
        self.foods.append(food)

        # Ajusta o tempo do próximo spawn para espaçamento
        pygame.time.set_timer(self.spawn_food_event,
                              random.randint(1000, 2000))  # Intervalo aleatório entre 1 e 2 segundos

