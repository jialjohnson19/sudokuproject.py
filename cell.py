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

        if self.sketched_value is not None:
            sketched_font = pygame.font.Font(None, 20)
            sketched_surf = sketched_font.render(str(self.sketched_value), True, NUM_COLOR)
            sketched_rect = sketched_surf.get_rect(
                topleft=(self.col * SQUARE_SIZE + 5, self.row * SQUARE_SIZE + 5))
            self.screen.blit(sketched_surf, sketched_rect)

        elif self.value == 1:
            # define the location
            num_1_rect = num_1_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_1_surf, num_1_rect)

        elif self.value == 2:
            # define the location
            num_2_rect = num_2_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_2_surf, num_2_rect)

        elif self.value == 3:
            # define the location
            num_3_rect = num_3_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_3_surf, num_3_rect)

        elif self.value == 4:
            # define the location
            num_4_rect = num_4_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_4_surf, num_4_rect)

        elif self.value == 5:
            # define the location
            num_5_rect = num_5_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_5_surf, num_5_rect)

        elif self.value == 6:
            # define the location
            num_6_rect = num_6_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_6_surf, num_6_rect)

        elif self.value == 7:
            # define the location
            num_7_rect = num_7_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_7_surf, num_7_rect)

        elif self.value == 8:
            # define the location
            num_8_rect = num_8_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_8_surf, num_8_rect)

        elif self.value == 9:
            # define the location
            num_9_rect = num_9_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))

            # blit chip onto the screen
            self.screen.blit(num_9_surf, num_9_rect)

        # call draw value function
        # if cell is not 0, value is displayed
        # if cell has a 0 value, no value is displayed in cell
        # is outlined red if it is currently selected
