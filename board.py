import pygame
from constants import *
from cell import Cell

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.board = self.initialize_board()
        #self.cells ?

    def draw(self): #draws the lines for the board
        #horizontal lines?
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i,0),
                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


    def select(self,row,col):
        pass

    def click(self,x,y):
        pass

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

""" def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i *SQUARE_SIZE),
                         LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (SQUARE_SIZE * i, 0),
                         (SQUARE_SIZE * i, HEIGHT),
                         LINE_WIDTH) """