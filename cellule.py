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

    def set_img(self,scalx,scaly,grap):
        if grap == 0 :
            self.wid = int(scalx*1/4)
            self.hei = int(scaly*1/4)
            self.img = pygame.Surface((self.wid,self.hei))
            self.img.set_colorkey((0,0,0))
            pygame.draw.ellipse(self.img,(255,0,255),pygame.Rect((0,0),(self.wid,self.hei)))

        elif grap == 1 :
            self.wid = int(scalx*1/4)
            self.hei = int(scaly*1/4)
            self.img = pygame.Surface((self.wid,self.hei))
            self.img.set_colorkey((0,0,0))
            pygame.draw.ellipse(self.img,(0,0,0),pygame.Rect((0,0),(self.wid,self.hei)))

    def draw(self,screen,pos):
        screen.blit(self.img,(pos[0]-.5*self.wid,pos[1]-.5*self.hei))


    def move(self,ls_cell,d) :
        if self.selecting == True :
            if self.is_selected.move(ls_cell.copy(),d) :
                self.pos = (self.pos[0]+d[0],self.pos[1]+d[1])
                return(True)
        else :
            if not(out((self.pos[0]+d[0],self.pos[1]+d[1]))):
                self.pos = (self.pos[0]+d[0],self.pos[1]+d[1])
                return(True)
        return(False)

    def select(self,cell,grap,scalx,scaly):
        if self.selecting == False:
            self.is_selected=cell
            if grap <= 1 : cell.change_color(scalx,scaly,grap,cell.change)
            self.selecting = True
        else :
            self.selecting=False
            if grap <= 1 : cell.change_color(scalx,scaly,grap,(-cell.change[0],-cell.change[1],-cell.change[2]))



class cellule:
    def __init__(self,cells,color,change = (0,0,0),img = None):
        self.ctr = 1
        self.color = color
        self.cells=cells
        self.img = img
        self.change = change

    def copy(self):
        return cellule([a for a in self.cells],self.color,self.change,self.img)

    def set_image(self,scalx,scaly,grap):
        self.img = pygame.Surface((6*scalx,6*scaly))
        self.img.set_colorkey((0,0,0))
        cellule = self.cells.copy()
        ctr = cellule[self.ctr]
        cellule = [(i[0]-ctr[0], i[1]-ctr[1]) for i in cellule]
        xoff = 3*scalx
        yoff = 3*scaly
        if grap == 0:
            wid = scalx*5/8
            hei = scaly*5/8
            lines = []
            for elm in cellule :
                x=xoff+scalx*(elm[0]-elm[1]+0.5)
                y=yoff+scaly*(elm[0]+elm[1]+0.5)
                lines.append((x,y))
                pygame.draw.ellipse(self.img,self.color,pygame.Rect(((x-wid/2),y-hei/2),(wid,hei)))
            if len(lines)>1:pygame.draw.lines(self.img,self.color,False,lines,int(min(wid/2,hei/2)))
        if grap == 1:
            lines = []
            for elm in cellule :
                x=xoff+scalx*(elm[0]-elm[1]+0.5)
                y=yoff+scaly*(elm[0]+elm[1]+0.5)
                lines.append((x,y))
                pygame.draw.circle(self.img,(255,255,255),(x,y),int(min(scalx,scaly)//2))

            if len(lines)>1:
                pygame.draw.lines(self.img,(255,255,255),False,lines,int(3*min(scalx,scaly)//4))
                if self.color==(255,0,0):
                    pygame.draw.lines(self.img,(255,0,0),False,lines,int(2*min(scalx,scaly)//4))
            for elm in cellule :
                x=xoff+scalx*(elm[0]-elm[1]+0.5)
                y=yoff+scaly*(elm[0]+elm[1]+0.5)
                pygame.draw.circle(self.img,self.color,(x,y),int(0.8*min(scalx,scaly)//2))

    def change_color(self,scalx,scaly,grap, changement):
        color = self.color
        self.color = (color[0]+changement[0],color[1]+changement[1],color[2]+changement[2])
        self.set_image(scalx,scaly,grap)

    def draw(self,screen,xoff,yoff,scalx,scaly):
        x = self.cells[self.ctr][0]
        y = self.cells[self.ctr][1]
        screen.blit(self.img,((xoff+scalx*((x-y)-3),yoff+scaly*((x+y)-3))))

    def move(self,ls_cell,d):
        ls_cell.remove(self)
        if check(self,ls_cell.copy(), d):
            for i in range(len(self.cells)):
                self.cells[i] = (self.cells[i][0]+d[0],self.cells[i][1]+d[1])
            return True
        return False

class virus(cellule):
    def __init__(self,pos,base_color = (255,0,0),c = (0,0,0), img = None):
        super().__init__([pos,(pos[0]+1,pos[1])],base_color,c,img)

    def copy(self):
        return virus(self.cells[0],self.color,self.change,self.img)


class o(cellule):
    def __init__(self,pos,base_color = (127,127,127),c = (0,0,0), img = None):
        super().__init__([pos],base_color,c,img)
        self.ctr = 0
    def move(self,ls_cell,d):
        return False
    def copy(self):
        return o(self.cells[0],self.color,self.change,self.img)


class v(cellule):
    def __init__(self,pos,r,base_color = (255,127,0),c = (0,0,0)):
        super().__init__([turn(r,(pos[0],pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]),pos)],base_color,c)

class w(cellule):
    def __init__(self,pos,r,base_color = (30,180,255),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]),pos),pos],base_color,c)


class r(cellule):
    def __init__(self,pos,r,base_color = (255,100,170),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]-1),pos),pos],base_color,c)

class g(cellule):
    def __init__(self,pos,r,base_color = (0,127,50),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]-1),pos),pos],base_color,c)

class u(cellule):
    def __init__(self,pos,r,base_color = (0,0,255),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]-1),pos)],base_color,c)

class c(cellule):
    def __init__(self,pos,r,base_color = (100,0,100),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]+1),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],base_color,c)

class j(cellule):
    def __init__(self,pos,r,base_color = (0,255,0),c = (0,0,0)):
        super().__init__([turn(r,(pos[0]-1,pos[1]),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],base_color,c)

class l(cellule):
    def __init__(self,pos,r,base_color = (255,255,0),c = (0,0,0)):
        super().__init__([turn(r,(pos[0],pos[1]-1),pos),pos,turn(r,(pos[0]+1,pos[1]+1),pos)],base_color,c)
