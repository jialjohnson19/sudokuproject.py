import pygame, sys
from constants import *
from board import Board

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)

def draw_nums():
    num_1_surf = num_font.render('1', 0, NUM_COLOR)
    num_1_rect = num_1_surf.get_rect()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
board = Board.draw(screen)

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