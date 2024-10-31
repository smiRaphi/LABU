import sys,os,subprocess

import os,sys,subprocess
def restart(file):
    if not '.venv' in sys.executable:
        subprocess.Popen(['.venv\\Scripts\\pythonw.exe',os.path.basename(file)] + sys.argv[1:])
        sys.exit()

if '.venv' in sys.executable:
    import pygame,ctypes,json,os
    pygame.init()

class TObject:
    def __init__(self,w:int,h:int,scale):
        if type(scale) in [int,float]: self.scale = scale
        else: self.scale = scale.oscale
        self.s = pygame.Surface((w//self.scale,h//self.scale),pygame.SRCALPHA)

    def fill(self): self.s.fill((255,255,255))
    def rect(self,x:int,y:int,w:int,h:int): self.s.fill((255,255,255),(x//self.scale,y//self.scale,w//self.scale,h//self.scale))
    def flip(self,xory=False): self.s = pygame.transform.flip(self.s,not xory,xory)
    def rotate(self,rot:float): self.s = pygame.transform.rotate(self.s,rot)

class IC:
    def __init__(self,fs):
        self.c = 0
        self.fs = fs
    def update(self): self.c = min(self.c+1,self.fs)
    def check(self):
        r = self.c >= self.fs
        if r: self.c = 0
        return r

def find_joycons():
    for x in range(pygame.joystick.get_count()):
        j = pygame.joystick.Joystick(x)
        if 'joy-con (l/r)' in j.get_name().lower(): return j

class LabuSet:
    tosave = ()
    savename = '?INVALID?'
    bsize = (320,240)
    fps = 30
    def __init__(self,scale:int=1,oscale:int=1,rotation=0,load_save=True,auto_save=True):
        self.size = (self.bsize[0]//scale,self.bsize[1]//scale)
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Labu")
        hwnd = pygame.display.get_wm_info()["window"]
        style = 0x00000000 | 0x00C00000 | 0x00080000 | 0x00040000 | 0x00800000 | 0x10000000
        ctypes.windll.user32.SetWindowLongW(hwnd,-16,style)

        self.running = self.__running = True
        self.scale = scale
        self.oscale = oscale
        self.rotation = rotation
        self.clock = pygame.time.Clock()
        self.ics = {}
        if load_save: self.load()

        self.auto_save = auto_save
        #self.controller = find_joycons()

    def clear(self): self.win.fill((0,0,0))
    def rect(self,x:int,y:int,w:int,h:int): pygame.draw.rect(self.win,(255,255,255),(x//self.scale,y//self.scale,w//self.oscale,h//self.oscale))
    def draw(self,o:TObject,x,y,right=False,center=False):
        # x //= self.scale
        # y //= self.scale
        o = o.s
        if right: po = o.get_rect(topright=(x,y))
        elif center: po = o.get_rect(center=(x,y))
        else: po = o.get_rect(topleft=(x,y))
        self.win.blit(o,po.topleft)

    def update(self):
        for e in self.events:
            if e.type == pygame.QUIT:
                self.running = False
                break
        if not self.running:
            self.stop()
            return
        self._update()
        for x in self.ics.values(): x.update()
        self.clock.tick(self.fps)
    def _update(self):
        if self.rotation: self.win.blit(pygame.transform.rotate(self.win,self.rotation),(0,0))
        pygame.display.flip()

    def start(self):
        while self.running: self.run()

    def stop(self,save:bool=None):
        if not self.__running: return
        self.clear()
        self._update()
        self.__running = self.running = False
        if save or (save is None and self.auto_save): self.save()

    def save(self):
        if not self.tosave: return
        s = {x:getattr(self,x) for x in self.tosave}
        json.dump(s,open(self.savename + '.json','w',encoding='utf-8'))
    def load(self):
        if not os.path.exists(self.savename + '.json'): return
        s = json.load(open(self.savename + '.json','r',encoding='utf-8'))
        for x in s:
            if x not in self.tosave: continue
            setattr(self,x,s[x])
    def add_ic(self,id,fs=7): self.ics[id] = IC(fs)
    def gic(self,id) -> bool: return self.ics[id].check()

    @property
    def events(self): return pygame.event.get()
    @property
    def keys(self): return pygame.key.get_pressed()

    def __del__(self): self.stop(self.auto_save)
