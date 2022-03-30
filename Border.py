from tkinter import Y


class Border:
    def __init__(self, xLeft, yLeft, xRight, yRight, width, height, name):
        self.xRight = xRight
        self.yRight = yRight
        self.xLeft = xLeft
        self.yLeft = yLeft
        self.width = width
        self.height = height
        self.name = name