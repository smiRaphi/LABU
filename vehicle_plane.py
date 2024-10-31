from labu import restart
restart(__file__)

from labu import LabuSet,TObject,pygame

class Vehicle_Plane(LabuSet):
    bsize = (128,96)
    def plane_obj(self):
        o = TObject(17,27,self)

        o.rect(5,0,7,13)  # |
        o.rect(0,20,17,7) # -

        self.draw(o,self.size[0]//2,self.size[1]//2,center=True)

    def firee(self):
        o = TObject(25,7,self)
        o.fill()
        if self.fire: self.draw(o,self.size[0]//2,5,center=True)
        else: self.draw(o,self.size[0]//2,15,center=True)

    def run(self):
        self.clear()
        self.fire = False

        keys = self.keys
        if keys[pygame.K_SPACE]: self.fire = True
        if keys[pygame.K_ESCAPE]: self.running = False

        self.plane_obj()
        self.firee()

        self.update()

if __name__ == '__main__':
    labu = Vehicle_Plane()
    labu.start()
