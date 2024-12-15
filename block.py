from colors import Colors
import pygame
from position import Position

# The Block class represents a single Tetris block with its shape, position, and color.
class Block:
    def __init__(self, id):
        # Each block has an ID to represent its type (e.g., square, line, etc.).
        self.id = id
        
        # A dictionary to store how the block looks in different rotations.
        self.cells = {}
        
        # Each cell in the block is 30 pixels by 30 pixels.
        self.cell_size = 30

        # This tells the block how far down (rows) and to the right (columns) it has moved.
        self.row_offset = 0
        self.column_offset = 0

        # Tracks the block's current rotation state (0, 1, 2, etc.).
        self.rotation_state = 0

        # Gets the color for this block based on its ID.
        self.colors = Colors.get_cell_colors()

    # This function moves the block by a certain number of rows and columns.
    def move(self, rows, columns):
        # Add the number of rows and columns to the current position.
        self.row_offset += rows
        self.column_offset += columns

    # This function returns the current positions of all the block's cells on the grid.
    def get_cell_positions(self):
        # Get the block's shape for the current rotation state.
        tiles = self.cells[self.rotation_state]

        # A new list to store the positions of the cells after moving them.
        moved_tiles = []

        # Update each cell's position by adding the offsets.
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        
        return moved_tiles

    # This function rotates the block to the next state.
    def rotate(self):
        # Move to the next rotation state.
        self.rotation_state += 1

        # If the state goes beyond the last one, reset it to the first state (0).
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # This function undoes the last rotation if it was invalid.
    def undo_rotation(self):
        # Go back one rotation state.
        self.rotation_state -= 1

        # If the state becomes negative, go to the last state.
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # This function draws the block on the screen.
    def draw(self, screen, offset_x, offset_y):
        # Get the current positions of the block's cells.
        tiles = self.get_cell_positions()

        # Draw each cell of the block.
        for tile in tiles:
            # Calculate the position and size of the rectangle for the cell.
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,  
                offset_y + tile.row * self.cell_size,    
                self.cell_size - 1,                     
                self.cell_size - 1                     
            )
            
            # Draw the rectangle on the screen with the block's color.
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
