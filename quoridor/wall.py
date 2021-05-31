import pygame
from quoridor.data import BROWN, GAP, SQUARE_SIZE, SQUARE_DISTANCE


class Wall:
    def __init__(self, row, col, direction, temp=False):
        self.row = row
        self.col = col
        self.color = BROWN
        self.width = GAP
        self.length = 2 * SQUARE_SIZE + GAP
        self.drc = direction  # Vertical or horizontal
        self.x = 0
        self.y = 0
        self.find_pos()
        self.temp = temp

    def find_pos(self):
        if self.drc == "vertical":
            self.x = ((self.col - 1) / 2) * SQUARE_DISTANCE + SQUARE_SIZE
            self.y = (self.row / 2) * SQUARE_DISTANCE
        else:
            self.x = (self.col / 2) * SQUARE_DISTANCE
            self.y = ((self.row - 1) / 2) * SQUARE_DISTANCE + SQUARE_SIZE

    def draw(self, win):
        if (self.drc == "vertical"):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.length))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.length, self.width))

    def __str__(self):
        return 'wall'

    def does_temp_equals_wall(self, wall):
        # Getting a temporary wall and returning "True" if every parmeter of it is identical to the wall object, and "False otherwise
        if self.row == wall.row and self.col == wall.col and self.drc == wall.drc:
            return True
        return False