import pygame, sys
from pygame.locals import *

print pygame.ver

foo = "../resources/hail-damage.jpg"
bar = "../resources/rocket-fly.png"

pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

background = pygame.image.load(foo).convert()
cursor = pygame.image.load(bar).convert_alpha()

x,y = 0,0
movex, movey = 0,0

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            if event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = 1
            elif event.key == K_LEFT:
                movex = -1
            elif event.key == K_RIGHT:
                movex = 1
        
        elif event.type == KEYUP:
            
            if event.key == K_UP or event.key == K_DOWN:
                movey = 0
            elif event.key == K_LEFT or event.key == K_RIGHT:
                movex = 0
    
    screen.blit(background, (0, 0))
    
    x += movex / 20.0
    y += movey / 20.0
    
    screen.blit(cursor, (x, y))
    
    pygame.display.update()