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
def draw_game_start(screen): # shows the game start screen
    #title font
    start_title_font = pygame.font.Font(None,100)
    button_font = pygame.font.Font(None,70)

    #background color
    screen.fill(BG_COLOR)

    #initiliezes and draws the title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    #initializes buttons text
    easy_text = button_font.render("Easy", 0, (155, 155, 155))
    medium_text = button_font.render("Medium", 0, (155, 155, 155))
    hard_text = button_font.render("Hard", 0, (155, 155, 155))

    #initializes button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1]+20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    #initliaizes the rectange of the buttons
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 + 50, HEIGHT // 2))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2 + 150, HEIGHT // 2))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2))

    #draws the rectangles
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    pass
                if medium_rectangle.collidepoint(event.pos):
                    pass
                if hard_rectangle.collidepoint(event.pos):
                    pass
        pygame.display.update


draw_game_start(screen)

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
            if event.type == pygame.K_KP_ENTER:
                pass

    #





        pygame.display.update() # to display and update things on the screen