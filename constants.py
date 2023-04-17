GRID_SIZE = 100

MOVEMENT = 8

#grid creation (not auto generated)
grid = [
    ["tl","t","t","t","tr"],
    ["l","c","c","c","r"],
    ["l","c","cupboard","c","r"],
    ["l","c","c","c","r"],
    ["dl","d","d","d","dr"]
]

GRID_WIDTH = len(grid[0]) * GRID_SIZE
GRID_HEIGHT = len(grid) * GRID_SIZE

# window width and height
WIDTH = (len(grid[0]) * 2) * GRID_SIZE
HEIGHT = (len(grid)) * GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GAME_NAME = "Utopia"