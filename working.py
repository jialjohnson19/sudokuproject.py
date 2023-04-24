def draw(self):  # draws the lines for the board
    # horizontal lines?
    for i in range(1, 3):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (GAME_WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH)
    for i in range(3, 4):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (GAME_WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH_BIG)
    for i in range(4, 6):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (GAME_WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH)
    for i in range(6, 7):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (GAME_WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH_BIG)
    for i in range(7, 9):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (GAME_WIDTH, i * SQUARE_SIZE),
                         LINE_WIDTH)

        for i in range(1, 3):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, GAME_HEIGHT),
                             LINE_WIDTH)
        for i in range(3, 4):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, GAME_HEIGHT),
                             LINE_WIDTH_BIG)
        for i in range(4, 6):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, GAME_HEIGHT),
                             LINE_WIDTH)
        for i in range(6, 7):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i,GAME_HEIGHT),
                             LINE_WIDTH_BIG)
        for i in range(7, 9):
            pygame.draw.line(screen,
                             LINE_COLOR,
                             (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, GAME_HEIGHT),
                             LINE_WIDTH)