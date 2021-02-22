from Required import *


# Check if (x,y) is tile in grid
def inGrid(x, y):
    return 0<=x and x<GRID_SIZE//SIZE and 0<=y and y<GRID_SIZE//SIZE

# Generate grid
def get_initial():
    tiles = []
    for i in range(GRID_SIZE // SIZE):
        tiles.append([])
        for j in range(GRID_SIZE // SIZE):
            tiles[i].append(Tile(i, j, SIZE))
    return tiles

# Get adjacent tiles
def get_adjacent(tiles):
    for i in range(GRID_SIZE//SIZE):
        for j in range(GRID_SIZE//SIZE):
            if inGrid(i-1,j):
                tiles[i][j].adjacent.append(tiles[i-1][j])
            if inGrid(i+1,j):
                tiles[i][j].adjacent.append(tiles[i+1][j])
            if inGrid(i,j-1):
                tiles[i][j].adjacent.append(tiles[i][j-1])
            if inGrid(i,j+1):
                tiles[i][j].adjacent.append(tiles[i][j+1])

# Find starting and ending tile
def FindInitialTiles(tiles):
    starting_tile, ending_tile = None, None

    for tile_row in tiles:
        for tile in tile_row:
            if tile.start_tile == True:
                starting_tile = tile
            if tile.end_tile == True:
                ending_tile = tile

    return starting_tile, ending_tile

def draw_tiles(tiles):
    for tile_row in tiles:
        for tile in tile_row:
            tile.draw(win)

def clear_grid(tiles):
    for tile_row in tiles:
        for tile in tile_row:
            tile.reset(win)


def draw_buttons(buttons):
    for button in buttons:
        button.draw(win)

def render_buttons():
    font = pygame.font.SysFont('Corbel', 20, bold=True)

    buttons = []
    buttons.append(CustomButton('Start tile', 630, 50, 140, 40, font))
    buttons.append(CustomButton('End tile', 630, 100, 140, 40, font))
    buttons.append(CustomButton('Set obstacles', 630, 150, 140, 40, font))
    buttons.append(CustomButton('Erase', 630, 250, 140, 40, font))
    buttons.append(CustomButton('Clear', 630, 300, 140, 40, font))
    buttons.append(CustomButton('Run A*', 630, 400, 140, 40, font))
    buttons.append(CustomButton('Run BFS', 630, 450, 140, 40, font))
    buttons.append(CustomButton('Run DFS', 630, 500, 140, 40, font))

    return buttons


def drawObstacle(tile):
    tile.setObstacle()

def drawStartTile(tiles, prev_i, prev_j, i, j):
    if prev_i != -1:
        tiles[prev_i][prev_j].reset(win)
    tiles[i][j].setStartTile()
    return i, j

def drawEndTile(tiles, prev_i, prev_j, i, j):
    if prev_i != -1:
        tiles[prev_i][prev_j].reset(win)
    tiles[i][j].setEndTile()
    return i, j


def eraseTile(tile):
    tile.reset(win)

def clearAllExceptInitial(tiles):
    for tile_row in tiles:
        for tile in tile_row:
            if tile.start_tile:
                tile.visited = False
                tile.color = tile.START_COLOR
            elif tile.end_tile:
                tile.visited = False
                tile.color = tile.END_COLOR
            elif tile.obstacle:
                tile.visited = False
            else:
                eraseTile(tile)


def findPath(tiles, starting_tile, ending_tile):
    path = []
    tile = ending_tile
    while True:
        if tile == starting_tile:
            break
        path.append(tile)
        tile = tile.parent

    path.append(starting_tile)
    path = path[::-1]

    return path

def printPath(tile, starting_tile, ending_tile):
    tile.setAsPathTile()
    if tile == starting_tile or tile == ending_tile:
        tile.color = tile.DARK_PURPLE

