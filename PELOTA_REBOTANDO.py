from juego import *
import random

GRAVITY = 100

class Ball(Object):
    def __init__(self, x, y):
        super().__init__(x, y, '@')

    def update(self, game):
        self.vely += GRAVITY/FPS
        self.x += self.velx/FPS
        self.y += self.vely/FPS

        if self.y >= game.y:
            self.y = game.y
            self.vely *= -0.9
            self.velx *= 0.9
        
        if self.y < 0:
            self.y = 0
            self.vely *= -0.9

        if self.x >= game.x:
            self.x = game.x-1
            self.velx *= -0.9
        
        if self.x < 0:
            self.x = 0
            self.velx *= -0.9

g = Game(40, 15)

pelota = Ball(20, 5)
pelota.velx = random.randint(1, 500) * random.choice([-1, 1])
pelota.vely = random.randint(1, 500) * random.choice([-1, 1])

g.addObject(pelota)

while True:
    start = time.time()
    g.update()
    g.draw()
    passed = time.time() - start
    if passed < 1/FPS:
        time.sleep(1/FPS - (time.time()-start))