import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *
pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)

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
            print(row, col)
            # Board.click(x, y) # needs adjusting
            #if Board.available_cell(screen,board,row,col):
                # Board.select(board,row,col)
                #Cell.draw(value)
                #pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                diff = input("What difficulty do you want?(easy, medium, hard): ")
                if diff == "easy":
                   removed_cells = 30
                if diff == "medium":
                    removed_cells = 40
                if diff == "hard":
                    removed_cells = 50





##

    pygame.display.update() # to display and update things on the screen