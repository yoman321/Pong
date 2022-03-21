from Bar import Bar
from Ball import Ball
import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.update()

#create the bars
bar1 = Bar(25, 350, 25, 450, 5, 100)
bar2 = Bar(970, 350, 25, 450, 5, 100)
rectBar1 = Rect(bar1.xTop, bar1.yTop, bar1.width, bar1.height)
rectBar2 = Rect(bar2.xTop, bar2.yTop, bar1.width, bar2.height)

#create values for ball
ball = Ball(500, 400, 13, 5)

#create the clock 
clock = pygame.time.Clock()

#boolean stateemtn to check if keys are still pressed
keyUp = False
keyDown = False
keyW = False
keyS = False

#Running algorithm
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                keyDown = True
            if event.key == K_UP:
                keyUp = True
            if event.key == K_w:
                keyW = True
            if event.key == K_s:
                keyS = True
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                keyDown = False
            if event.key == K_UP:
                keyUp = False
            if event.key == K_w:
                keyW = False
            if event.key == K_s:
                keyS = False
            
    #Move bar while key is pressed-
    if keyS:
        bar1.yTop += 5
        bar2.yBot += 5
        rectBar1.move_ip(0, 5)
    if keyW:
        bar1.xTop += -5
        bar2.xBot += -5
        rectBar1.move_ip(0, -5)
    if keyUp:
        bar2.xTop += -5
        bar2.xBot += -5
        rectBar2.move_ip(0, -5)
    if keyDown:
        bar2.xTop += 5
        bar2.xBot += 5
        rectBar2.move_ip(0, 5)

    #change ball direction if ever it hits something
    ball.distBar(bar1)
    ball.distBar(bar2)
    ball.x += ball.moveSpeed

    #update the screen
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 1, 1), (500, 0), (500, 800), 1)
    pygame.draw.circle(screen, (0, 0, 255), (ball.x, ball.y), ball.radius, 0)
    pygame.draw.rect(screen, (0, 255, 0), rectBar2)
    pygame.draw.rect(screen, (255, 0, 0), rectBar1)
    pygame.display.update()

    #tick the clock to check next update
    clock.tick(60)

pygame.quit() #quit pygame
