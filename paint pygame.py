#paint pygame

import pygame

pygame.init()
sc = pygame.display.set_mode((960,540))
pygame.display.set_caption("Pygame paint")
sc.fill("white")

colors = ["black","green","blue","red","yellow","purple","orange"]
startingcolor = "black"
width = 4
class myline():
    global startingcolor
    global width
    def __init__(self,startpos,endpos):
        self.startpos = startpos
        self.endpos = endpos
        self.color = startingcolor
        self.width = width
        self.surface = sc
    def draw(self):
        self.line = pygame.draw.line(self.surface,self.color,self.startpos,self.endpos,self.width)
    def grow(self):
        global width
        self.width = self.width + 10
        #pygame.draw.line(self.surface,self.color,self.startpos,self.endpos,self.width)
    def shrink(self):
        global width
        self.width = self.width - 10
        #pygame.draw.line(self.surface,self.color,self.startpos,self.endpos,self.width)
    def next_color(self):
        global startingcolor
        ind = colors.index(startingcolor)
        startingcolor = colors[(ind+1) % len(colors)]
        self.line = pygame.draw.line(self.surface,self.color,self.startpos,self.endpos,self.width)
        
line = myline(0,0)
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
                line = myline(last_pos,new_pos)
                line.draw()
        if clicking == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    line.shrink()
        if clicking == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    line.grow()
        if clicking == False:
            if event.type == pygame.KEYDOWN:#to here doesnt work
                if event.key == pygame.K_c:
                    line.next_color()

    pygame.display.update()