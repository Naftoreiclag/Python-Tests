import pygame, sys
from pygame.locals import *

print pygame.ver

foo = "../resources/hail-damage.jpg"
bar = "../resources/rocket-fly.png"

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)

background = pygame.image.load(foo).convert()
cursor = pygame.image.load(bar).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background, (0, 0))
    
    x, y = pygame.mouse.get_pos()
    
    screen.blit(cursor, (x, y))
    
    pygame.display.update()