import pygame, sys
from constants import *
from cell import Cell

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None,400)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.board = self.initialize_board()

    def draw(self): #draws the lines for the board
        #horizontal lines?
        def draw_lines():  # i believe this function has to go in board.py but works here for now
            for i in range(1, 3):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (0, i * SQUARE_SIZE),
                                 (WIDTH, i * SQUARE_SIZE),
                                 LINE_WIDTH)
            for i in range(3, 4):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (0, i * SQUARE_SIZE),
                                 (WIDTH, i * SQUARE_SIZE),
                                 LINE_WIDTH_BIG)
            for i in range(4, 6):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (0, i * SQUARE_SIZE),
                                 (WIDTH, i * SQUARE_SIZE),
                                 LINE_WIDTH)
            for i in range(6, 7):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (0, i * SQUARE_SIZE),
                                 (WIDTH, i * SQUARE_SIZE),
                                 LINE_WIDTH_BIG)
            for i in range(7, 9):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (0, i * SQUARE_SIZE),
                                 (WIDTH, i * SQUARE_SIZE),
                                 LINE_WIDTH)

                for i in range(1, 3):
                    pygame.draw.line(screen,
                                     LINE_COLOR,
                                     (SQUARE_SIZE * i, 0),
                                     (SQUARE_SIZE * i, HEIGHT),
                                     LINE_WIDTH)
                for i in range(3, 4):
                    pygame.draw.line(screen,
                                     LINE_COLOR,
                                     (SQUARE_SIZE * i, 0),
                                     (SQUARE_SIZE * i, HEIGHT),
                                     LINE_WIDTH_BIG)
                for i in range(4, 6):
                    pygame.draw.line(screen,
                                     LINE_COLOR,
                                     (SQUARE_SIZE * i, 0),
                                     (SQUARE_SIZE * i, HEIGHT),
                                     LINE_WIDTH)
                for i in range(6, 7):
                    pygame.draw.line(screen,
                                     LINE_COLOR,
                                     (SQUARE_SIZE * i, 0),
                                     (SQUARE_SIZE * i, HEIGHT),
                                     LINE_WIDTH_BIG)
                for i in range(7, 9):
                    pygame.draw.line(screen,
                                     LINE_COLOR,
                                     (SQUARE_SIZE * i, 0),
                                     (SQUARE_SIZE * i, HEIGHT),
                                     LINE_WIDTH)


    def select(self,row,col):
        pass


    def click(self,x,y):
        if self.board[row][col] == (x,y):
            return (x,y)
        else:
            return None

    def clear(self):
        pass

    def sketch(self):
        pass

    def place_numer(self,value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for i in range (self.rows):
            for j in range (self.cols):
                if self.board[i][j] == "-":
                    return False

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

while True: #window always showing in screen
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             # mouse click or selection
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            click(x,y)

    pygame.display.update() # to display and update things on the screen