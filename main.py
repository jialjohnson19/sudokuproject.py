import pygame, sys
from constants import *
from board import Board
from cell import Cell

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
board = Board.draw(screen)

c1 = Cell(1, 0, 0, screen)
c1.draw()

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
            print(row, col)
            # Board.click(x, y) # needs adjusting
            #if Board.available_cell(screen,board,row,col):
                # Board.select(board,row,col)
                #Cell.draw(value)
                #pass
        if event.type == pygame.K_KP_ENTER:
            pass



    pygame.display.update() # to display and update things on the screen