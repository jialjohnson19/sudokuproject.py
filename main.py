import pygame, sys
from constants import *
from board import Board

pygame.init()
pygame.display.set_caption("Sudoku")
chip_font = pygame.font.Font(None,400)

def draw_nums():
    chip_1_surf = chip_font.render('1', 0, NUM_COLOR)
    chip_1_rect = chip_1_surf.get_rect()
def draw_lines(): #i believe this function has to go in board.py but works here for now
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
                         LINE_WIDTH)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
draw_lines() #belive will be draw() from board file


while True: #window always showing in screen
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() # to display and update things on the screen