from labu import restart
restart(__file__)

import math
from labu import LabuSet,TObject,pygame

def circle(v):
    t = 2*math.pi*(v/100)
    x,y = math.cos(t)*35,math.sin(t)*35
    return x+65,y+50
class Vehicle_Submarine(LabuSet):
    fps = 60
    def __init__(self,load_save=True,auto_save=True):
        self.left = 0
        self.right = 0
        super().__init__(load_save=load_save,auto_save=auto_save)
    def submarine_obj(self):
        o = TObject(51,38,0.3 + self.oscale)

        o.rect(0,0,51,15)
        o.rect(0,25,21,13)
        o.rect(30,25,21,13)

        self.draw(o,self.size[0]//2,self.size[1]//2,center=True)

    def firee(self):
        o = TObject(70,20,0.1 + self.oscale)
        o.fill()
        if not self.fire: self.draw(o,self.size[0]//2,20,center=True)
        else: self.draw(o,self.size[0]//2,50,center=True)

    def lefte(self):
        o = TObject(150,100,self)
        o.rect(60,45,20,20)
        o.rect(0,100 - ((self.left + 25)%50) * 3,27,10)
        o.rect(*circle(self.left*2),13,10)
        self.draw(o,0,65)
    def righte(self) -> None:
        o = TObject(150,125,self)
        o.rect(60,45,25,20)
        o.rect(0,100 - ((self.right + 25)%50) * 3,27,10)
        o.rect(*circle(self.right*2),13,10)
        o.flip()
        self.draw(o,self.size[0],65,right=True)

    def run(self):
        self.clear()
        self.fire = False

        keys = self.keys
        if keys[pygame.K_SPACE]: self.fire = True
        if keys[pygame.K_d]: self.left = (self.left-1)%50
        if keys[pygame.K_c]: self.left = (self.left+1)%50
        if keys[pygame.K_k]: self.right = (self.right-1)%50
        if keys[pygame.K_m]: self.right = (self.right+1)%50
        if keys[pygame.K_ESCAPE]: self.running = False

        self.submarine_obj()
        self.firee()
        self.righte()
        self.lefte()

        self.update()

if __name__ == '__main__':
    labu = Vehicle_Submarine()
    labu.start()
