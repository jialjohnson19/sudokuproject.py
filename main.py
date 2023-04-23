import pygame
import sys

from board import Board
from cell import Cell
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 90)
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)


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

draw()
c1 = Cell(1, 1, 0, screen)
c1.draw()


while True:  # window always showing in screen
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # mouse click or selection
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            print(row, col)
            # Board.click(x, y) # needs adjusting
            # if Board.available_cell(screen,board,row,col):
            # Board.select(board,row,col)
            # Cell.draw(value)
            # pass
        if event.type == pygame.K_KP_ENTER:
            pass

    pygame.display.update()  # to display and update things on the screen
