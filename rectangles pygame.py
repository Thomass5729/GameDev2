#rectangles pygame

import pygame

pygame.init()
sc = pygame.display.set_mode((960,540))
pygame.display.set_caption("Pygame rectagles")
sc.fill("white")

class circ():
    def __init__(self,color,centre,radius):
        self.color = color
        self.centre = centre
        self.radius = radius
        self.surface = sc
    def draw(self):
        self.rect = pygame.draw.circle(self.surface,self.color,self.centre,self.radius)
    def grow(self):
        self.radius+=10
        self.rect = pygame.draw.circle(self.surface,self.color,self.centre,self.radius)

red_circle = circ("red",(480,270),20)
yellow_circle = circ("yellow",(100,100),200)
blue_circle = circ("blue",(800,400),80)


while True:
    red_circle.draw()
    yellow_circle.draw()
    blue_circle.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           pass 
        elif event.type == pygame.MOUSEBUTTONUP:
            red_circle.grow()
            yellow_circle.grow()
            blue_circle.grow()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            pink_circle = circ("pink",(mouse_pos),5)
            pink_circle.draw()
    pygame.display.update()
