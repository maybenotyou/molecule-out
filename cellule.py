import pygame

def turn(n,p,c): #tourne 90 horaire
    for i in range(n) :
        p=(-(p[1]-c[1])+c[0],p[0]-c[0]+c[1])
    return p

def check(cel, ls_cell,d):
    und =(-d[0],-d[1])
    un=[]
    for i in cel.cells :
        i=(i[0]+d[0],i[1]+d[1])
        if out(i):
            for z in un :
                ls_cell.append(z)
                z.move(ls_cell,und)
            return False
        for z in ls_cell :
            if i in z.cells :
                if not(z.move(ls_cell, d)) :
                    for k in un :
                        ls_cell.append(k)
                        k.move(ls_cell,und)
                    return False
                un.append(z)
    return True

def placement(pos):
    x=pos[0]
    y=pos[1]
    return ((xoff +(x-y)*scalx),yoff+(x+y)*scaly)

def out(pos):
    if (1+abs(pos[1]-3)<=pos[0]<=7-abs(pos[1]-3)) or (pos[0]==0 and pos[1] == 3):
        return False
    return True

class cursor :
    def __init__(self,pos):
        self.pos = pos
        self.selecting = False
        self.is_selected = None
        self.img = None

    def set_img(self,scalx,scaly):
        self.wid = int(scalx*1/4)
        self.hei = int(scaly*1/4)
        self.img = pygame.Surface((self.wid,self.hei))
        self.img.set_colorkey((0,0,0))
        pygame.draw.ellipse(self.img,(255,0,255),pygame.Rect((0,0),(self.wid,self.hei)))

    def draw(self,screen,pos):
        screen.blit(self.img,(pos[0]-.5*self.wid,pos[1]-.5*self.hei))


    def move(self,ls_cell,d) :
        if self.selecting == True :
            if self.is_selected.move(ls_cell.copy(),d) :
                self.pos = (self.pos[0]+d[0],self.pos[1]+d[1])
        else :
            if not(out((self.pos[0]+d[0],self.pos[1]+d[1]))):
                self.pos = (self.pos[0]+d[0],self.pos[1]+d[1])
    def select(self,cell):
        if self.selecting == False:
            self.is_selected=cell
            self.selecting = True
        else :
            self.selecting=False



class cellule:
    def __init__(self,cells,color):
        self.ctr = 1
        self.color = color
        self.cells=cells
        self.img = None

    def copy(self):
        return cellule([a for a in self.cells],self.color)

    def set_image(self,scalx,scaly):
        self.img = pygame.Surface((5*scalx,5*scaly))
        self.img.set_colorkey((0,0,0))
        cellule = self.cells.copy()
        ctr = cellule[self.ctr]
        cellule = [(i[0]-ctr[0], i[1]-ctr[1]) for i in cellule]
        wid = scalx*5/8
        hei = scaly*5/8
        xoff = 2.5*scalx
        yoff = 2.5*scaly
        lines = []
        for elm in cellule :
            x=xoff+scalx*(elm[0]-elm[1]+.5)
            y=yoff+scaly*(elm[0]+elm[1]+.5)
            lines.append((x,y))
            pygame.draw.ellipse(self.img,self.color,pygame.Rect(((x-wid/2),y-hei/2),(wid,hei)))
        if len(lines)>1:pygame.draw.lines(self.img,self.color,False,lines,int(min(wid/2,hei/2)))


    def draw(self,screen,xoff,yoff,scalx,scaly):
        x = self.cells[self.ctr][0]
        y = self.cells[self.ctr][1]
        screen.blit(self.img,((xoff+scalx*((x-y)-2.5),yoff+scaly*((x+y)-2.5))))

    def move(self,ls_cell,d):
        ls_cell.remove(self)
        if check(self,ls_cell.copy(), d):
            for i in range(len(self.cells)):
                self.cells[i] = (self.cells[i][0]+d[0],self.cells[i][1]+d[1])
            return True
        return False

class virus(cellule):
    def __init__(self,pos):
        super().__init__([pos,(pos[0]+1,pos[1])],(255,0,0))

    def copy(self):
        return virus(self.cells[0])


class o(cellule):
    def __init__(self,pos):
        super().__init__([pos],(127,127,127),)
        self.ctr = 0
    def move(self,ls_cell,d):
        return False
    def copy(self):
        return o(self.cells[0])


class v(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0],pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]),pos)],(255,127,0))

class w(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]),pos),pos],(30,180,255))

class r(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]-1),pos),pos],(255,100,170))

class g(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]-1),pos),pos],(0,127,50))

class u(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]-1),pos)],(0,0,255))

class c(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],(100,0,100))

class j(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0]-1,pos[1]),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],(0,255,0))

class l(cellule):
    def __init__(self,pos,r):
        super().__init__([turn(r,(pos[0],pos[1]-1),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],(255,255,0))
