def initialize_board(self):
    return generate_sudoku(9, removed)


 if event.type == pygame.MOUSEBUTTONDOWN:

                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    board = Board(WIDTH, HEIGHT, screen, difficulty)
                    board.draw(screen)
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    board = Board(9, 9, WIDTH, HEIGHT, screen, difficulty)
                    board.draw(screen)
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    board = Board(9, 9, WIDTH, HEIGHT, screen, difficulty)
                    board.draw(screen)
                    return