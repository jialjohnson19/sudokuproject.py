import pygame, sys
from constants import *
from cell import Cell

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.board = self.initialize_board()

    def draw(self): #draws the lines for the board
        #horizontal lines?
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
        return self.board[row][col]

    def click(self,x,y):
        if self.board[row][col] == (x,y):
            return (x,y)
        else:
            return None

    def clear(self):
        pass

    def sketch(self,value):
        pass

    def place_number(self,value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for i in range (self.rows):
            for j in range (self.cols):
                if self.board[i][j] == 0:
                    return False
        return True

    def update_board(self):
        pass

    def find_empty(self):
        #should find empty cell and return row and col tuple
        if self.board[row][col] == 0:
            return (row,col)

    def check_board(self):
        # if value in each row or column does not equal another value then win

