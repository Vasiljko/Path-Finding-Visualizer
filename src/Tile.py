import pygame

class Tile:
    GRAY, BLACK, WHITE                      = (150, 150, 150), (50, 50, 50), (255,255,255)
    START_COLOR, END_COLOR, NEIGHBOUR_COLOR = (255, 121, 25), (3, 128, 36), (186, 217, 255)
    CURRENT_COLOR, DARK_BLUE                = (0, 70, 156), (0, 3, 69)
    PATH_COLOR, DARK_PURPLE                 = (138, 48, 255), (72, 24, 133)

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.color = self.GRAY
        self.border_size  = 1       #If border_size = 0 then whole tile is filled with some color

        self.obstacle = False
        self.start_tile = False
        self.end_tile = False

        self.visited = False
        self.adjacent = []
        self.parent = None

        self.f = 0
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def draw(self, win):
        rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
        pygame.draw.rect(win, self.color, rect, self.border_size)

    def reset(self, win):
        self.color = self.GRAY
        self.border_size = 1

        self.obstacle = False
        self.start_tile = False
        self.end_tile = False
        self.visited = False

        rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
        pygame.draw.rect(win, self.WHITE, rect)

    def setObstacle(self):
        self.obstacle = True
        self.border_size = 0
        self.color = self.BLACK

    def setStartTile(self):
        self.start_tile = True
        self.border_size =  0
        self.color = self.START_COLOR

    def setEndTile(self):
        self.end_tile = True
        self.border_size = 0
        self.color = self.END_COLOR

    def setAsNextTile(self):
        self.border_size = 0
        self.color = self.NEIGHBOUR_COLOR

    def setAsPassedTile(self):
        self.border_size = 0
        self.color = self.CURRENT_COLOR
        self.visited = True

    def setAsPathTile(self):
        self.border_size = 0
        self.color = self.PATH_COLOR
