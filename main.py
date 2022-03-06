import Bar
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
            
    #Move bar while key is pressed
    if keyDown:
        bar1.move_ip(moveDict[K_DOWN])
    if keyUp:
        bar1.move_ip(moveDict[K_UP])
    if keyW:
        bar2.move_ip(moveDict[K_UP])
    if keyS:
        bar2.move_ip(moveDict[K_DOWN])

    #update the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), bar2)
    pygame.draw.rect(screen, (255, 0, 0), bar1)
    pygame.display.update()

    #tick the clock to check next update
    clock.tick(60)

pygame.quit() #quit pygame
