import pygame
from quoridor.data import RED, WHITE, INSTRUCTIONS, RETURN_TEXT, TEXT_SIZE, WIDTH, FONT


class Instructions:
    def __init__(self):
        self.font = pygame.font.SysFont(FONT, TEXT_SIZE)
        self.instrucions_text = self.font.render(INSTRUCTIONS, True, WHITE)
        self.ret = self.font.render(RETURN_TEXT, True, WHITE)
        self.instrucions_pos = (5, 5)
        self.ret_pos = ((WIDTH - self.ret.get_width()) / 2, self.instrucions_text.get_height() + 10)

    def draw_screen(self, win):
        win.fill(RED)
        win.blit(self.instrucions_text, self.instrucions_pos)
        win.blit(self.ret, self.ret_pos)
        pygame.display.update()

    def back_to_hompage(self, pos):
        if pos[0] >= self.ret_pos[0] and pos[0] <= self.ret_pos[0] + self.ret.get_width() and pos[1] >= self.ret_pos[
            1] and pos[1] <= self.ret_pos[1] + self.ret.get_height():
            return 'hompage'
        return 'instructions'
