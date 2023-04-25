import pygame, sys
from constants import *
from cell import Cell
from sudoku_generator import *

# new
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)


class Board:
    def __init__(self, width, height, screen, difficulty):
        # self.rows = rows
        # self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # self.removed_cells = removed_cells
        if self.difficulty == 'easy':
            self.board = generate_sudoku(9, 30)
        elif self.difficulty == 'medium':
            self.board = generate_sudoku(9, 40)
        elif self.difficulty == 'hard':
            self.board = generate_sudoku(9, 50)
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        for row in self.cells:
            for col in row:
                if col.get_value == 0:
                    col.is_selected()

    def draw_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()
                # Call the draw() method for each Cell object

    def draw(self, screen):  # draws the lines for the board
        # horizontal lines
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
        for i in range(9, 10):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (0, i * SQUARE_SIZE),
                             (WIDTH, i * SQUARE_SIZE),
                             LINE_WIDTH_BIG)
            # vertical lines
            for i in range(1, 3):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, GAME_HEIGHT),
                                 LINE_WIDTH)
            for i in range(3, 4):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, GAME_HEIGHT),
                                 LINE_WIDTH_BIG)
            for i in range(4, 6):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, GAME_HEIGHT),
                                 LINE_WIDTH)
            for i in range(6, 7):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, GAME_HEIGHT),
                                 LINE_WIDTH_BIG)
            for i in range(7, 9):
                pygame.draw.line(screen,
                                 LINE_COLOR,
                                 (SQUARE_SIZE * i, 0),
                                 (SQUARE_SIZE * i, GAME_HEIGHT),
                                 LINE_WIDTH)
            # populate values in squares

    def select(self, row, col):
        return self.cells[row][col] 

    def user_selects(self, row, col):
        if self.cells[row][col].isSelected:
            return True 
        return False 
            

    def click(self, x, y):
        if x < 9 and x >= 0:
            if y < 9 and y >= 0:
                return (x, y)

    def clear(self):
        if self.board[row][col] == value:
            self.board[row][col] = 0
        # if sketch == value then also return 0?

    def available_cell(self, row, col):
        return self.cells[row][col] == 0

    def place_number(self, row, col, value):
        self.board[row][col] = value
        self.update_cells()

    def reset_to_original(self):
        for row in range(9):
            return 0
        for col in range(9):
            return 0

    def is_full(self):
        for i in self.cells:
            for j in i:
                if j.get_value() == 0:
                    return False
        return True

    def update_board(self):
        self.board = [[Board(self.board[row][col], row, col, SQUARE_SIZE,
                             SQUARE_SIZE) for col in range(self.cols)] for row in range(self.rows)]

    def find_empty(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                if board[i][j] == 0:
                    return i, j
        pass

    def check_board(self):
        # check rows
        for row in range(self.rows):
            row_vals = [val for val in self.board[row] if val != 0]
            if len(row_vals) != len(set(row_vals)):
                return False

        # check columns
        for col in range(self.cols):
            col_vals = [self.board[row][col] for row in range(self.rows) if self.board[row][col] != 0]
            if len(col_vals) != len(set(col_vals)):
                return False

        # check squares
        for square_row in range(0, self.rows, 3):
            for square_col in range(0, self.cols, 3):
                square_vals = []
                for row in range(square_row, square_row + 3):
                    for col in range(square_col, square_col + 3):
                        if self.board[row][col] != 0:
                            square_vals.append(self.board[row][col])
                if len(square_vals) != len(set(square_vals)):
                    return False

        # check that all values are between 1 and 9
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.board[row][col]
                if val < 1 or val > 9:
                    return False

        return True

    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height // self.rows,
                            self.width // self.cols) for j in range(self.cols)] for i
                      in range(self.rows)]
