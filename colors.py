
# The Colors class is used to define and manage the color codes for the Tetris game.

class Colors:
	dark_grey = (26, 31, 40) #RGB Colors
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)


    # A class method to return a list of colors for Tetris blocks.
    # The index in the list corresponds to the block's ID.
	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
	# Return a list of colors specifically for Tetris blocks.
    # The order in this list matches the IDs of the blocks (e.g., 1 = green, 2 = red, etc.).