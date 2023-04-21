#Alejandra
import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        # constructor for cell class
        # screen is a window from pycharm
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.selected = False
        pass

    def set_cell_value(self, value):
        # setter for this cell's value
        pass

    def set_sketched_value(self, value):
        # setter for this cell's sketched value
        pass

    def draw(self):
        # draws cell w value inside it
        num_font = pygame.font.Font(None, 400)
        num_1_surf = num_font.render('1', 0, NUM_COLOR)

        #repeat for numbers 1-9
        if self.value == 1:
            pass
        elif self.value == 2:
            pass
        elif self.value == 3:
            pass
        elif self.value == 4:
            pass
        elif self.value == 5:
            pass
        elif self.value == 6:
            pass
        elif self.value == 7:
            pass
        elif self.value == 8:
            pass
        elif self.value == 9:
            pass
        # call draw value function
        # if cell is not 0, value is displayed
        # if cell has a 0 value, no value is displayed in cell
        # cell is outlined red if it is currently selected
        pass
