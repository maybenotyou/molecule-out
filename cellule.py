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
        
    def draw(self,screen):
        pygame.draw.circle(screen,(255,0,255),placement(self.pos),10)
        
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
        self.color = color
        self.cells=cells
    
    def copy(self):
        return cellule([a for a in self.cells],self.color)
        
    def draw(self,screen):
        rad=40
        for i in self.cells :
            pygame.draw.circle(screen,self.color,placement(i),rad)
        for i in range(1,len(self.cells)) :
            pygame.draw.line(screen,self.color,placement(self.cells[i-1]),placement(self.cells[i]),width=50)

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
        super().__init__([pos],(127,127,127))
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
