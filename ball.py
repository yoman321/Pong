from Bar import Bar
from Border import Border
import math

class Ball:
    def __init__(self, x, y, radius, moveSpeed, moveX, moveY, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.moveSpeed = moveSpeed
        self.moveX = moveX
        self.moveY = moveY
        self.angle = angle
    
    #check distance between either bar
    def distBar(self, bar):
        extremity = 0

        if bar.player == "left":
            extremity = self.x - self.radius
        else:
            extremity = self.x + self.radius
        
        if bar.player == "left" and extremity <= bar.xTop + bar.width:
            if self.y >= bar.yTop and self.y <= bar.yBot:
                self.moveSpeed = 5
                if self.y >= bar.yTop and self.y < bar.yTop + 25:
                    self.angle = 125
                elif self.y >= bar.yTop + 25 and self.y < bar.yTop + 50:
                    self.angle = 160
                
                elif self.y >= bar.yTop + 50 and self.y < bar.yTop + 75:
                    self.angle = 325
                    
                elif self.y >= bar.yTop + 75 and self.y <= bar.yBot:
                    self.angle = 290
            
                #change movement for x and y
                self.moveX = math.cos(math.radians(self.angle)) * self.moveSpeed
                self.moveY = math.sin(math.radians(self.angle)) * self.moveSpeed

        elif bar.player == "right" and extremity >= bar.xTop:
            if self.y >= bar.yTop and self.y <= bar.yBot:
                self.moveSpeed = -5 #change movement direction
                
                if self.y >= bar.yTop and self.y < bar.yTop + 25:
                    self.angle = 35
                elif self.y >= bar.yTop + 25 and self.y < bar.yTop + 50:
                    self.angle = 70
                
                elif self.y >= bar.yTop + 50 and self.y < bar.yTop + 75:
                    self.angle = 325
                    
                elif self.y >= bar.yTop + 75 and self.y <= bar.yBot:
                    self.angle = 290
            
                #change movement for x and y
                self.moveX = math.cos(math.radians(self.angle)) * self.moveSpeed
                self.moveY = math.sin(math.radians(self.angle)) * self.moveSpeed

    def distBorder(self, border):
        extremity = 0
        if (border.name == "top"):
            extremity = self.y - self.radius
        else:
            extremity = self.y + self.radius
        
        if (border.name == "top" and extremity <= border.yLeft) or (border.name == "bot" and extremity >= border.yLeft):
            self.moveY *= -1
