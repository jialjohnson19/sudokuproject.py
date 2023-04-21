import pygame, sys
from constants import *
from board import Board
pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
board = Board.draw(screen)

Board.find_empty(screen)

while True: #window always showing in screen
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             # mouse click or selection
        if event.type == pygame.MOUSEBUTTONDOWN:
            Board.click(x, y) # needs adjusting
            #if Board.available_cell(screen,board,row,col):
                # Board.select(board,row,col)
                #Cell.draw(value)
                #pass
        if event.type == pygame.K_KP_ENTER:
            pass







    pygame.display.update() # to display and update things on the screen