import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *
from cell import Cell

pygame.init()
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
difficulty = "easy", "medium", "hard"
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
        center=(WIDTH // 2 - 200, HEIGHT // 2))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    hard_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2 + 250, HEIGHT // 2))
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                global removed_cells
                screen.fill(BG_COLOR)  # clears out beginner screen

                # sets up sudoku board according to difficulty
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 'easy'
                    return difficulty
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 'medium'
                    return difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 'hard'
                    return difficulty

                #sudoku = SudokuGenerator(9, removed_cells)  # initiates the randomly generated array
                #sudoku.fill_values()
                #sudoku.remove_cells()
                #global board
                #board = Board(sudoku.print_board(), difficulty)  # creates Board object out of SudokuGenerator
                #board.draw_board(screen)  # prints numbers
                #board.draw(screen)  # prints lines
                #pygame.display.update()
                #in_progress(screen)
                #pygame.display.update()


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
    if winner == 1:
        text = f'Game won!'
        screen.blit(restart_surface, restart_rectangle)
    else:
        winner == 0
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


def in_progress(screen):
    # this section draws out button menu at the bottom of the board
    button_font = pygame.font.Font(None, 70)
    # Initialize buttons
    # Initialize text first
    restart_text = button_font.render("RESTART", 0, (255, 255, 255))
    quit_text = button_font.render("EXIT", 0, (255, 255, 255))
    reset_text = button_font.render("RESET", 0, (255, 255, 255))

    # Initialize button background color and text
    # restart button
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20,
                                      restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    # quit button
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20,
                                   quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # reset button
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20,
                                    reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    # Initialize button rectangles
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    quit_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2 + 300, HEIGHT - 40))
    reset_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT - 40))

    screen.blit(restart_surface, restart_rectangle)
    screen.blit(quit_surface, quit_rectangle)
    screen.blit(reset_surface, reset_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on restart button
                    return  # If the mouse is on the restart button, we can return to main
                elif quit_rectangle.collidepoint(event.pos):  # If the mouse is on the quit button, exit the program
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):  # will clear out board to original
                    board.reset_to_original()
        pygame.display.update()

    pygame.display.update()



# start of MAIN

if __name__ == '__main__':
    game_over = False
    winner = 0

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)  # Calls function to draw start screen and game screen depending on difficulty
    # Assuming you have a Board object called 'board'

    board = Board(WIDTH, HEIGHT, screen, draw_game_start(screen))
    screen.fill(BG_COLOR)
    board.draw(screen)
    board.draw_board()
    in_progress(screen)
    pygame.display.update()

    key = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # Get the mouse position to insert number
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_row = int(event.pos[1] / SQUARE_SIZE)
                clicked_col = int(event.pos[0] / SQUARE_SIZE)

                if board.available_cell(clicked_row, clicked_col):
                    number = Cell(value, clicked_row, clicked_col)
                    number.selected = True
                    number.draw()
                    board.draw_board(screen)
                board.place_number(clicked_row, clicked_col, value)

        board.draw(screen)

    pygame.display.update()  # to display and update things on the screen
