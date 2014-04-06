import pygame, sys
from pygame.locals import *

print pygame.ver

file_ball = "../resources/basket-ball.png"
file_paddle = "../resources/paddle.png"
file_back = "../resources/georgia.jpg"
file_cursor = "../resources/rocket-fly.png"

pygame.init()

screen = pygame.display.set_mode((900, 500), 0, 32)

ball_x, ball_y = 450, 250
ball_xvel, ball_yvel = 0, 0

player_y = 450
player_yvel = 0

opp_y = 450
opp_yvel = 0

img_ball = pygame.image.load(file_ball).convert_alpha()
img_paddle = pygame.image.load(file_paddle).convert()
img_back = pygame.image.load(file_back).convert()

img_cursor = pygame.image.load(file_cursor).convert_alpha()

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            if event.key == K_UP:
                player_yvel = -1
            elif event.key == K_DOWN:
                player_yvel = 1
        
        elif event.type == KEYUP:
            
            player_yvel= 0;
    
    screen.blit(img_back, (0, 0))
    
    screen.blit(img_ball, (ball_x, ball_y))
    screen.blit(img_paddle, (50, player_y))
    screen.blit(img_paddle, (850, opp_y))
    
    pygame.display.update()