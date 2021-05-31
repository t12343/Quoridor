WIDTH, HEIGHT = 800, 850  # The dimensions of the window
ROWS, COLS = 9, 9  # The amount of rows and columns on the board
GAP = (WIDTH / 9) / ROWS - 1  # THE distance between two adjacent squares
SQUARE_SIZE = (WIDTH - GAP * 8) / ROWS  # The size of a square
SQUARE_DISTANCE = SQUARE_SIZE + GAP  # The distance between one corner of a square to the same corner of an adjacent square
WALLS_AT_THE_START = 10  # The amount of walls each player begins with
RED_START_POS = COLS - 1, 0
BLUE_START_POS = COLS - 1, (ROWS - 1) * 2
QUORIDOR = 'quoridor'
FONT = 'arial'
FONT_SIZE = 20
DEPTH = 1
TITLE_SIZE = 100
HOME_TEXT1 = '1 player'
HOME_TEXT2 = '2 players'
HOME_TEXT3 = 'instructions'
TEXT_SIZE = 30
WINNER_TEXT1 = 'The '
WINNER_TEXT2 = ' player is the winner!'
WINNER_SIZE = 50
RETURN_TEXT = 'return to homepage'
INSTRUCTIONS = """In quoridor, your goal is to get your pawn to the other side of\n
               the board before your opponent. There are 2 possible actions you can\n
               make: move your pawn one block to any side, or place a wall. a pawn\n
               can't move through a wall. To move a pawn, tou need to click on a\n
               square adjacent to the pawn's square. When your mouse is above a gap\n
               in the board, you will see the wall you can place there, if it is\n
               possible according to these rules: all of the wall is within the board,\n
               walls can not overlap and walls can not cross each other. to permanently\n 
               place a wall, left click when you see the wall. to reset the board and\n 
               the game, click 'r'."""


# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (175, 100, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
