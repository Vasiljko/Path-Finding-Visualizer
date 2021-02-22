from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from Util import *
from PathFinding import *
import sys


def main():
    sys.setrecursionlimit(5000)
    pygame.init()
    pygame.display.set_caption('Pathfinding Visualizer')

    tiles = get_initial()
    get_adjacent(tiles)
    buttons = render_buttons()

    input_text = "Start tile"
    prev_start_i, prev_start_j = -1, -1
    prev_end_i, prev_end_j = -1, -1

    holding = False
    clock = pygame.time.Clock()

    open = []
    closed = []

    queue = []
    stack = []

    running_a_search, running_bfs, running_dfs = False, False, False
    found_solution_a_search, found_solution_bfs, found_solution_dfs = False, False, False
    path_a_search, path_bfs, path_dfs = [], [], []
    still_finding_solution, printing_path = False, False
    start_tile, end_tile = None, None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if running_a_search:
            printing_path, running_a_search, still_finding_solution, found_solution_a_search, path_a_search = \
                RunASearch(tiles, start_tile, end_tile, open, closed, printing_path, running_a_search,
                           still_finding_solution, found_solution_a_search, path_a_search)

        elif running_dfs:
            printing_path, running_dfs, still_finding_solution, found_solution_dfs, path_dfs = \
                RunDFS(tiles, start_tile, end_tile, stack, printing_path, running_dfs, still_finding_solution,
                       found_solution_dfs, path_dfs)
        elif running_bfs:
            printing_path, running_bfs, still_finding_solution, found_solution_bfs, path_bfs = \
                RunBFS(tiles, start_tile, end_tile, queue, printing_path, running_bfs, still_finding_solution,
                       found_solution_bfs, path_bfs)
        else:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                j = y // SIZE
                i = x // SIZE

                if x >= GRID_SIZE:  # Cursor is on the side of buttons
                    for button in buttons:
                        if button.clicked(x, y) and holding == False:
                            input_text = button.text

                    if input_text == "":
                        continue

                    if input_text == "Clear" and holding == False:
                        clear_grid(tiles)
                        input_text = "Start tile"
                    elif input_text == "Run A*" and holding == False:
                        clearAllExceptInitial(tiles)
                        running_a_search, still_finding_solution, found_solution_a_search = True, True, False

                        start_tile, end_tile = FindInitialTiles(tiles)
                        open, closed = [start_tile], []

                        input_text = ""

                    elif input_text == "Run DFS" and holding == False:
                        clearAllExceptInitial(tiles)
                        running_dfs, still_finding_solution, found_solution_dfs = True, True, False

                        start_tile, end_tile = FindInitialTiles(tiles)
                        stack = [start_tile]

                        input_text = ""

                    elif input_text == "Run BFS" and holding == False:
                        clearAllExceptInitial(tiles)
                        running_bfs, still_finding_solution, found_solution_bfs = True, True, False

                        start_tile, end_tile = FindInitialTiles(tiles)
                        queue = [start_tile]

                        input_text = ""

                else:
                    if input_text == "Erase":
                        clearAllExceptInitial(tiles)
                        eraseTile(tiles[i][j])
                    elif input_text == "Set obstacles":
                        if not (tiles[i][j].start_tile or tiles[i][j].end_tile):  # If it's possible to put obstacle in given position
                            clearAllExceptInitial(tiles)
                            drawObstacle(tiles[i][j])
                    elif input_text == "Start tile":
                        if not (tiles[i][j].obstacle or tiles[i][j].end_tile):
                            clearAllExceptInitial(tiles)
                            prev_start_i, prev_start_j = drawStartTile(tiles, prev_start_i, prev_start_j, i, j)
                    elif input_text == "End tile":
                        if not (tiles[i][j].obstacle or tiles[i][j].start_tile):
                            clearAllExceptInitial(tiles)
                            prev_end_i, prev_end_j = drawEndTile(tiles, prev_end_i, prev_end_j, i, j)

                holding = True
            else:
                holding = False

        draw_buttons(buttons)
        draw_tiles(tiles)
        pygame.display.update()
        clock.tick(50)


if __name__ == '__main__':
    main()
