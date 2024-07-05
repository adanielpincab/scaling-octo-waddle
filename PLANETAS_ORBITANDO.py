from juego import *
import random
from uuid import uuid4

CONSTANTE_GRAVITACIONAL = 60

class Planet(Object):
    def __init__(self, x, y, mass):
        super().__init__(x, y, 'O')
        self.mass = mass
        self.id = str(uuid4())

    def update(self, game):
        '''https://www.fisicalab.com/apartado/fuerza-gravitatoria'''

        accx = 0
        accy = 0
        for p in game.objects:
            if p.id != self.id:
                distance = ((p.x - self.x)**2 + (p.y - self.y)**2)**(0.5) # https://es.wikipedia.org/wiki/Distancia_euclidiana
                if distance < 1:
                    distance = 1
                force = -CONSTANTE_GRAVITACIONAL * (self.mass * p.mass) / (distance)**2 # distancia (modulo)
                vector = [(self.x - p.x)/distance, (self.y - p.y)/distance] # vector UNITARIO de la fuerza
                
                # fuerza = masa * acceleracion, asi que la aceleracion es fuerza/masa
                accx += vector[0] * force / self.mass
                accy += vector[1] * force / self.mass
        
        self.velx += accx/FPS
        self.vely += accy/FPS

        self.x += self.velx/FPS
        self.y += self.vely/FPS

        # rebotes con las paredes
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

g = Game(100, 40)

'''
for i in range(20):
    planeta = Planet(random.randint(1, 100), random.randint(1, 40), random.randint(1, 5))
    g.addObject(planeta)
'''

planeta1 = Planet(50, 10, 50)
planeta2 = Planet(50, 30, 10)

planeta2.velx = 10
g.addObject(planeta1)
g.addObject(planeta2)

while True:
    start = time.time()
    g.update()
    g.draw()
    passed = time.time() - start
    if passed < (1/FPS):
        time.sleep((1/FPS) - (passed))