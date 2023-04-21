import pygame, sys
from constants import *
from board import Board

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None,400)

def draw_nums():
    num_1_surf = num_font.render('1', 0, NUM_COLOR)
    num_1_rect = num_1_surf.get_rect()
def draw_lines(): #i believe this function has to go in board.py but works here for now
    for i in range(1, 3):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i *SQUARE_SIZE),
                         LINE_WIDTH)
    for i in range(3,4):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH_BIG)
    for i in range (4,6):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH)
    for i in range(6,7):
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


screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
draw() #belive will be draw() from board file


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

    pygame.display.update() # to display and update things on the screen