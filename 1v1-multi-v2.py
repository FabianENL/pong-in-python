import pygame
import numpy as np
import random
import os
pygame.init()
locatie = os.getcwd()

print("Made by Fabian Eppens | _Fabian_#4035. if you found bugs dm me on Discord!")

size = width,height = 800,600
color = (0,0,0)
vel = [2,2]
title = "Pong in python"

points1 = 0
points2 = 0
speed = 1

randomN = random.randrange(0,2)
if randomN == 0:
    ball_left = False
    ballposx = 1
    ballposy = random.randrange(0, 2)

    if ballposy == 0:
        ballposy = -1
    if ballposy == 1:
        ballposy = 1
        
    ballpostemp = ballposx, ballposy
    ballpos = ballpostemp

if randomN == 1:
    ball_left = True
    ballposx = -1
    ballposy = random.randrange(0, 2)

    if ballposy == 0:
        ballposy = -1
    if ballposy == 1:
        ballposy = 1
    ballpostemp = ballposx, ballposy
    ballpos = ballpostemp


pos = 0,0
pos2 = 0,0

window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

player1 = pygame.image.load("sprites/square.png")
playerRect1 = player1.get_rect()
playerRect1.center = (18,300)
postemp = 18,300

player2 = pygame.image.load("sprites/square.png")
playerRect2 = player1.get_rect()
playerRect2.center = (782,300)
postemp2 = 782,300


wall = pygame.image.load("sprites/wall.png")
wallRect = wall.get_rect()

wall2 = pygame.image.load("sprites/wall.png")
wallRect2 = wall.get_rect()
wallRect2 = wallRect2.move(790,0)

ball = pygame.image.load("sprites/ball.png")
ballRect = ball.get_rect()
ballRect = ballRect.move(400,300)

middlewall = pygame.image.load("sprites/middle_wall.png")
middlewallRect = middlewall.get_rect()
middlewallRect = middlewallRect.move(395, 0)

walltop = pygame.image.load("sprites/wall_top.png")
walltopRect = walltop.get_rect()
walltopRect = walltopRect.move(0, 590)

walltop2 = pygame.image.load("sprites/wall_top.png")
walltopRect2 = walltop2.get_rect()
walltopRect2 = walltopRect2.move(0, 0)




        


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            os.system('cd ' + str(locatie) + ' && python main.py')
            exit()
            
    #Reset the pos 
    

    
    pygame.time.delay(1)
    ads = pygame.event.get()
    #Handle Arrow Key event
    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP]:
        if keys[pygame.K_DOWN] != True:
            if postemp2 > (782,74):
                pos2 = 0,-2
                x, y = postemp2
                y = y - 2
                postemp2 = x,y

    if keys[pygame.K_DOWN]:
        if keys[pygame.K_UP] != True:
            if postemp2 < (782,526): 
                pos2 = 0,2
                x, y = postemp2
                y = y + 2
                postemp2 = x,y

    if keys[pygame.K_w]:
        if keys[pygame.K_s] != True:
            if postemp > (18,74):
                pos = 0,-2
                x, y = postemp
                y = y - 2
                postemp = x,y

    if keys[pygame.K_s]:
        if keys[pygame.K_w] != True:
            if postemp < (18,526):  
                pos = 0,2
                x, y = postemp
                y = y + 2
                postemp = x,y


    #Break the loop when ESCAPE is pressed
    if keys[pygame.K_ESCAPE]:
        run = False
        exit()
    
    collide = ballRect.colliderect(playerRect1)
    collide2 = ballRect.colliderect(playerRect2)
    collide3 = ballRect.colliderect(walltopRect)
    collide4 = ballRect.colliderect(walltopRect2)
    collide5 = ballRect.colliderect(wallRect)
    collide6 = ballRect.colliderect(wallRect2)

    if collide5 == True:
        points2 = points2+1
        playerRect1.center = (18,300)
        playerRect2.center = (782,300)
        ballRect.center = (400,300)
        postemp = (18,300)
        postemp2 = (782, 300)
        speed = 1
        randomN = random.randrange(0,2)
        if randomN == 0:
            ball_left = False
            ballposx = 1
            ballposy = random.randrange(0, 2)

            if ballposy == 0:
                ballposy = -1
            if ballposy == 1:
                ballposy = 1
                
            ballpostemp = ballposx, ballposy
            ballpos = ballpostemp

        if randomN == 1:
            ball_left = True
            ballposx = -1
            ballposy = random.randrange(0, 2)

            if ballposy == 0:
                ballposy = -1
            if ballposy == 1:
                ballposy = 1
            ballpostemp = ballposx, ballposy
            ballpos = ballpostemp

    if collide6 == True:
        points1 = points1+1
        playerRect1.center = (18,300)
        playerRect2.center = (782,300)
        ballRect.center = (400,300)
        postemp = (18,300)
        postemp2 = (782, 300)
        speed = 1
        randomN = random.randrange(0,2)
        if randomN == 0:
            ball_left = False
            ballposx = 1
            ballposy = random.randrange(0, 2)

            if ballposy == 0:
                ballposy = -1
            if ballposy == 1:
                ballposy = 1
                
            ballpostemp = ballposx, ballposy
            ballpos = ballpostemp

        if randomN == 1:
            ball_left = True
            ballposx = -1
            ballposy = random.randrange(0, 2)

            if ballposy == 0:
                ballposy = -1
            if ballposy == 1:
                ballposy = 1
            ballpostemp = ballposx, ballposy
            ballpos = ballpostemp

    
        
    if collide == False:
        if collide2 == False:
            if collide4 == False:
                if collide3 == False:
                    if ballpostemp == (speed,speed):
                        ballpostempx, ballpostempy = ballpostemp
                        ballpostemp = (speed),(speed)
                        ballpos = ballpostemp

                    if ballpostemp == (-speed,-speed):
                        ballpostempx, ballpostempy = ballpostemp
                        ballpostemp = (-speed),(-speed)
                        ballpos = ballpostemp

                    if ballpostemp == (speed,-speed):
                        ballpostempx, ballpostempy = ballpostemp
                        ballpostemp = (speed),(-speed)
                        ballpos = ballpostemp

                    if ballpostemp == (-speed,speed):
                        ballpostempx, ballpostempy = ballpostemp
                        ballpostemp = (-speed),(speed)
                        ballpos = ballpostemp

                    ballpos = ballpostemp
    
    

    if ball_left == True:      
        if collide == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,-speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = speed,speed

        if collide2 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = speed,speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed

        if collide3 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = speed,speed
            if ballpostemp == (-speed,speed):
                ballpos = -speed,-speed
        
        if collide4 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = speed,speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = -speed,-speed


    if ball_left == False:      
        if collide == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,-speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = speed,speed

        if collide2 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,-speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = speed,speed

        if collide3 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = speed,speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = -speed,-speed
        
        if collide4 == True:
            if ballpostemp == (speed,speed):
                speed = speed + 0.1
                ballpos = speed,-speed
            if ballpostemp == (-speed,-speed):
                speed = speed + 0.1
                ballpos = -speed,speed
            if ballpostemp == (speed,-speed):
                speed = speed + 0.1
                ballpos = speed,speed
            if ballpostemp == (-speed,speed):
                speed = speed + 0.1
                ballpos = -speed,-speed

    #Move the rectangle
    playerRect1 = playerRect1.move(pos)
    playerRect2 = playerRect2.move(pos2)
    ballRect = ballRect.move(ballpos)

    if collide == True:
        ball_left = False
    if collide2 == True:
        ball_left = True
    
    window.fill(color)
    window.blit(middlewall, middlewallRect)
    window.blit(player1,playerRect1)
    window.blit(wall,wallRect)
    window.blit(wall2, wallRect2)
    window.blit(player2, playerRect2)
    window.blit(ball, ballRect)
    window.blit(walltop, walltopRect)
    window.blit(walltop2, walltopRect2)

    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(points1), True, white)
    textRect = text.get_rect()
    textRect.center = (350, 30)

    text2 = font.render(str(points2), True, white)
    textRect2 = text2.get_rect()
    textRect2.center = (450, 30)
    window.blit(text, textRect)
    window.blit(text2, textRect2)

    ballpostemp = ballpos
    
    pos = 0,0
    pos2 = 0,0
    ballpos = 0,0
    
    
    pygame.display.flip()


pygame.quit()