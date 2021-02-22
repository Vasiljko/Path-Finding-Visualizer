import pygame
pygame.init()
class CustomButton:
    COLOR = (255,255,255)
    BG    = (54,54,54)

    def __init__(self, text, x, y, widht, height, font):
        self.text = text
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.font = font

    def draw(self, win):
        text = self.font.render(self.text, True, self.COLOR)
        pygame.draw.rect(win, self.BG, [self.x, self.y, self.width, self.height])
        win.blit(text, (self.x + 14, self.y + 10))

    def clicked(self, pos_x, pos_y):
        return self.x <= pos_x and pos_x <= self.x+self.width and self.y <= pos_y and pos_y <= self.y+self.height