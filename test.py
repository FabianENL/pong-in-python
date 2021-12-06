import pygame
pygame.init

ball = pygame.image.load("sprites/ball.png")
ballRect = ball.get_rect()
ballRect = ballRect.move(400,300)


size = width,height = 800,600
color = (0,0,0)
vel = [2,2]
title = "Pong in python"



window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

run = True
while run:
    pygame.time.delay(1)
    ads = pygame.event.get()
    #Handle Arrow Key event
    keys = pygame.key.get_pressed()

    ballpostemp = 1,1
    ballRect = ballRect.move(ballpostemp)

    window.blit(ball, ballRect)
    pygame.display.flip()
pygame.quit()

    