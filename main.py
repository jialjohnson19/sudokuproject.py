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

board = Board.draw(screen)  # board is drawn from here


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Tic Tac Toe", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    start_text = button_font.render("Start", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # Initialize button background color and text
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill(LINE_COLOR)
    start_surface.blit(start_text, (10, 10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle
    start_rectangle = start_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return  # If the mouse is on the start button, we can return to main
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()


def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    button_font = pygame.font.Font(None, 70)
    winner = False
    screen.fill(BG_COLOR)
    if winner:
        text = f'Game Won!'
        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        # Initialize button background color and text
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20,
                                       exit_text.get_size()[1] + 20))
        exit_surface.fill((255, 165, 0))
        exit_surface.blit(exit_text, (10, 10))

        # initialize button rectangle
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(exit_surface, exit_rectangle)
    else:
        text = "Game Over :("
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        # Initialize button background color and text
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
                                          restart_text.get_size()[1] + 20))
        restart_surface.fill((255, 165, 0))
        restart_surface.blit(restart_text, (10, 10))

        # initialize button rectangle
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(restart_surface, restart_rectangle)

    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return  # If the mouse is on the start button, we can return to main
                elif exit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
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
            pass

    pygame.display.update()  # to display and update things on the screen
