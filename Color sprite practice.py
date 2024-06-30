import pygame
import random

WIDTH = 800
HEIGHT = 800


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Color sprite practice")


class clickable_sprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,ret):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ret = ret
    def update(self,events):
        for i in events:
            if i.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(i.pos):
                    self.ret()
def click():
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    rectangle.image.fill((r,g,b))
                    

rectangle = clickable_sprite(pygame.Surface((100,100)),400,400,click)

group = pygame.sprite.GroupSingle(rectangle)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    group.update(events)
    sc.fill("white")
    group.draw(sc)
    pygame.display.update()