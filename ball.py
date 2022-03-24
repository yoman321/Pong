from Bar import Bar
import math

class Ball:
    def __init__(self, x, y, radius, moveSpeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.moveSpeed = moveSpeed
    
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
        elif bar.player == "right" and extremity >= bar.xTop:
            if self.y >= bar.yTop and self.y <= bar.yBot:
                self.moveSpeed = -5

