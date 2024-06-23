import pygame
import time

WIDTH = 600
HEIGHT = 600


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pygame Image editor")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\Backgroundone.jpg")
    img = pygame.transform.scale(img,(WIDTH,HEIGHT))
    font = pygame.font.SysFont("Times New Roman",50)
    text = font.render("Happy Birthday",True,"red")
    sc.fill("white")
    sc.blit(img,(0,0))
    sc.blit(text,(20,20))
    pygame.display.update()
    time.sleep(2)
    img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\Backgroundtwo.jpg")
    img = pygame.transform.scale(img,(WIDTH,HEIGHT))
    font = pygame.font.SysFont("Times New Roman",50)
    text1 = font.render("Happy",True,"red")
    text2 = font.render("Birthday",True,"red")
    sc.fill("white")
    sc.blit(img,(0,0))
    sc.blit(text1,(160,200))
    sc.blit(text2,(160,260))
    pygame.display.update()
    time.sleep(2)
    img = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\Backgroundthree.jpg")
    img = pygame.transform.scale(img,(WIDTH,HEIGHT))
    font = pygame.font.SysFont("Times New Roman",50)
    text = font.render("Happy Birthday",True,"red")
    sc.fill("white")
    sc.blit(img,(0,0))
    sc.blit(text,(160,520))
    pygame.display.update()
    time.sleep(2)