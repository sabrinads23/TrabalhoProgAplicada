import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
import json

from code.Const import C_ORANGE, C_BROW1  # Certifique-se de que essas constantes estão definidas

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/SCOREBG.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.score_file = 'scores.json'  # Arquivo onde as pontuações serão salvas

    def save(self, score: int, elapsed_time: int):
        """
        Salva a pontuação e exibe a tela de entrada do nome do jogador.
        """
        pygame.mixer_music.load('./asset/musicamenu.wav')
        pygame.mixer_music.play(-1)
        name = ''
        while True:
            self.window.blit(self.surf, self.rect)  # Corrigido de 'source' para o uso correto de 'blit'
            self.display_text(40, 'GAME OVER', C_ORANGE, (self.window.get_width() // 2, 160))  # Alteração para 'display_text'
            self.display_text(20, f"Your Score: {score}", C_BROW1, (self.window.get_width() // 2, 200))
            self.display_text(20, f"Time Played: {elapsed_time}s", C_BROW1, (self.window.get_width() // 2, 220))
            self.display_text(16, "Enter your name:", C_BROW1, (self.window.get_width() // 2, 260))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and 1 <= len(name) <= 12:
                        # Salva os dados no arquivo JSON
                        self.save_score_to_file(name, score, elapsed_time)
                        self.show_top_scores()  # Exibe os top scores após salvar
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 12:
                        name += event.unicode

            self.display_text(20, name, (255, 255, 0), (self.window.get_width() // 2, 350))
            pygame.display.flip()

    def show_top_scores(self):
        pygame.mixer_music.load('./asset/musicamenu.wav')
        pygame.mixer_music.play(-1)
        scores = self.load_scores_from_file()  # Carrega os scores do arquivo JSON
        scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]  # Ordena pela pontuação

        self.window.blit(self.surf, self.rect)
        self.display_text(48, 'HIGH SCORES', (255, 215, 0), (400, 100))
        self.display_text(20, 'Name    Score    Time    Date', (255, 255, 255), (400, 150))

        for i, entry in enumerate(scores):
            name, score, time, date = entry['name'], entry['score'], entry['time'], entry['date']
            self.display_text(20, f"{name:<12}   {score:<6}   {time}s   {date}", (255, 255, 255), (400, 180 + i * 30))

        self.display_text(20, "Press ESC to return", (255, 255, 255), (400, 360))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

    def display_text(self, size: int, text: str, color: tuple, position: tuple):
        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        text_surf: Surface = font.render(text, True, color)
        text_rect: Rect = text_surf.get_rect(center=position)
        self.window.blit(text_surf, text_rect)

    @staticmethod
    def get_date():
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    def save_score_to_file(self, name: str, score: int, elapsed_time: int):
        # Salva a pontuação no arquivo JSON
        entry = {
            'name': name,
            'score': score,
            'time': elapsed_time,
            'date': self.get_date()
        }
        scores = self.load_scores_from_file()
        scores.append(entry)

        with open(self.score_file, 'w') as f:
            json.dump(scores, f, indent=4)

    def load_scores_from_file(self):
        # Carrega as pontuações do arquivo JSON
        try:
            with open(self.score_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Se o arquivo não existir, retorna uma lista vazia
