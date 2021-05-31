import pygame
from quoridor.data import RED, QUORIDOR, TITLE_SIZE, HOME_TEXT1, HOME_TEXT2, HOME_TEXT3, TEXT_SIZE, FONT, WHITE, WIDTH, \
    HEIGHT


class Home:
    def __init__(self):
        self.title_font = pygame.font.SysFont(FONT, TITLE_SIZE)
        self.text_font = pygame.font.SysFont(FONT, TEXT_SIZE)
        self.title = self.title_font.render(QUORIDOR, True, WHITE)
        self.ai = self.text_font.render(HOME_TEXT1, True, WHITE)
        self.networks = self.text_font.render(HOME_TEXT2, True, WHITE)
        self.instructions = self.text_font.render(HOME_TEXT3, True, WHITE)
        self.title_pos = ((WIDTH - self.title.get_width()) / 2, 5)
        self.text1_pos = ((WIDTH - self.ai.get_width()) / 2, HEIGHT / 3)
        self.text2_pos = ((WIDTH - self.networks.get_width()) / 2, self.text1_pos[1] + self.ai.get_height() + 10)
        self.text3_pos = (
            (WIDTH - self.instructions.get_width()) / 2, self.text2_pos[1] + self.networks.get_height() + 10)

    def draw_screen(self, win):
        win.fill(RED)
        win.blit(self.title, self.title_pos)
        win.blit(self.ai, self.text1_pos)
        win.blit(self.networks, self.text2_pos)
        win.blit(self.instructions, self.text3_pos)
        pygame.display.update()


    def play(self, pos):
        if pos[0] >= self.text1_pos[0] and pos[0] <= self.text1_pos[0] + self.ai.get_width() and pos[1] >= \
                self.text1_pos[1] and pos[1] <= self.text1_pos[1] + self.ai.get_height():
            return 'ai'
        elif pos[0] >= self.text2_pos[0] and pos[0] <= self.text2_pos[0] + self.networks.get_width() and pos[1] >= \
                self.text2_pos[1] and pos[1] <= self.text2_pos[1] + self.networks.get_height():
            return 'networks'
        elif pos[0] >= self.text3_pos[0] and pos[0] <= self.text3_pos[0] + self.instructions.get_width() and pos[1] >= \
                self.text3_pos[1] and pos[1] <= self.text3_pos[1] + self.instructions.get_height():
            return 'instructions'
        return 'hompage'
