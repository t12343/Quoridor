import random

import pygame
from quoridor.data import COLS, ROWS, RED_START_POS, RED, BLUE_START_POS, BLUE, BLACK, WHITE, SQUARE_DISTANCE, \
    SQUARE_SIZE, WIDTH
from quoridor.pawn import Pawn
from quoridor.wall import Wall
from copy import deepcopy
from minimax.minimax_algorithm import simulate_move


class Board:
    def __init__(self):
        # Board constractor
        self.board = []  # data on rows, cols and gaps, and weather they contain something or not
        self.create_board()

    def draw_squares(self, win):
        # Drawing the squares on the board
        win.fill(BLACK)
        for col in range(COLS):
            for row in range(ROWS):
                pygame.draw.rect(win, WHITE, (col * SQUARE_DISTANCE, row * SQUARE_DISTANCE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        # Creating the board list with everything in starting positions
        for vertical_space in range(ROWS + (ROWS - 1)):
            self.board.append([])
            for horizontal_space in range(COLS + (COLS - 1)):
                self.board[vertical_space].append(0)
        self.board[RED_START_POS[1]][RED_START_POS[0]] = Pawn(RED_START_POS[1], RED_START_POS[0], RED)
        self.board[BLUE_START_POS[1]][BLUE_START_POS[0]] = Pawn(BLUE_START_POS[1], BLUE_START_POS[0], BLUE)

    def draw(self, win, mouse_row, mouse_col, font):
        # Drawing the squares, walls and pawns
        self.draw_squares(win)
        for row in range(ROWS + (ROWS - 1)):
            for col in range((COLS + COLS - 1)):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(win)
                    self.remove_temporary_wall(self.board[row][col], mouse_row, mouse_col)
        blue_walls = font.render("There are " + str(self.find_pawn(BLUE).walls_left) + " blue walls left", True, WHITE)
        red_walls = font.render("There are " + str(self.find_pawn(RED).walls_left) + " red walls left", True, WHITE)
        win.blit(blue_walls, (0, WIDTH))
        win.blit(red_walls, (WIDTH - red_walls.get_width(), WIDTH))

    def move(self, pawn, row, col):
        # Moving a given pawn to a given position on the board
        self.board[int(pawn.row)][int(pawn.col)], self.board[int(row)][int(col)] = self.board[int(row)][int(col)], \
                                                                                   self.board[int(pawn.row)][
                                                                                       int(pawn.col)]
        pawn.move(row, col)

    def add_wall_to_list(self, wall):
        # Getting a wall and adding it to the board list
        self.board[int(wall.row)][int(wall.col)] = wall
        if (wall.drc == "vertical"):
            self.board[int(wall.row + 1)][int(wall.col)] = wall
            self.board[int(wall.row + 2)][int(wall.col)] = wall
        else:
            self.board[int(wall.row)][int(wall.col + 1)] = wall
            self.board[int(wall.row)][int(wall.col + 2)] = wall

    def check_wall_direction(self, row, col):
        # If the pos given is a gap, returning the direction of it. otherwise returning None
        if int(row % 2) == 0 and int(col % 2) == 1:
            return "vertical"
        elif int(row % 2) == 1 and int(col % 2) == 0:
            return "horizontal"
        return None

    def is_wall_possible(self, wall, turn):
        if self.find_pawn(turn).walls_left <= 0:
            return False
        if wall.drc == "vertical":
            if wall.row + 2 >= ROWS * 2 - 1 or self.board[int(wall.row + 1)][int(wall.col)] != 0 or \
                    self.board[int(wall.row + 2)][int(wall.col)] != 0 or self.board[int(wall.row)][int(wall.col)] != 0:
                return False
        elif wall.col + 2 >= COLS * 2 - 1 or self.board[int(wall.row)][int(wall.col + 1)] != 0 or \
                self.board[int(wall.row)][int(wall.col + 2)] != 0 or self.board[int(wall.row)][int(wall.col)] != 0:
            return False
        return True

    def is_temp_wall_in_place(self, wall):
        if self.board[int(wall.row)][int(wall.col)].__str__() == "wall":
            if wall.does_temp_equals_wall(self.board[int(wall.row)][int(wall.col)]):
                return True

    def find_valid_moves(self, pawn):
        # Returns a list of all of the moves a pawn can make
        moves = []
        if self.is_in_board(pawn.row - 2, pawn.col) and self.is_passage_possible(pawn, "up"):
            moves.append((pawn.row - 2, pawn.col))
        if self.is_in_board(pawn.row + 2, pawn.col) and self.is_passage_possible(pawn, "down"):
            moves.append((pawn.row + 2, pawn.col))
        if self.is_in_board(pawn.row, pawn.col + 2) and self.is_passage_possible(pawn, "right"):
            moves.append((pawn.row, pawn.col + 2))
        if self.is_in_board(pawn.row, pawn.col - 2) and self.is_passage_possible(pawn, "left"):
            moves.append((pawn.row, pawn.col - 2))
        return moves

    def is_in_board(self, row, col):
        # Gets a position and returning "True" if the position is on the board, and "False" otherwise
        if row < 0 or row >= ROWS * 2 - 1 or col < 0 or col >= COLS * 2 - 1:
            return False
        return True

    def is_passage_possible(self, pawn, direction):
        # Gets a pawn and direction (string) and return "False" if a wall blocks the path or the other pawn is at the destination, and returns "True" otherwise
        if direction == "up":
            if self.board[int(pawn.row - 1)][int(pawn.col)] != 0 or self.board[int(pawn.row - 2)][int(pawn.col)] != 0:
                return False
        elif direction == "down":
            if self.board[int(pawn.row + 1)][int(pawn.col)] != 0 or self.board[int(pawn.row + 2)][int(pawn.col)] != 0:
                return False
        elif direction == "right":
            if self.board[int(pawn.row)][int(pawn.col + 1)] != 0 or self.board[int(pawn.row)][int(pawn.col + 2)] != 0:
                return False
        elif direction == "left":
            if self.board[int(pawn.row)][int(pawn.col - 1)] != 0 or self.board[int(pawn.row)][int(pawn.col - 2)] != 0:
                return False
        return True

    def find_pawn(self, color):
        # getting pawn's color and returning the pawn.
        for row in range(ROWS * 2 - 1):
            for col in range(COLS * 2 - 1):
                if self.board[row][col] != 0 and self.board[row][col].color == color:
                    return self.board[row][col]

    def remove_temporary_wall(self, wall, row, col):
        # get an item in the board list and the mouse's position, and if it is a temporary wall that should not exist anymore - remove it from the list
        if self.board[int(wall.row)][int(wall.col)].__str__() == "wall":
            if self.board[int(wall.row)][int(wall.col)].temp == True:
                if row != self.board[int(wall.row)][int(wall.col)].row or col != self.board[int(wall.row)][
                    int(wall.col)].col:
                    self.board[int(wall.row)][int(wall.col)] = 0

    def valid_wall_moves(self, turn):
        # Returns a list of all possible wall moves
        moves = []
        for row in range(0, ROWS * 2 - 1, 2):
            for col in range(1, COLS * 2 - 1, 2):
                wall = Wall(row, col, self.check_wall_direction(row, col))
                if self.is_wall_possible(wall, turn):
                    moves.append((row, col))
        for row in range(1, ROWS * 2 - 1, 2):
            for col in range(0, COLS * 2 - 1, 2):
                wall = Wall(row, col, self.check_wall_direction(row, col))
                if self.is_wall_possible(wall, turn):
                    moves.append((row, col))
        return moves

    def winner(self):
        # Returns the winners' color
        for square in self.board[0]:
            if square.__str__() == "pawn":
                if square.color == BLUE:
                    return square.color
        for square in self.board[ROWS * 2 - 2]:
            if square.__str__() == "pawn":
                if square.color == RED:
                    return square.color
        return None

    def add_wall_for_simulation(self, row, col, turn):
        drc = self.check_wall_direction(row, col)
        if drc:
            wall = Wall(row, col, drc)
            if (row, col) in self.valid_wall_moves(turn):
                self.board[int(row)][int(col)] = wall
                if (wall.drc == "vertical"):
                    self.board[int(wall.row + 1)][int(wall.col)] = wall
                    self.board[int(wall.row + 2)][int(wall.col)] = wall
                else:
                    self.board[int(wall.row)][int(wall.col + 1)] = wall
                    self.board[int(wall.row)][int(wall.col + 2)] = wall
                self.find_pawn(turn).walls_left -= 1


    def evaluate(self):
        #return self.minimal_distance_to_victory(BLUE) - self.minimal_distance_to_victory(RED)
        return random.randrange(0, 100)

"""    def minimal_distance_to_victory(self, color, board, distance = 0):
        if self.winner() == color:
            return distance
        
        for move in self.pawn_moves(board, color):
            distance = min()
    
    def pawn_moves(self, board, color):
        moves = []
        pawn = board.find_pawn(color)
        temp_pawn = deepcopy(pawn)
        for move in board.find_valid_moves(temp_pawn):
            if not move in temp_pawn.been_there:
                temp_board = deepcopy(board)
                new_board = simulate_move(temp_board.find_pawn(color), move, temp_board, color, self)
                moves.append(new_board)
        return moves"""
