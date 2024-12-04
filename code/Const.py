# C
import pygame

C_WHITE = (255, 255, 255)  # Cor branca
C_YELLOW = (255, 255, 128)  # Cor amarela
C_ORANGE = (255, 128, 0)  # Cor laranja
C_BLACK = (0, 0, 0)  # Cor preta
C_BLUE = (0, 0, 255)  # Cor azul

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Background': 0,  # Velocidade do fundo
    'Player': 3,  # Velocidade do jogador
    'PlayerShot': 5,  # Velocidade do tiro do jogador
}

ENTITY_HEALTH = {
    'Background': 999,
    'Player': 100,
    'PlayerShot': 1,
}

ENTITY_DAMAGE = {
    'Player': 10,
    'PlayerShot': 5,
}

ENTITY_SCORE = {
    'Player': 0,
}

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'EXIT')  # Opções do menu

# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_RCTRL}

# S
SPAWN_TIME = 4000  # Tempo de spawn de inimigos

# T
TIMEOUT_STEP = 100  # Passo de timeout em milissegundos
TIMEOUT_LEVEL = 20000  # Timeout do nível (20 segundos)

# W
WIN_WIDTH = 576  # Largura da janela do jogo
WIN_HEIGHT = 324  # Altura da janela do jogo

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 130),
    1: (WIN_WIDTH / 2, 150),
    2: (WIN_WIDTH / 2, 170),
    3: (WIN_WIDTH / 2, 190),
    4: (WIN_WIDTH / 2, 210),
    5: (WIN_WIDTH / 2, 230),
    6: (WIN_WIDTH / 2, 250),
    7: (WIN_WIDTH / 2, 270),
    8: (WIN_WIDTH / 2, 290),
    9: (WIN_WIDTH / 2, 310),
}
