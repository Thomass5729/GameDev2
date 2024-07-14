#rocket moving

import pygame


WIDTH = 1200
HEIGHT = 800


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Color sprite practice")






class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\rocket.png")
        self.rect = self.image.get_rect()
    def update(self,pressed_keys):
        if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and self.rect.top > 0:
            self.rect.move_ip(0,-15)
        if (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0,15)
        if (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and self.rect.right < WIDTH:
            self.rect.move_ip(15,0)
        if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.move_ip(-15,0)

rocketgroup = pygame.sprite.Group()
rocket = Rocket()
rocketgroup.add(rocket)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()
    rocket.update(pressed_keys)
    sc.blit(pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\space.png"),(0,0))
    rocketgroup.draw(sc)
    pygame.display.update()
