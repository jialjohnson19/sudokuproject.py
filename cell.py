# Alejandra

import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)


class Cell:

    def __init__(self, value, row, col, screen):
        # constructor for cell class
        # screen is a window from pycharm
        self.value = value
        self.sketched_value = None
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.event = None

    def is_selected(self):
        return self.selected

    def get_value(self):
        return self.value

    def selected(self):
        self.selected = True

    def set_cell_value(self, value):
        # setter for this cell's value
        self.value = value

    def set_sketched_value(self, value):
        # store the sketched value
        self.sketched_value = value

    def draw(self):

        # draws cell w value inside it
        # defining the text and number values
        num_font = pygame.font.Font(None, 90)
        num_surf = num_font.render(str(self.value), 0, NUM_COLOR)

        if self.value > 0:
            num_rect = num_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            self.screen.blit(num_surf, num_rect)

        elif self.is_selected() and self.value > 0:
            pygame.draw.rect(screen, (255, 0, 0),
                             pygame.Rect(self.col * SQUARE_SIZE, self.row *
                                         SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 12)
            self.selected = False

            num_rect = num_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            self.screen.blit(num_surf, num_rect)

        if self.sketched_value is not None:
            sketched_font = pygame.font.Font(None, 20)
            sketched_surf = sketched_font.render(str(self.sketched_value), True, NUM_COLOR)
            sketched_rect = sketched_surf.get_rect(
                topleft=(self.col * SQUARE_SIZE + 5, self.row * SQUARE_SIZE + 5))
            self.screen.blit(sketched_surf, sketched_rect)

        # call draw value function
        # if cell is not 0, value is displayed
        # if cell has a 0 value, no value is displayed in cell
        # is outlined red if it is currently selected



