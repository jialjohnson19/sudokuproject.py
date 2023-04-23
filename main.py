import pygame
import sys

from board import Board
from cell import Cell
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 90)
font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 70)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
winner = False

board = Board.draw(screen)  # board is drawn from here


def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
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


draw_game_over(screen)

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
