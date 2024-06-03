#rectangles pygame

import pygame

pygame.init()
sc = pygame.display.set_mode((960,540))
pygame.display.set_caption("Pygame rectangles")


class rectangles():
    def __init__(self,color,dimensions):
        self.color = color
        self.dimensions = dimensions
        self.surface = sc
    def draw(self):
        self.rect = pygame.draw.rect(self.surface,self.color,self.dimensions)

red_rect = rectangles("red",(480,270,20,20))
yellow_rect = rectangles("yellow",(100,100,200,200))
blue_rect = rectangles("blue",(800,400,100,80))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill("white")
    red_rect.draw()
    yellow_rect.draw()
    blue_rect.draw()
    pygame.display.update()