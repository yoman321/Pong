from Border import Border
from Bar import Bar
from Ball import Ball
import pygame
from pygame.locals import *

pygame.init() #remove this line if the window does not pop up instantly
screen = pygame.display.set_mode((1000, 800))
pygame.display.update()

#create the bars
bar1 = Bar(25, 350, 25, 450, 5, 100, "left", 8)
bar2 = Bar(970, 350, 970, 450, 5, 100, "right", 8)
rectBar1 = Rect(bar1.xTop, bar1.yTop, bar1.width, bar1.height)
rectBar2 = Rect(bar2.xTop, bar2.yTop, bar1.width, bar2.height)

#create top and bottom borders
leftBorder = Border(1, 1, 1, 800, "left")
rightBorder = Border(999, 0, 1, 800, "right")
topBorder = Border(1, 1, 1000, 1, "top")
botBorder = Border(0, 799, 1000, 1, "bot")
rectLeftBorder = Rect(leftBorder.x, leftBorder.y, leftBorder.width, leftBorder.height)
rectRightBorder = Rect(rightBorder.x, rightBorder.y, rightBorder.width, rightBorder.height)
rectTopBorder = Rect(topBorder.x, topBorder.y, topBorder.width, topBorder.height)
rectBotBorder = Rect(botBorder.x, botBorder.y, botBorder.width, botBorder.height)

#create values for ball
ball = Ball(500, 400, 13, -5, -5, 0, 180, True)

#create the clock 
clock = pygame.time.Clock()
tickCheck = 0

#boolean stateemtn to check if keys are still pressed
keyUp = False
keyDown = False
keyW = False
keyS = False

#Running algorithm
running = True
while  running:
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
        bar1.yTop += bar1.moveSpeed
        bar1.yBot += bar1.moveSpeed
        rectBar1.move_ip(0, bar1.moveSpeed)
    if keyW:
        bar1.yTop += -bar1.moveSpeed
        bar1.yBot += -bar1.moveSpeed
        rectBar1.move_ip(0, -bar1.moveSpeed)
    if keyUp:
        bar2.yTop += -bar2.moveSpeed
        bar2.yBot += -bar2.moveSpeed
        rectBar2.move_ip(0, -bar2.moveSpeed)
    if keyDown:
        bar2.yTop += bar2.moveSpeed
        bar2.yBot += bar2.moveSpeed
        rectBar2.move_ip(0, bar2.moveSpeed)

   #change ball direction if ever it hits something
    ball.distBorder(leftBorder)
    ball.distBorder(rightBorder)
    ball.distBorder(topBorder)
    ball.distBorder(botBorder)
    ball.distBar(bar1)
    ball.distBar(bar2)
    ball.x += ball.moveX
    ball.y += ball.moveY

    #update the screen
    screen.fill((0, 0, 0)) #reset screen
    pygame.draw.line(screen, (255, 1, 1), (500, 0), (500, 800), 1) #draw middle line
    pygame.draw.rect(screen, (0, 255, 0), rectBar2) #draw player bars
    pygame.draw.rect(screen, (255, 0, 0), rectBar1)
    pygame.draw.rect(screen, (9, 255, 255), rectLeftBorder)
    pygame.draw.rect(screen, (0, 255, 255), rectRightBorder)
    pygame.draw.rect(screen, (0, 255, 255), rectTopBorder)
    pygame.draw.rect(screen, (0, 255, 255), rectBotBorder)
    if ball.moveX != 0 or ball.moveY != 0: #check if the ball stopped moving
        pygame.draw.circle(screen, (0, 0, 255), (ball.x, ball.y), ball.radius, 0) #draw ball
    pygame.display.update()

    #tick the clock to check next update
    clock.tick(60)

pygame.quit() #quit pygame
