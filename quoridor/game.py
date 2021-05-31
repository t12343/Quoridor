import pygame
from quoridor.board import Board
from quoridor.data import BLUE, RED, ROWS
from quoridor.wall import Wall
from minimax.minimax_algorithm import simulate_move
from copy import deepcopy

class Game:
    def __init__(self, win):
        # Game constractor
        self._init()
        self.win = win

    def _init(self):
        # Setting the values needed at the beginning of the game
        self.board = Board()
        self.turn = BLUE

    def reset(self):
        # Reseting the game
        self._init()

    def update(self, row, col, FONT):
        # Updating the game
        self.board.draw(self.win, row, col, FONT)
        pygame.display.update()

    def change_turn(self):
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE

    def move_pawn(self, pawn, row, col):
        # checking if pressed position is a square whuch can be reached by the pawn, and if it is, moving the pawn
        if row % 2 == 0 and col % 2 == 0:
            moves = self.board.find_valid_moves(pawn)
            if (row, col) in moves:
                self.board.move(pawn, row, col)
                self.change_turn()

    def add_wall(self, row, col):
        # Checking if a gap in the board was pressed, and if yes adding a wall to the board list
        drc = self.board.check_wall_direction(row, col)
        wall = Wall(row, col, drc)
        if self.board.is_temp_wall_in_place(wall):
            self.board.add_wall_to_list(wall)
            self.board.find_pawn(self.turn).walls_left -= 1
            self.change_turn()

    def add_temporary_wall(self, row, col):
        drc = self.board.check_wall_direction(row, col)
        if drc:
            wall = Wall(row, col, drc, True)
            if (row, col) in self.board.valid_wall_moves(self.turn):
                self.board.board[int(row)][int(col)] = wall



    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def distance_to_victory(self, board, color, distance=0, been_there=[]):
        if board.winner() == color:
            return distance




    def pawn_moves(self, board, color , been_there):
        moves = []
        for move in board.find_valid_moves(board.find_pawn(color)):
            if not move in been_there:
                temp_board = deepcopy(board)
                new_board = simulate_move(temp_board.find_pawn(color), move, temp_board, self.turn, self)
                moves.append(new_board)
        return moves

