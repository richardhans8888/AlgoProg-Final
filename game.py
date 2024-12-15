from grid import Grid
from blocks import *
import random
import pygame

class Game: # The Game class is the main controller of the Tetris game.
	def __init__(self):
		self.grid = Grid()		# Initialize the game grid.
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

		# The block currently falling and the next block to appear
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()

		# Tracks if the game is over.
		self.game_over = False

		# Keeps the player's score.
		self.score = 0

		# Load sounds for game events.
		self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
		
        # Load and start background music.
		pygame.mixer.music.load("Sounds/music.ogg")
		pygame.mixer.music.play(-1)


	# Updates the score based on the number of rows cleared and points from moving down.
	def update_score(self, lines_cleared, move_down_points):
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points # Add points for moving the block down.


    # Returns a random block and removes it from the available blocks.
	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks) 
		self.blocks.remove(block)
		return block
	
	# Moves the block one step to the left.
	def move_left(self):
		self.current_block.move(0, -1)  
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	# Moves the block one step to the right.
	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False: 
			self.current_block.move(0, -1) 

	# Moves the block one step down.
	def move_down(self):
		self.current_block.move(1, 0)  
		if self.block_inside() == False or self.block_fits() == False: 
			self.current_block.move(-1, 0)  
			self.lock_block() 


	# Locks the current block in the grid and prepares the next block.
	def lock_block(self):
		# Add the block's cells to the grid.
		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id

		# Update to the next block.
		self.current_block = self.next_block
		self.next_block = self.get_random_block()

		# Clear any full rows and update the score.
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.clear_sound.play() # Play sound if rows are cleared.
			self.update_score(rows_cleared, 0)

		# If the new block doesn't fit, the game is over.	
		if self.block_fits() == False:
			self.game_over = True

	# Resets the game state to start a new game.
	def reset(self):
		self.grid.reset()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0

    # Checks if the current block fits in the grid.
	def block_fits(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False 
		return True

	# Rotates the current block.
	def rotate(self):
		self.current_block.rotate()  
		if self.block_inside() == False or self.block_fits() == False: 
			self.current_block.undo_rotation() 
		else:
			self.rotate_sound.play()  


	# Checks if the block is inside the grid boundaries.
	def block_inside(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False 
		return True  

    # Draws the game grid, current block, and next block.
	def draw(self, screen):
		self.grid.draw(screen)  
		self.current_block.draw(screen, 11, 11)

        # Position the next block preview in the correct spot based on its type.
		if self.next_block.id == 3: 
			self.next_block.draw(screen, 255, 290)
		elif self.next_block.id == 4: 
			self.next_block.draw(screen, 255, 280)
		else: 
			self.next_block.draw(screen, 270, 270)