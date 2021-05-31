import pygame
from quoridor.data import RED, WINNER_SIZE, WINNER_TEXT1, WINNER_TEXT2, RETURN_TEXT, TEXT_SIZE, FONT, WHITE, WIDTH, HEIGHT, BLUE

class End:
    def __init__(self):
        self.winner = None
        self.winner_font = pygame.font.SysFont(FONT, WINNER_SIZE)
        self.text_font = pygame.font.SysFont(FONT, TEXT_SIZE)
        self.winner_text = self.winner_font.render(WINNER_TEXT1 + str(self.winner) + WINNER_TEXT2, True, WHITE)
        self.ret = self.text_font.render(RETURN_TEXT, True, WHITE)
        self.winner_pos = ((WIDTH - self.winner_text.get_width()) / 2, 5)
        self.ret_pos = ((WIDTH - self.ret.get_width()) / 2, HEIGHT / 3)


    def draw_screen(self, win):
        self.winner_text = self.winner_font.render(WINNER_TEXT1 + str(self.winner) + WINNER_TEXT2, True, WHITE)
        self.winner_pos = ((WIDTH - self.winner_text.get_width()) / 2, 5)
        win.fill(RED)
        win.blit(self.winner_text, self.winner_pos)
        win.blit(self.ret, self.ret_pos)
        pygame.display.update()

    def find_color(self, color):
        if color == BLUE:
            self.winner = 'blue'
        if color == RED:
            self.winner = 'red'

    def back_to_hompage(self, pos):
        if pos[0] >= self.ret_pos[0] and pos[0] <= self.ret_pos[0] + self.ret.get_width() and pos[1] >= \
                self.ret_pos[1] and pos[1] <= self.ret_pos[1] + self.ret.get_height():
            return 'hompage'
        return 'end_screen'