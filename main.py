import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
board = Board.draw(screen)
winner = False

def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200 , HEIGHT // 2 ))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2 , HEIGHT // 2 ))
    hard_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2 + 250, HEIGHT // 2))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return  # If the mouse is on the start button, we can return to main
                elif medium_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    return
                elif hard_rectangle.collidepoint(even.pos):
                    return
        pygame.display.update()

def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 200)
    screen.fill(BG_COLOR)
    button_font = pygame.font.Font(None, 70)
    # Initialize buttons
    # Initialize text first
    restart_text = button_font.render("RESTART", 0, (255, 255, 255))
    quit_text = button_font.render("EXIT", 0, (255, 255, 255))

    # Initialize button background color and text
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
                                      restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20,
                                   quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))

    if winner:
        text = f'Game won!'
        screen.blit(restart_surface, restart_rectangle)
    else:
        text = "Game Over :("
        screen.blit(quit_surface, quit_rectangle)
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_rectangle.collidepoint(event.pos):
                # Checks if mouse is on restart button
                return  # If the mouse is on the start button, we can return to main
            elif quit_rectangle.collidepoint(event.pos):  # If the mouse is on the quit button, exit the program
                sys.exit()
        pygame.display.update()


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
            diff = input("what difficulty do you want?")
            if diff == "easy":
                removed_cells = 30
            if diff == "medium":
                removed_cells = 40
            if diff == "hard":
                removed_cells = 50
            else:
                print("Invalid Input!")

    ##

    pygame.display.update()  # to display and update things on the screen
