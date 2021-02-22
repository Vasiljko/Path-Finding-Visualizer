from Required import *
from Util import printPath
from Util import findPath



# -----------------------A* Star Search Algorithm----------------------------#

def calculateDistance(start, end):
    return (start.x - end.x) ** 2 + (start.y - end.y) ** 2


# Return ( still running, found solution, open, closed )
def AStarSearch(tiles, starting_tile, ending_tile, open, closed):
    if ending_tile in closed:
        return False, True, open, closed
    if len(open) == 0:
        return False, False, open, closed

    current = None
    index = -1
    for i, tile in enumerate(open):
        if not current or tile.f < current.f or tile == ending_tile:
            current = tile
            index = i

    open.pop(index)
    closed.append(current)
    current.setAsPassedTile()

    if current == starting_tile:
        current.color = current.DARK_BLUE
    elif current == ending_tile:
        current.color = current.DARK_BLUE

    for neighbour in current.adjacent:

        if neighbour.obstacle or neighbour in closed:
            continue
        elif not (neighbour in open):
            neighbour.g = current.g + 1
            neighbour.h = calculateDistance(neighbour, ending_tile)
            neighbour.f = neighbour.g + neighbour.h
            neighbour.parent = current
            neighbour.setAsNextTile()

            open.append(neighbour)
        else:
            for tile in open:
                if tile == neighbour:
                    if neighbour.g < tile.g:
                        tile.g = neighbour.g
                        tile.f = tile.g + tile.h

    return True, False, open, closed


def RunASearch(tiles, start_tile, end_tile, open, closed, printing_path, running_a_search, still_finding_solution,
               found_solution_a_search, path_a_search):
    if not start_tile or not end_tile:
        running_a_search = False
        return printing_path, running_a_search, still_finding_solution, found_solution_a_search, path_a_search

    if still_finding_solution:
        still_finding_solution, found_solution_a_search, open, closed = AStarSearch(tiles, start_tile, end_tile, open,
                                                                                    closed)
    else:
        if found_solution_a_search:
            if len(path_a_search) == 0 and printing_path == False:
                path_a_search = findPath(tiles, start_tile, end_tile)
                printing_path = True
            elif len(path_a_search) > 0:
                printPath(path_a_search[0], start_tile, end_tile)
                path_a_search.pop(0)
            else:
                printing_path = False
                running_a_search = False
        else:
            printing_path = False
            running_a_search = False
    return printing_path, running_a_search, still_finding_solution, found_solution_a_search, path_a_search



# --------------------------------DFS------------------------------------#

# Return ( still running, found solution, stack )
def DFS(starting_tile, ending_tile, stack):

    if len(stack) == 0:
        return False, False, stack

    current = stack.pop()
    if not current.visited:
        current.setAsPassedTile()

    if current == starting_tile:
        current.color = current.DARK_BLUE
    elif current == ending_tile:
        current.color = current.DARK_BLUE

        return False, True, stack

    for neighbour in current.adjacent:
        if not neighbour.visited and not neighbour.obstacle:
            neighbour.parent = current
            stack.append(neighbour)

    return True, False, stack


def RunDFS(tiles, start_tile, end_tile, stack, printing_path, running_dfs, still_finding_solution, found_solution_dfs, path_dfs):
    if not start_tile or not end_tile:
        running_dfs = False
        return printing_path, running_dfs, still_finding_solution, found_solution_dfs, path_dfs

    if still_finding_solution:
        still_finding_solution, found_solution_dfs, stack = DFS(start_tile, end_tile, stack)
    else:
        if found_solution_dfs:
            if len(path_dfs) == 0 and printing_path == False:
                path_dfs = findPath(tiles, start_tile, end_tile)
                printing_path = True
            elif len(path_dfs) > 0:
                printPath(path_dfs[0], start_tile, end_tile)
                path_dfs.pop(0)
                pygame.time.delay(20)
            else:
                printing_path = False
                running_dfs = False
        else:
            printing_path = False
            running_dfs = False
    return printing_path, running_dfs, still_finding_solution, found_solution_dfs, path_dfs



# -----------------------------------BFS-----------------------------------------#

# Return ( still running, found solution, queue)
def BFS(tiles, starting_tile, ending_tile, queue):
    if len(queue) == 0:
        return False, False, queue
    current = queue.pop(0)

    if current.visited:
        return True, False, queue

    if current == ending_tile:
        current.color = current.DARK_BLUE
        return False, True, queue

    current.setAsPassedTile()
    if current == starting_tile:
        current.color = current.DARK_BLUE

    for neighbour in current.adjacent:
        if (not neighbour.visited) and (not neighbour.obstacle):
            neighbour.setAsNextTile()
            neighbour.parent = current

            queue.append(neighbour)

    return True, False, queue


def RunBFS(tiles, start_tile, end_tile, queue, printing_path, running_bfs, still_finding_solution, found_solution_bfs,
           path_bfs):
    if not start_tile or not end_tile:
        running_bfs = False
        return printing_path, running_bfs, still_finding_solution, found_solution_bfs, path_bfs

    if still_finding_solution:
        still_finding_solution, found_solution_bfs, queue = BFS(tiles, start_tile, end_tile, queue)
    else:
        if found_solution_bfs:
            if len(path_bfs) == 0 and printing_path == False:
                path_bfs = findPath(tiles, start_tile, end_tile)
                printing_path = True
            elif len(path_bfs) > 0:
                printPath(path_bfs[0], start_tile, end_tile)
                path_bfs.pop(0)
                pygame.time.delay(20)
            else:
                printing_path = False
                running_bfs = False
        else:
            printing_path = False
            running_bfs = False
    return printing_path, running_bfs, still_finding_solution, found_solution_bfs, path_bfs
