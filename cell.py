import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.sketched = None
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_selected = False

    def is_selected(self):
        return self.is_selected

    def selected(self):
        self.is_selected = True

    def get_value(self):
        return self.value

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self): # draws numbers in the cell
        num_font = pygame.font.Font(None, 90)
        num_surf = num_font.render(str(self.value), 0, LINE_COLOR)
        if self.value > 0 and self.is_selected:
            num_surf = num_font.render(str(self.value), 0, NUM_COLOR)
            num_rect = num_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)
            pygame.display.update()
        if self.value > 0:
            num_rect = num_surf.get_rect(
                center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row *
                        SQUARE_SIZE + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)

    def highlight_cell(self):
        # upper line
        pygame.draw.line(self.screen, RED, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE),
                         ((self.col + 1) * SQUARE_SIZE, self.row * SQUARE_SIZE), LINE_WIDTH)

        # line on bottom
        pygame.draw.line(self.screen, RED, (self.col * SQUARE_SIZE, (self.row + 1) * SQUARE_SIZE),
                         ((self.col + 1) * SQUARE_SIZE, (self.row + 1) * SQUARE_SIZE), LINE_WIDTH)

        # left line
        pygame.draw.line(self.screen, RED, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE),
                         (self.col * SQUARE_SIZE, (self.row + 1) * SQUARE_SIZE), LINE_WIDTH)

        # right line
        pygame.draw.line(self.screen, RED, ((self.col + 1) * SQUARE_SIZE, self.row * SQUARE_SIZE),
                         ((self.col + 1) * SQUARE_SIZE, (self.row + 1) * SQUARE_SIZE), LINE_WIDTH)



