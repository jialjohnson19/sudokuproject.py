import pygame, sys
from constants import *
from cell import Cell

# new
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)

class Board:
    def __init__(self,width,height,screen,difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.board = self.initialize_board()
        self.cells = [[Cell(0, row, col, SQUARE_SIZE, SQUARE_SIZE) for col in
                       range(self.cols)] for row in range(self.rows)]

    def initialize_board(self):
        return [[0 for i in range(9)]for j in range (9)]
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

    def click(self, x, y):
        x, y = event.pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        print(row, col)
    def clear(self):
        pass


    def available_cell(self, board, row, col):
        return self.board[row][col] == 0

    def sketch(self,value):
        pass

    def place_number(self,value):
        if select(row, col):
            pass

    def reset_to_original(self):
        for row in range(9):
            if value != 0:
                return 0
        for col in range(9):
            if value != 0:
                return 0

    def is_full(self):
        for i in range (self.rows):
            for j in range (self.cols):
                if self.board[i][j] == 0:
                    return False
        return True

    def update_board(self):
        self.board = [[Board(self.board[row][col], row, col, SQUARE_SIZE,
                            SQUARE_SIZE) for col in range(self.cols)] for row in range(self.rows)]

    def find_empty(self):
        #should find empty cell and return row and col tuple
        for cell in board:
            if board[row][col] == 0:
                return (row,col)

    def check_board(self):
        for row in range(9):  #checks that each value in each row is different
            if self.board[row][0] != self.board[row][1] != self.board[row][2] != self.board[row][3] !=self.board[row][4] != self.board[row][5] != self.board[row][6] != self.board[row][7] != self.board[row][8]:
                return True
        for col in range(9): #checks that each value in ach column is different
            if self.board[col][0] != self.board[col][1] != self.board[col][2] != self.board[col][3] !=self.board[col][4] != self.board[col][5] != self.board[col][6] != self.board[col][7] != self.board[col][8]:
                return True
        for row in  range(9): #checks that the value are int between 1 and 9
            if value == (1-9):
                return True
        for col in range(9):
            if value == (1-9):
                return True
        return False



