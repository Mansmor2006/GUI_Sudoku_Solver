import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up grid parameters
rows, cols = 10, 10
pygame.init()

width, height = 500, 500


class Board:
    def __init__(self, window):
        """
        Initializes a Board object.

        Args:
            window: The Pygame window object.
        """
        
        
        # Create a 2D list of Tile objects to represent the Sudoku board.
        self.tiles = [[Tile(self.board[i][j], window, i * 60, j * 60) for j in range(9)]
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




class Tile:
    def __init__(self, value, window, x1, y1):
        """
        Initializes a Tile object.

        Args:
            value (int): The value to be displayed in the Tile.
            window (pygame.Surface): The surface to draw the Tile on.
            x1 (int): The x-coordinate of the top-left corner of the Tile.
            y1 (int): The y-coordinate of the top-left corner of the Tile.

        Attributes:
            value (int): The value to be displayed in the Tile.
            window (pygame.Surface): The surface to draw the Tile on.
            rect (pygame.Rect): The rectangular area of the Tile.
            selected (bool): Whether the Tile is currently selected.
            correct (bool): Whether the value in the Tile is correct.
            incorrect (bool): Whether the value in the Tile is incorrect.
        """

        self.value = value
        self.window = window
        self.rect = pygame.Rect(x1, y1, 60, 60)
        self.selected = False
        self.correct = False
        self.incorrect = False





    
# Main game loop
def main():
    window = pygame.display.set_mode((540, 690)) 
    window.fill(WHITE)
    pygame.display.set_caption("Sudoku Puzzle")
    

    


    # Set up the display
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
if __name__ == "__main__":
    main()