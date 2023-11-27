for i in range(9):
            for j in range(9):
                # Draw vertical lines every three columns.
                if j % 3 == 0 and j != 0:
                    pygame.draw.line(self.window,(0, 0, 0),(j // 3 * 180, 0),(j // 3 * 180, 540),4,)

                # Draw horizontal lines every three rows.
                if i % 3 == 0 and i != 0:
                    pygame.draw.line(self.window,(0, 0, 0),(0, i // 3 * 180),(540, i // 3 * 180),4,)







if (i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()




for i in range(10):
        # Draw horizontal lines
            cell_size = width // 9
        # Draw horizontal lines
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), 2)
        # Draw vertical lines
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), 2)
        

def draw_board(self):
        """
        Draws the Sudoku board on the Pygame window.
        """
        for i in range(9):
            for j in range(9):
                # Draw vertical lines every three columns.
                if j % 3 == 0 and j != 0:
                    pygame.draw.line(self.window,(0, 0, 0),(j // 3 * 180, 0),(j // 3 * 180, 540),4)
                    pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                # Draw horizontal lines every three rows.
                if i % 3 == 0 and i != 0:
                    pygame.draw.line(
                        self.window,
                        (0, 0, 0),
                        (0, i // 3 * 180),
                        (540, i // 3 * 180),
                        4,
                    )

                # Draw the Tile object on the board.
                self.tiles[i][j].draw((0, 0, 0), 1)

                # Display the Tile value if it is not 0 (empty).
                if self.tiles[i][j].value != 0:
                    self.tiles[i][j].display(
                        self.tiles[i][j].value, (21 + j * 60, 16 + i * 60), (0, 0, 0)
                    )
        # Draw a horizontal line at the bottom of the board.
        pygame.draw.line(
            self.window,
            (0, 0, 0),
            (0, (i + 1) // 3 * 180),
            (540, (i + 1) // 3 * 180),
            4,
        )



class Board:
    def __init__(self, window):
        """
        Initializes a Board object.

        Args:
            window: The Pygame window object.
        """
        # Generate a new Sudoku board and create a solved version of it.
        self.board = generate_board()
        self.solvedBoard = deepcopy(self.board)
        solve(self.solvedBoard)
        # Create a 2D list of Tile objects to represent the Sudoku board.
        self.tiles = [
            [Tile(self.board[i][j], window, i * 60, j * 60) for j in range(9)]
            for i in range(9)
        ]
        self.window = window

    def draw_board(self):
            """
            Draws the Sudoku board on the Pygame window.
            """
            for i in range(9):
                for j in range(9):
                    # Draw vertical lines every three columns.
                    if j % 3 == 0 and j != 0:
                        pygame.draw.line(
                            self.window,
                            (0, 0, 0),
                            (j // 3 * 180, 0),
                            (j // 3 * 180, 540),
                            4,
                        )

                    # Draw horizontal lines every three rows.
                    if i % 3 == 0 and i != 0:
                        pygame.draw.line(
                            self.window,
                            (0, 0, 0),
                            (0, i // 3 * 180),
                            (540, i // 3 * 180),
                            4,
                        )

                    # Draw the Tile object on the board.
                    self.tiles[i][j].draw((0, 0, 0), 1)

                    # Display the Tile value if it is not 0 (empty).
                    if self.tiles[i][j].value != 0:
                        self.tiles[i][j].display(
                            self.tiles[i][j].value, (21 + j * 60, 16 + i * 60), (0, 0, 0)
                        )
            # Draw a horizontal line at the bottom of the board.
            pygame.draw.line(
                self.window,
                (0, 0, 0),
                (0, (i + 1) // 3 * 180),
                (540, (i + 1) // 3 * 180),
                4,
            )