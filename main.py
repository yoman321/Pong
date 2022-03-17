import Bar
import math
import pygame
from pygame.locals import *

#create a movement dictionary
moveDict = {
    K_DOWN: [0, 5],
    K_UP: [0, -5],
}

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.update()

#create the bars
bar1 = Rect(25, 350, 5, 100)
bar2 = Rect(970, 350, 5, 100)

#create values for ball
ballX = 500
ballY = 400
ballRadius = 13
ballMovement = 5

#create the clock 
clock = pygame.time.Clock()

#boolean stateemtn to check if keys are still pressed
keyUp = False
keyDown = False
keyW = False
keyS = False

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
        bar1.move_ip(moveDict[K_DOWN])
    if keyW:
        bar1.move_ip(moveDict[K_UP])
    if keyUp:
        bar2.move_ip(moveDict[K_UP])
    if keyDown:
        bar2.move_ip(moveDict[K_DOWN])

    #move ball if ever it hits something
    distanceBar2 = math.sqrt(math.pow((bar2.top - ballY), 2) + math.pow((bar2.left - ballX), 2))
    print(bar2.top)
    print(bar2.left)
    if (distanceBar2 <= ballRadius):
        ballMovement = -5

    ballX += ballMovement

    #update the screen
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 1, 1), (500, 0), (500, 800), 1)
    pygame.draw.circle(screen, (0, 0, 255), (ballX, ballY), ballRadius, 0)
    pygame.draw.rect(screen, (0, 255, 0), bar2)
    pygame.draw.rect(screen, (255, 0, 0), bar1)
    pygame.display.update()

    #tick the clock to check next update
    clock.tick(60)

pygame.quit() #quit pygame
