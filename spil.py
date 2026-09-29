import pygame
from platforme import *



WIDTH = 400
HEIGHT = 400


TILE_SIZE = 40
BACKGROUND_COLOR = "black"
LINE_COLOR = "dark green"

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("spilprojekt")


background = Background(20, BACKGROUND_COLOR, LINE_COLOR)

platform1 = Platform("purple")
platform2 = Platform("green")
platform3 = Platform("yellow")


gameRunning = True

while gameRunning:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameRunning = False

    #background.draw_grid()
    background.drawPlatform(platform1)
    background.drawPlatform(platform2)
    background.drawPlatform(platform3)


    
    pygame.display.flip() 

pygame.quit()  




