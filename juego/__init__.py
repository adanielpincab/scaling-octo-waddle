import os
import time

FPS = 60

class Object:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.symbol = symbol
    
    def update(self, game):
        pass

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.objects = []
        self.lastScreen = None
    
    def addObject(self, object):
        self.objects.append(object)

    def update(self):
        for obj in self.objects:
            obj.update(self)

    def draw(self):
        screen = '_'*(self.x+2)+'\n'
        for y in range(self.y+1):
            screen += '|'
            for x in range(self.x+1):
                paint = ' '
                for obj in self.objects:
                    if (int(obj.x) == x) and (int(obj.y) == y):
                        paint = obj.symbol
                screen += paint
            screen += '|'
            screen += '\n'
        screen += '-'*(self.x+2)

        if screen != self.lastScreen:
            os.system('cls')
            print(screen)
            self.lastScreen = screen