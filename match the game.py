#match the game

import pygame
import random

WIDTH = 1200
HEIGHT = 765


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
sc.fill("white")

subwaysurfers_img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\subwaysurfers.png")
ludo_img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\ludo.png")
candycrush_img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\candycrush.jpg")
templerun_img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\templerun.png")

co_ordinates_array = [(355,150),(355,275),(355,400),(355,525)]
imgs = [subwaysurfers_img,ludo_img,candycrush_img,templerun_img]

for i in range(len(imgs)):
    coord_choice = random.choice(co_ordinates_array)
    co_ordinates_array.remove(coord_choice)
    sc.blit(imgs[i],coord_choice)

textfont = pygame.font.SysFont("Times New Roman",40)


subwaysurfers_txt = textfont.render("Subway Surfers",True,"Black")
ludo_txt = textfont.render("Ludo",True,"Black")
candycrush_txt = textfont.render("Candy Crush",True,"Black")
templerun_txt = textfont.render("Temple Run",True,"Black")

co_ordinates_array = [(700,175),(700,300),(700,425),(700,550)]
txts = [subwaysurfers_txt,ludo_txt,candycrush_txt,templerun_txt]

for i in range(len(txts)):
    coord_choice = random.choice(co_ordinates_array)
    co_ordinates_array.remove(coord_choice)
    sc.blit(txts[i],coord_choice)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(sc,"black",pos,10)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            newpos = pygame.mouse.get_pos()
            pygame.draw.circle(sc,"black",newpos,10)
            pygame.draw.line(sc,"black",pos,newpos,3)
            pygame.display.update()
    pygame.display.update()