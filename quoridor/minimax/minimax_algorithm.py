from copy import deepcopy
import pygame
from quoridor.data import RED, BLUE
from quoridor.pawn import Pawn
from quoridor.wall import Wall


def minimax(position, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, False, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if alpha >= beta:
                break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimax(move, depth - 1, True, game, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if alpha >= beta:
                break
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def get_all_moves(board, color, game):
    moves = []
    pawn = board.find_pawn(color)
    for move in board.valid_wall_moves(color):
        temp_board = deepcopy(board)
        new_board = simulate_move(Wall(move[0], move[1], board.check_wall_direction(move[0], move[1])), move,
                                  temp_board, color, game)
        moves.append(new_board)
    for move in board.find_valid_moves(pawn):
        temp_board = deepcopy(board)
        temp_pawn = temp_board.find_pawn(color)
        new_board = simulate_move(temp_pawn, move, temp_board, color, game)
        moves.append(new_board)
    return moves


def simulate_move(item, move, board, turn, game):
    if item.__str__() == "pawn":
        board.move(item, move[0], move[1])
    elif item.__str__() == "wall":
        board.add_wall_for_simulation(move[0], move[1], turn)
    return board
