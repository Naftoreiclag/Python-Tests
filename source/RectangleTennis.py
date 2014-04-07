import pygame, sys
from pygame.locals import *

import math

print pygame.ver

file_ball = "../resources/basket-ball.png"
file_paddle = "../resources/paddle.png"
file_back = "../resources/georgia.jpg"
file_cursor = "../resources/rocket-fly.png"

pygame.init()

scr_width = 900
scr_height = 500

screen = pygame.display.set_mode((scr_width, scr_height), 0, 32)

ball_x, ball_y = scr_width / 2, scr_height / 2
ball_xvel, ball_yvel = 1, 1

player_x, player_y = 0 + 50, scr_height / 2
player_yvel = 0

opp_x, opp_y = scr_width - 50, scr_height / 2
opp_yvel = 0

img_ball = pygame.image.load(file_ball).convert_alpha()
img_paddle = pygame.image.load(file_paddle).convert()
img_back = pygame.image.load(file_back).convert()

img_cursor = pygame.image.load(file_cursor).convert_alpha()

paddle_hwidth = img_paddle.get_size()[0] / 2.0
paddle_hheight = img_paddle.get_size()[1] / 2.0

paddle_maxspd = 0.6

ball_hwidth = img_ball.get_size()[0] / 2.0
ball_hheight = img_ball.get_size()[1] / 2.0

ball_maxspd = 0.5

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            if event.key == K_UP:
                player_yvel = -paddle_maxspd
            elif event.key == K_DOWN:
                player_yvel = paddle_maxspd
        
        elif event.type == KEYUP:
            
            player_yvel= 0;
    
    screen.blit(img_back, (0, 0))
    
    player_y += player_yvel
    opp_y += opp_yvel
    
    ball_x += ball_xvel
    ball_y += ball_yvel
    
    if(ball_y < 0 + ball_hheight or ball_y > scr_height - ball_hheight): ball_yvel = -ball_yvel
    
    if(ball_x < 0 - ball_hwidth or ball_x > scr_width + ball_hwidth):
        ball_x, ball_y = scr_width / 2, scr_height / 2
        ball_xvel = -ball_xvel
    
    if(ball_x - ball_hwidth == player_x + paddle_hwidth and ball_y > player_y - paddle_hheight and ball_y < player_y + paddle_hheight): ball_xvel = -ball_xvel
    if(ball_x + ball_hwidth == opp_x - paddle_hwidth and ball_y > opp_y - paddle_hheight and ball_y < opp_y + paddle_hheight): ball_xvel = -ball_xvel
    
    if(ball_x > scr_width / 2):
        opp_yvel = math.copysign(paddle_maxspd, ball_y - opp_y)
    else:
        opp_yvel = 0
    
    screen.blit(img_ball, (ball_x - ball_hwidth, ball_y - ball_hheight))
    screen.blit(img_paddle, (50 - paddle_hwidth, player_y - paddle_hheight))
    screen.blit(img_paddle, (850 - paddle_hwidth, opp_y - paddle_hheight))
    
    pygame.display.update()
