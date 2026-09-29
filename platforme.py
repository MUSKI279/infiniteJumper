import pygame
import random

WIDTH = 400
HEIGHT = 400


pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("spilprojekt")


class Background:
    def __init__(self, tileSize, backgroundColor, lineColor):

        self.tileSize = tileSize
        self.backgroundColor = backgroundColor
        self.lineColor = lineColor

        
    def draw_grid(self):

        screen.fill(self.backgroundColor)

        for x in range(0, WIDTH, self.tileSize):
            pygame.draw.line(screen, self.lineColor, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, self.tileSize):
            pygame.draw.line(screen, self.lineColor, (0, y), (WIDTH, y))

    def drawPlatform(self, platform):
            for x, y in platform.body:
                pygame.draw.rect(
                    screen, platform.color,
                    (x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize))

            



class Platform:

    def __init__(self, color):
        self.xStart = random.randint(1, 10)
        self.yStart = random.randint(1, 10)
        self.size = random.randint(1, 4)
        self.color = color
        self.body = [(self.xStart + i, self.yStart) for i in range(self.size)]
    
    


    
    
    
    




