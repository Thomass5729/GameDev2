#space invaders competitive game

import pygame


WIDTH = 1200
HEIGHT = 800


pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Color sprite practice")

border = pygame.Rect(585,0,30,800)
bullet_speed = 2
player_speed = 1
ship_wid = 50
ship_hei = 50
ye_health = 10
or_health = 10
winner = ""
gameover = False
font = pygame.font.SysFont("Times New Roman",50)
game_over_font = pygame.font.SysFont("Times New Roman",80)

ye_bullets = []
or_bullets = []

ye_ship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\Spaceship_Ye.png"),(ship_wid,ship_hei)),90)
or_ship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\Spaceship_Or.png"),(ship_wid,ship_hei)),270)
background = pygame.transform.scale(pygame.image.load("C:\\Users\\Thomas\\Documents\\Coding\\GameDev2\\images\\space.png"),(WIDTH,HEIGHT))

yellow = pygame.Rect(20,375,ship_wid,ship_hei)
orange = pygame.Rect(1130,375,ship_wid,ship_hei)

def draw():
    global yellow
    global orange
    sc.blit(background,(0,0))
    pygame.draw.rect(sc,"black",border)
    ye_text = font.render(f"Health: {ye_health}",True,"white")
    or_text = font.render(f"Health: {or_health}",True,"white")
    game_over_text1 = game_over_font.render("Game over!",True,"White")
    game_over_text2 = game_over_font.render(f"The winner is {winner}",True,"White")
    sc.blit(ye_text,(20,20))
    sc.blit(or_text,(965,20))
    sc.blit(ye_ship,(yellow.x,yellow.y))
    sc.blit(or_ship,(orange.x,orange.y))
    if gameover == True:
        sc.blit(background,(0,0))
        sc.blit(game_over_text1,(250,300))
        sc.blit(game_over_text2,(150,450))
    for bullet in ye_bullets:
        pygame.draw.rect(sc,"Yellow",bullet)
    for bullet in or_bullets:
        pygame.draw.rect(sc,"Orange",bullet)

def movement_ye(keys_pressed):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= player_speed
    if keys_pressed[pygame.K_s] and yellow.y < HEIGHT-ship_hei:
        yellow.y += player_speed
    if keys_pressed[pygame.K_d] and yellow.x < 585 - ship_wid:
        yellow.x += player_speed
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= player_speed

def movement_or(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and orange.x > 615:
        orange.x -= player_speed
    if keys_pressed[pygame.K_DOWN] and orange.y < HEIGHT-ship_hei:
        orange.y += player_speed
    if keys_pressed[pygame.K_RIGHT] and orange.x < WIDTH-ship_wid:
        orange.x += player_speed
    if keys_pressed[pygame.K_UP] and orange.y > 0:
        orange.y -= player_speed

def movement_bullet(ye_bullets,or_bullets):
    global or_health,ye_health,bullet_speed,orange,yellow
    for bullet in ye_bullets:
        bullet.x += bullet_speed
        if orange.colliderect(bullet):
            ye_bullets.remove(bullet)
            or_health -= 1
        elif bullet.x > WIDTH:
            ye_bullets.remove(bullet)
    for bullet in or_bullets:
        bullet.x -= bullet_speed
        if yellow.colliderect(bullet):
            or_bullets.remove(bullet)
            ye_health -= 1
        elif bullet.x < 0:
            or_bullets.remove(bullet)

def gameover_func():
    global ye_health,or_health,gameover,winner
    if ye_health == 0:
        winner = "orange"
        gameover = True
    elif or_health == 0:
        winner = "yellow"
        gameover = True
    



while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(yellow.x+(ship_wid//2),yellow.y+(ship_hei//2)-1,10,5)
                ye_bullets.append(bullet)
            if event.key == pygame.K_RCTRL:
                bullet = pygame.Rect(orange.x+(ship_wid//2),orange.y+(ship_hei//2)-1,10,5)
                or_bullets.append(bullet)
    draw()
    gameover_func()
    movement_bullet(ye_bullets,or_bullets)
    keys_pressed = pygame.key.get_pressed()
    movement_ye(keys_pressed)
    movement_or(keys_pressed)
    pygame.display.update()
