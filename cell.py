# Alejandra
import pygame
from constants import *
from board import Board

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
board = Board.draw(screen)
num_font = pygame.font.Font(None, 400)


class Cell:
    def __init__(self, value, row, col, screen):
        # constructor for cell class
        # screen is a window from pycharm
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        # setter for this cell's value
        self.value = value

    def set_sketched_value(self, value):
        # setter for this cell's sketched value
        self.sketched_value = value

    def draw(self):
        # draws cell w value inside it
        # defining the text and number values
        num_font = pygame.font.Font(None, 400)
        num_1_surf = num_font.render('1', 0, NUM_COLOR)
        num_2_surf = num_font.render('2', 0, NUM_COLOR)
        num_3_surf = num_font.render('3', 0, NUM_COLOR)
        num_4_surf = num_font.render('4', 0, NUM_COLOR)
        num_5_surf = num_font.render('5', 0, NUM_COLOR)
        num_6_surf = num_font.render('6', 0, NUM_COLOR)
        num_7_surf = num_font.render('7', 0, NUM_COLOR)
        num_8_surf = num_font.render('8', 0, NUM_COLOR)
        num_9_surf = num_font.render('9', 0, NUM_COLOR)

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0),
                             pygame.Rect(self.col * SQUARE_SIZE, self.row *
                                         SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 12)
            self.selected = False

        if self.value == 1:
            # define the location
            num_1_rect = num_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_1_surf, num_1_rect)

        # call draw value function
        # if cell is not 0, value is displayed
        # if cell has a 0 value, no value is displayed in cell
        # is outlined red if it is currently selected


