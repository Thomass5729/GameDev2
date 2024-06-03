#PYGAME flappy ball


import time
import pygame

pygame.init()
sc = pygame.display.set_mode((960,540))
pygame.display.set_caption("Flappy ball")
ball = pygame.draw.circle(surface = sc,color = "red",center = [480,270], radius = 15)
speed = [1,1]

framerate = 256

while True:
    time.sleep(1/framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill("black")
    ball = ball.move(speed)
    if ball.left <= 0 or ball.right >= 960:
        speed[0] = (-speed[0])
    if ball.top <= 0 or ball.bottom >= 540:
        speed[1] = (-speed[1])
    ball = pygame.draw.circle(surface = sc,color = "red",center = ball.center, radius = 15)



    pygame.display.update()