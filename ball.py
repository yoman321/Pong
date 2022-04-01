from Bar import Bar
from Border import Border
import math

class Ball:
    def __init__(self, x, y, radius, moveSpeed, moveX, moveY, angle, firstCollision):
        self.x = x
        self.y = y
        self.radius = radius
        self.moveSpeed = moveSpeed
        self.moveX = moveX
        self.moveY = moveY
        self.angle = angle
        self.firstCollision = firstCollision
    
    #check distance between either bar
    def distBar(self, bar):
        extremity = 0

        if bar.player == "left":
            extremity = self.x - self.radius
        else:
            extremity = self.x + self.radius
        
        if bar.player == "left" and extremity <= (bar.xTop + bar.width):
            if self.y >= bar.yTop and self.y <= bar.yBot:
                self.moveSpeed = self.moveSpeed * -1
                if self.y >= bar.yTop and self.y < bar.yTop + 25:
                    self.angle = 315
                elif self.y >= bar.yTop + 25 and self.y < bar.yTop + 50:
                    self.angle = 335
                
                elif self.y >= bar.yTop + 50 and self.y < bar.yTop + 75:
                    self.angle = 50
                    
                elif self.y >= bar.yTop + 75 and self.y <= bar.yBot:
                    self.angle = 25

                #change movement for x and y
                if self.firstCollision:
                    self.moveSpeed = 8
                    self.firstCollision = False

                self.moveX = math.cos(math.radians(self.angle)) * self.moveSpeed
                self.moveY = math.sin(math.radians(self.angle)) * self.moveSpeed

        elif bar.player == "right" and extremity >= bar.xTop:
            if self.y >= bar.yTop and self.y <= bar.yBot:
                self.moveSpeed = self.moveSpeed * -1 #change movement direction
                if self.y >= bar.yTop and self.y < bar.yTop + 25:
                    self.angle = 25
                elif self.y >= bar.yTop + 25 and self.y < bar.yTop + 50:
                    self.angle = 50
                
                elif self.y >= bar.yTop + 50 and self.y < bar.yTop + 75:
                    self.angle = 335
                    
                elif self.y >= bar.yTop + 75 and self.y <= bar.yBot:
                    self.angle = 315
            
                #change movement for x and y
                if self.firstCollision:
                    self.moveSpeed = -8
                    self.firstCollision = False

                self.moveX = math.cos(math.radians(self.angle)) * self.moveSpeed
                self.moveY = math.sin(math.radians(self.angle)) * self.moveSpeed

    def distBorder(self, border):
        extremity = 0
        if border.name == "left":
            extremity = self.x - self.radius
        elif border.name == "right":
            extremity = self.x + self.radius
        elif border.name == "top":
            extremity = self.y - self.radius + 1
        else:
            extremity = self.y + self.radius
        
        if (border.name == "left" and extremity <= border.x) or (border.name == "right" and extremity >= border.x):
            self.moveX = 0
            self.moveY = 0
        elif (border.name == "top" and extremity <= border.y) or (border.name == "bot" and extremity >= border.y):
            self.moveY *= -1

