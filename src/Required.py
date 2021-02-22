import pygame
from Tile import Tile
from CustomButton import CustomButton

pygame.init()

SIZE, WIN_HEIGHT, WIN_WIDTH, GRID_SIZE = 15, 600, 800, 600
WHITE, GRAY = (255,255,255), (54,54,54)
win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
win.fill(WHITE)
