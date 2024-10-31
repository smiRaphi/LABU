from labu import restart
restart(__file__)

from labu import LabuSet,TObject,pygame

STICK = (
    (0,1,1),
    (1,1,1),
    (1,1,0),
    (0,1,0),
)

class Vehicle_Car(LabuSet):
    bsize = (128,96)
    tosave = ('stick1','stick2')
    savename = 'vehicle.car'
    def __init__(self,load_save=True,auto_save=True):
        self.stick1 = 0
        self.stick2 = 0
        super().__init__(oscale=2,load_save=load_save,auto_save=auto_save)

        self.add_ic('s1')
        self.add_ic('s2')

    def booste(self):
        if self.boost: self.rect(7,7,50,10)
    def reversee(self):
        if self.reverse: self.rect(11,self.size[1]-25,50,15)
        else: self.rect(38,self.size[1]-25,23,15)
    def stick1e(self):
        s = STICK[self.stick1]
        o = TObject(76,16,self)
        if s[0]: o.rect(0,0,8,16)
        if s[1]: o.rect(24,0,28,16)
        if s[2]: o.rect(68,0,8,16)
        o.rotate(10 if self.stick1_down else 45)
        o.flip(True)
        self.draw(o,self.size[0],50 + (20 if self.stick1_down else 0),right=True)
    def stick2e(self):
        s = STICK[self.stick2]
        o = TObject(76,16,self)
        if s[0]: o.rect(0,0,8,16)
        if s[1]: o.rect(24,0,28,16)
        if s[2]: o.rect(68,0,8,16)
        o.rotate(10 if self.stick2_down else 45)
        self.draw(o,self.size[0],16 - (5 if self.stick2_down else 0),right=True)
    def car_obj(self):
        o = TObject(76,70,self)
        o.rect(0,0,25,22) # small, top left
        o.rect(0,48,25,22) # small, bottom left
        o.rect(51,48,25,22) # small, bottom right
        o.rect(48,0,28,25) # big, top right
        self.draw(o,self.size[0]//2,self.size[1]//2,center=True)

    def run(self):
        self.clear()
        self.stick1_down = self.stick2_down = self.boost = self.reverse = False

        keys = self.keys
        if keys[pygame.K_s]: self.reverse = True
        if keys[pygame.K_q]: self.stick1_down = True
        if keys[pygame.K_e]: self.stick2_down = True
        if keys[pygame.K_w]: self.boost = True
        if keys[pygame.K_1] and self.gic('s1'): self.stick1 = (self.stick1-1)%4
        if keys[pygame.K_2] and self.gic('s1'): self.stick1 = (self.stick1+1)%4
        if keys[pygame.K_3] and self.gic('s2'): self.stick2 = (self.stick2-1)%4
        if keys[pygame.K_4] and self.gic('s2'): self.stick2 = (self.stick2+1)%4
        if keys[pygame.K_ESCAPE]: self.running = False

        self.car_obj()
        self.booste()
        self.reversee()
        self.stick1e()
        self.stick2e()

        self.update()

if __name__ == '__main__':
    v = Vehicle_Car()
    v.start()
