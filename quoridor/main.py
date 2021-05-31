import pygame
from quoridor.data import WIDTH, HEIGHT, SQUARE_DISTANCE, SQUARE_SIZE, QUORIDOR, FONT, FONT_SIZE, RED, BLUE, DEPTH
from quoridor.game import Game
from minimax.minimax_algorithm import minimax
from home import Home
from instructions import Instructions
from end import End
pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Opening a window
pygame.display.set_caption(QUORIDOR)  # Displaying the name of the game at the top of the window
FONT_OBJ = pygame.font.SysFont(FONT, FONT_SIZE)


def find_mouse_pos(pos):
    # Finding on which square on the board th mouse has clicked
    x, y = pos
    if (y % SQUARE_DISTANCE > SQUARE_SIZE):
        row = (y // SQUARE_DISTANCE) * 2 + 1
        if (x % SQUARE_DISTANCE > SQUARE_SIZE):
            col = (x // SQUARE_DISTANCE) * 2 + 1
        else:
            col = (x // SQUARE_DISTANCE) * 2
    else:
        row = (y // SQUARE_DISTANCE) * 2
        if (x % SQUARE_DISTANCE > SQUARE_SIZE):
            col = (x // SQUARE_DISTANCE) * 2 + 1
        else:
            col = (x // SQUARE_DISTANCE) * 2
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    home = Home()
    ins = Instructions()
    end = End()
    game = Game(WIN)
    mode = 'hompage'
    winner = None

    """moves = game.pawn_moves(game.board, BLUE, [])
    for move in moves:
        print(move.board)
        print("")"""

    is_mouse_button_up = True
    while run:
        clock.tick(FPS)
        if mode == "hompage":
            home.draw_screen(WIN)
            for event in pygame.event.get():
                # Going over events in the game
                if event.type == pygame.QUIT:
                    # Checkig if the player has closed the window
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = home.play(pygame.mouse.get_pos())
        elif mode == "ai":
            row, col = find_mouse_pos(pygame.mouse.get_pos())
            if game.turn == RED:
                value, new_board = minimax(game.board, DEPTH, True, game)
                game.ai_move(new_board)

            winner = game.board.winner()
            if winner != None:
                game.reset()
                mode = 'end_screen'

            for event in pygame.event.get():
                # Going over events in the game
                if event.type == pygame.QUIT:
                    # Checkig if the player has closed the window
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_mouse_button_up = False
                    game.move_pawn(game.board.find_pawn(game.turn), row, col)
                    game.add_wall(row, col)
                if event.type == pygame.MOUSEBUTTONUP:
                    is_mouse_button_up = True
            if is_mouse_button_up:
                game.add_temporary_wall(row, col)

            game.update(row, col, FONT_OBJ)
        elif mode == 'networks':
            pygame.quit()
        elif mode == 'instructions':
            ins.draw_screen(WIN)
            for event in pygame.event.get():
                # Going over events in the game
                if event.type == pygame.QUIT:
                    # Checkig if the player has closed the window
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = ins.back_to_hompage(pygame.mouse.get_pos())

        elif mode == 'end_screen':
            end.find_color(winner)
            end.draw_screen(WIN)
            for event in pygame.event.get():
                # Going over events in the game
                if event.type == pygame.QUIT:
                    # Checkig if the player has closed the window
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = end.back_to_hompage(pygame.mouse.get_pos())

main()
