#paint pygame

import pygame
import random

pygame.init()
sc = pygame.display.set_mode((960,540))
pygame.display.set_caption("Pygame paint")
sc.fill("white")

colors = ["black","green","blue","red","yellow","purple","orange"]
startingcolor = "blue"
width = 4
        
clicking = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False
        elif event.type == pygame.MOUSEMOTION:
            new_pos = pygame.mouse.get_pos()
            if clicking == True:
                last_pos = new_pos
                new_pos = pygame.mouse.get_pos()
                pygame.draw.line(sc,startingcolor,last_pos,new_pos,width)
                pygame.display.update()
        if clicking == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    width = width - 10
                    pygame.display.update()
        if clicking == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    width = width + 10
                    pygame.display.update()
        if clicking == False:
            if event.type == pygame.KEYDOWN:#to here doesnt work
                if event.key == pygame.K_c:
                    print(startingcolor)
                    startingcolor = random.choice(colors)
                    pygame.display.update()

    pygame.display.update()