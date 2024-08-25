#flappy bird

import pygame
from pygame.locals import *


WIDTH = 864
HEIGHT = 768


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")


flying = False
gap = 200
gameover = False
score = 0
pipe_success = False
clock = pygame.time.Clock()
fps = 60
pipe_freq = 1500
lastpipe = pygame.time.get_ticks() - pipe_freq

ground = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\ground.png")
background = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\background.png")
restart = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\restart.png")
pipe = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\pipe.png")



class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            image = pygame.image.load(f"C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\bird{i}.png")
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.click = False
    def update(self):
        global gameover,flying
        if gameover == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            flap_interval = 5
            self.counter += 1
            if self.counter == flap_interval:
                self.index += 1
                if self.index == 3:
                    self.index = 0
                self.image = self.images[self.index]
                self.counter = 0
        if flying == True:
            self.vel += 1
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < HEIGHT:
                self.rect.y += self.vel
            if self.rect.bottom > HEIGHT:
                #gameover = True
                self.rect.bottom = HEIGHT
                #flying = False

BirdGroup = pygame.sprite.Group()
red = Bird(WIDTH/3,HEIGHT/2)
BirdGroup.add(red)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    clock.tick(fps)
    sc.blit(background,(0,0))
    BirdGroup.draw(sc)
    BirdGroup.update()

    pygame.display.update()
