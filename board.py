import pygame
from constants import *
from cell import Cell
from sudoku_generator import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # setting up different difficulties
        # 30, 40, 50 represent removed cells
        if difficulty == 'easy':
            self.board = generate_sudoku(9, 30)
        elif difficulty == 'medium':
            self.board = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            self.board = generate_sudoku(9, 50)

        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        for row in self.cells:
            for col in row:
                if col.get_value == 0:
                    col.selected()

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

        # calls cell object to draw
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):
        self.cells[row][col].highlight_cell()

    def click(self, x, y):
        if 0 <= x < 9:
            if 0 <= y < 9:
                return x, y

    def clear(self, row, col):  # clears cell value when delete is pressed
        self.cells[row][col].set_cell_value(0)

    def place_value(self, value, row, col):
        # sets cell value to what user inputted and then user presses enter key
        if value == pygame.K_1:
            self.cells[row][col].set_cell_value(1)
            self.cells[row][col].selected()
        if value == pygame.K_2:
            self.cells[row][col].set_cell_value(2)
            self.cells[row][col].selected()
        if value == pygame.K_3:
            self.cells[row][col].set_cell_value(3)
            self.cells[row][col].selected()
        if value == pygame.K_4:
            self.cells[row][col].set_cell_value(4)
            self.cells[row][col].selected()
        if value == pygame.K_5:
            self.cells[row][col].set_cell_value(5)
            self.cells[row][col].selected()
        if value == pygame.K_6:
            self.cells[row][col].set_cell_value(6)
            self.cells[row][col].selected()
        if value == pygame.K_7:
            self.cells[row][col].set_cell_value(7)
            self.cells[row][col].selected()
        if value == pygame.K_8:
            self.cells[row][col].set_cell_value(8)
            self.cells[row][col].selected()
        if value == pygame.K_9:
            self.cells[row][col].set_cell_value(9)
            self.cells[row][col].selected()


    def board_full(self):
        for i in self.cells:
            for j in i:
                if j.get_value() == 0:
                    return False  # if there is any blank value board is not full
        return True

    def find_cleared(self):
        for i in range(self.width):
            for j in range(self.height):
                if board[i][j] == 0:
                    return i, j  # returns coordinates of where the cell is empty
        pass

    def check_board(self):
        for i in range(9):
            if not self.is_editable(i, i):
                return False
        return True

    def editable(self, row, col):
        if self.cells[row][col].is_selected:
            return True
        return False

    def editable_row(self, row):
        numbers = []
        for i in range(9):
            if self.cells[row][i].get_value() in numbers or self.cells[row][i].get_value == 0:
                return False
            else:
                numbers.append(self.cells[row][i].get_value())
        return True

    def editable_col(self, col):
        numbers = []
        for i in range(9):
            if self.cells[i][col].get_value() in numbers or self.cells[i][col].get_value == 0:
                return False
            else:
                numbers.append(self.cells[i][col].get_value())
        return True

    def editable_box(self, row_start, col_start):
        numbers = []
        for i in range(3):
            for j in range(3):
                if self.cells[row_start + i][col_start + j].get_value() in numbers or \
                        self.cells[row_start + i][col_start + j].get_value == 0:
                    return False
                else:
                    numbers.append(self.cells[row_start + i][col_start + j].get_value())
        return True

    def is_editable(self, row, col):
        row_start = row // 3
        row_start *= 3
        col_start = col // 3
        col_start *= 3
        if self.editable_box(row_start, col_start):
            if self.editable_row(row):
                if self.editable_col(col):
                    return True
        return False



