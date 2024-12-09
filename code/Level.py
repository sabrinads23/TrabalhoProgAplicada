import random
import time
import pygame
from code.Background import Background
from code.Food import Food
from code.Player import Player
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Score import Score  # Import da classe Score
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

        # Variáveis de controle do jogo
        self.lives = 7
        self.score = 0
        self.start_time = time.time()

        # Ícones redimensionados
        self.VIDA_img = self.load_scaled_asset('./asset/VIDA.png', (25, 25))
        self.PONTO_img = self.load_scaled_asset('./asset/PONTO.png', (25, 25))
        self.TEMPO_img = self.load_scaled_asset('./asset/TEMPO.png', (25, 25))

    def load_scaled_asset(self, path, size):
        """
        Carrega um asset de um caminho e redimensiona para o tamanho especificado.
        """
        asset = pygame.image.load(path)
        return pygame.transform.scale(asset, size)

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

        # Quando o jogo termina, exibe o placar final
        elapsed_time = int(time.time() - self.start_time)
        self.show_final_score(elapsed_time)

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
            elif food.rect.colliderect(self.player.get_head_rect()):  # Colisão com a cabeça do jogador
                if food.name.startswith('C'):  # Comida boa
                    self.score += 10
                elif food.name.startswith('V'):  # Veneno
                    self.lives -= 1
                    if self.lives <= 0:
                        self.running = False
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
        esc_message = font.render("Press ESC to exit ", True, (255, 255, 255))
        self.window.blit(esc_message, (WIN_WIDTH - esc_message.get_width() - 10, 10))

        # Exibe informações de jogo
        self.render_ui()

        pygame.display.flip()  # Atualiza a tela

    def render_ui(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 20)

        # Desenha corações (vidas)
        for i in range(self.lives):
            self.window.blit(self.VIDA_img, (10 + i * 27, 10))

        # Desenha estrela (pontuação)
        self.window.blit(self.PONTO_img, (10, 40))
        score_text = font.render(f"{self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (40, 42))

        # Desenha ampulheta (tempo)
        self.window.blit(self.TEMPO_img, (10, 75))
        elapsed_time = int(time.time() - self.start_time)
        time_text = font.render(f"{elapsed_time}s", True, (255, 255, 255))
        self.window.blit(time_text, (40, 75))

    def spawn_food(self):  # Cria uma comida em uma posição aleatória na parte superior da tela.
        screen_margin = 180  # Margem para não spawnar muito próximo às bordas
        x_position = random.randint(screen_margin, WIN_WIDTH - screen_margin)
        food_type = random.choice(['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6'])
        size = (40, 40)  # Defina o tamanho da comida aqui (largura, altura)
        food = Food(food_type, (x_position, 0), size)
        self.foods.append(food)

        # Ajusta o tempo do próximo spawn para espaçamento
        pygame.time.set_timer(self.spawn_food_event,
                              random.randint(1000, 2000))  # Intervalo aleatório entre 1 e 2 segundos

    def confirm_exit(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 20)
        prompt = font.render("Go back to the menu? Your score will be lost", True, (255, 255, 255))
        option_yes = font.render("Yes (ENTER)", True, (0, 255, 0))
        option_no = font.render("No (ESC)", True, (255, 0, 0))

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

    def show_final_score(self, elapsed_time):
        """
        Exibe o placar final usando a classe Score.
        """
        score_screen = Score(self.window)
        score_screen.save(score=self.score, elapsed_time=elapsed_time)

