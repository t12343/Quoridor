import pygame
from quoridor.data import SQUARE_DISTANCE, SQUARE_SIZE, WALLS_AT_THE_START


class Pawn:
    def __init__(self, row, col, color, been_there=[]):
        # Pawn constractor
        self.row = row
        self.col = col
        self.color = color
        self.RADIUS = SQUARE_SIZE // 4
        self.walls_left = WALLS_AT_THE_START
        self.x = 0
        self.y = 0
        self.find_pos()
        self.been_there = been_there

    def find_pos(self):
        # Finding the exact position of the pawn on the board
        self.x = SQUARE_DISTANCE * (self.col / 2) + SQUARE_SIZE / 2
        self.y = SQUARE_DISTANCE * (self.row / 2) + SQUARE_SIZE / 2

    def draw(self, win):
        # Drawing the pawn
        pygame.draw.circle(win, self.color, (self.x, self.y), self.RADIUS)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.find_pos()

    def __str__(self):
        return 'pawn'
