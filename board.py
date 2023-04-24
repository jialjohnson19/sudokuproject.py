import pygame, sys
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator

# new
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)


class Board:
    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = "easy", "medium", "hard"
        self.board = self.initialize_board()
        self.cells = [[Cell(0, row, col, SQUARE_SIZE) for col in
                       range(self.cols)] for row in range(self.rows)]

    def initialize_board(self):
        return [[0 for i in range(9)] for j in range(9)]

    def draw(self):  # draws the lines for the board
        # horizontal lines?
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
                
        # this section draws out button menu at the bottom of the board
        button_font = pygame.font.Font(None, 70)
        # Initialize buttons
        # Initialize text first
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        quit_text = button_font.render("EXIT", 0, (255, 255, 255))
        reset_text = button_font.render("RESET", 0, (255, 255, 255))

        # Initialize button background color and text
        # restart button
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
                                          restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))

        # quit button
        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20,
                                       quit_text.get_size()[1] + 20))
        quit_surface.fill(LINE_COLOR)
        quit_surface.blit(quit_text, (10, 10))

        # reset button
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20,
                                        reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))

        # Initialize button rectangles
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 15))
        quit_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2 + 300, HEIGHT - 15))
        reset_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2 - 200, HEIGHT - 15))

        screen.blit(restart_surface, restart_rectangle)
        screen.blit(quit_surface, quit_rectangle)
        screen.blit(reset_surface, reset_rectangle)

         while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rectangle.collidepoint(event.pos):
                        # Checks if mouse is on restart button
                        return  # If the mouse is on the restart button, we can return to main
                    elif quit_rectangle.collidepoint(event.pos):  # If the mouse is on the quit button, exit the program
                        sys.exit()
                    elif reset_rectangle.collidepoint(event.pos):  # will clear out board to original
                        self.Board.reset_to_original()
            pygame.display.update()

        pygame.display.update()


    def select(self, row, col):
        return self.board[row][col]

    def clear(self):
        if self.board[row][col] == value:
            self.board[row][col] == 0
        # if sketch == value then also return 0?

    def available_cell(self, board, row, col):
        if self.board[row][col] == 0:
            return self.board[row][col]

    def place_number(self, row, col, value):
        self.board[row][col] = value
        self.update_cells()
    
    def difficulty_level(self,difficulty):
        if self.board[difficulty] == easy:
            pass
        if self.board[difficulty] == medium:
            pass 
        if self.board[difficulty] == hard:
            pass

    def reset_to_original(self):
        for row in range(9):
            if value != 0:
                return 0
        for col in range(9):
            if value != 0:
                return 0

    def is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return False
        return True

    def update_board(self):
        self.board = [[Board(self.board[row][col], row, col, SQUARE_SIZE,
                             SQUARE_SIZE) for col in range(self.cols)] for row in range(self.rows)]

    def find_empty(self):
        # should find empty cell and return row and col tuple
        for cell in board:
            if board[row][col] == 0:
                return (row, col)

    def check_board(self):
        for row in range(9):  # checks that each value in each row is different
            if self.board[row][0] != self.board[row][1] != self.board[row][2] != self.board[row][3] != self.board[row][
                4] != self.board[row][5] != self.board[row][6] != self.board[row][7] != self.board[row][8]:
                return True
        for col in range(9):  # checks that each value in ach column is different
            if self.board[col][0] != self.board[col][1] != self.board[col][2] != self.board[col][3] != self.board[col][
                4] != self.board[col][5] != self.board[col][6] != self.board[col][7] != self.board[col][8]:
                return True
        for row in range(9):  # checks that the value are int between 1 and 9
            if value == (1 - 9):
                return True
        for col in range(9):
            if value == (1 - 9):
                return True
        return False
