import pygame
import time
import random

WIDTH = 800
HEIGHT = 800


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chase game")

clock = pygame.time.Clock()


class Block(pygame.sprite.Sprite):
    def __init__(self,width,height,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

block_list = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()

for i in range(30):
    block = Block(15,15,"black")
    block.rect.x = random.randint(0,WIDTH)
    block.rect.y = random.randint(0,HEIGHT)
    block_list.add(block)
    all_blocks.add(block)

player = Block(15,15,"red")
player.rect.x = WIDTH/2
player.rect.y = HEIGHT/2
all_blocks.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill("white")
    position = pygame.mouse.get_pos()
    player.rect.x = position[0]
    player.rect.y = position[1]
    collide = pygame.sprite.spritecollide(player,block_list,True)
    #red_block.draw(sc)
    all_blocks.draw(sc)
    pygame.display.flip()
    clock.tick(60)