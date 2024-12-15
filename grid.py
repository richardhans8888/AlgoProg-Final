import pygame
from colors import Colors

class Grid:
    def __init__(self):
        # Initializes the grid with a size of 20 rows by 10 columns.
        # Each cell is 30x30 pixels and starts as empty (value 0).
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        # Prints the grid to the console for debugging purposes.
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        # Checks if the given cell (row, column) is within the grid boundaries
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        # Checks if the given cell (row, column) is empty (value 0)
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        # Checks if a specific row is completely filled (no empty cells)
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        # Clears all cells in the specified row by setting them to 0 (empty)
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        # Moves the contents of a row down by the specified number of rows
        # This is used when rows above a cleared row need to shift down
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        # Clears all fully filled rows and shifts rows above them downward
        # Returns the number of rows that were cleared.
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):  # Start from the bottom row and move up
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        # Resets the entire grid, making all cells empty (value 0)
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        # Draws the grid on the screen using pygame.
        # Each cell is drawn with the appropriate color based on its value
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 11,  
                    row * self.cell_size + 11,   
                    self.cell_size - 1,          
                    self.cell_size - 1          
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)