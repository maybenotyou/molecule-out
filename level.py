import pygame
from cellule import *
import os

def rectangle_inscrit(rayon):
    return int((2*(rayon**2))**0.5)

class Bouton_circulaire():
    def __init__(self,x,y,rayon,couleur,surface,nom):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.rayon=rayon
        self.surface=surface
        self.nom=nom
        self.longueur=rectangle_inscrit(rayon)
        self.rect = pygame.Rect((self.x-(self.longueur//2),self.y-(self.longueur//2)),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
home = Bouton_circulaire(7,4,8,(255,255,255),3,'home')

class Bouton_menu(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Menu')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.rect[0]+self.rect[2],self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3),self.y),(int(2*self.longueur/3),int(self.longueur/2))))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y+int(self.longueur/12)),(int(self.longueur/3),int(self.longueur/3))))

class Bouton_recommencer(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Recommencer')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.circle(self.surface,(0,0,0),(self.x,self.y),self.rayon*0.8)
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon*0.6)
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/4),self.y),(int(self.longueur/2),+int(9*self.rayon/10))))
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.y+self.rayon*0.75),(self.x-int(self.longueur/2.5),self.y+self.rayon*0.75),(self.x-int(self.longueur/5),self.y+self.rayon*0.35)))


def level(screen,list_cell_ini,grap,taille):
    a= cursor((4,3))
    bg = pygame.Surface(screen.get_size())
    bg.fill((0,0,0))
    d=bg.get_size()
    xoff=d[0]*4/10
    yoff=-d[1]*3/10

    rad=45
    scalx=d[0]/9
    scaly=d[1]/9
    def placement(pos):
        x=pos[0]
        y=pos[1]
        return ((xoff + (x-y+0.5)*scalx),yoff+(x+y+0.5)*scaly)

    win = False

    #----Generation du plateau-----------
    wid = scalx*3/4
    hei = scaly*3/4
    for x in range(8):
        for y in range(8):
            if (1+abs(y-3)<=x<=7-abs(y-3)) or (x==0 and y == 3):
                koala=placement((x,y))
                pygame.draw.ellipse(bg,(255,255,255),pygame.Rect(((koala[0]-wid/2),koala[1]-hei/2),(wid,hei)))
    #--------------------------------------------


    list_cell_current=[i.copy() for i in list_cell_ini]

    #------- set base image of cells and the cursor ------------
    def generation_png(grap):
        for cell in list_cell_ini :
            cell.set_png(scalx,scaly,grap)

    def generation_image_cell(grap):
        for cell in list_cell_current :
            cell.set_image(scalx,scaly,grap)


    if grap > 1:
        generation_png(grap)
    else: generation_image_cell(grap)
    a.set_img(scalx,scaly,grap)
    #-----------------------------------------------------


    Menu=Bouton_menu(int(2*taille),screen.get_height()-int(2*taille),taille,(255,255,255),screen)
    Recommencer=Bouton_recommencer((2*taille),screen.get_height()-int(5*taille),taille,(255,255,255),screen)
    liste_boutons=[Menu,Recommencer]
    i=0
    b=liste_boutons[i]
    going=True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going=False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return False
                
                elif event.key==pygame.K_TAB:
                    if i>0:
                        i-=1
                    else:
                        i=len(liste_boutons)-1
                    b=liste_boutons[i]
                elif event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                    if b.nom=='Menu':
                        home.x = 1
                        going=False
                        
                    elif b.nom=='Recommencer':
                        return level(screen,list_cell_ini,grap,taille)
                elif     event.key == pygame.K_r :
                    a.selecting = False
                    list_cell_current=[i.copy() for i in list_cell_ini]
                    if grap <= 1 :generation_image_cell(grap)
                elif event.key == pygame.K_UP :
                    a.move(list_cell_current,(0,-1))
                elif event.key == pygame.K_DOWN :
                    a.move(list_cell_current,(0,1))
                elif event.key == pygame.K_LEFT :
                    a.move(list_cell_current,(-1,0))
                elif event.key == pygame.K_RIGHT :
                    a.move(list_cell_current,(1,0))
                elif event.key == pygame.K_x :
                    for e in list_cell_current :
                        if a.pos in e.cells :
                            a.select(e,grap,scalx,scaly)
        if pygame.mouse.get_pressed()[0] :
                mpos = pygame.mouse.get_pos()
                mx = mpos[0]
                my = mpos[1]
                mx,my = (mx-xoff)/scalx-.5 , (my-yoff)/scaly-.5
                mx = (mx + my)/2
                my = my-mx
                mx,my = round(mx), round(my)
                if not(out((mx,my))):
                    if not a.selecting :
                        for e in list_cell_current :
                            if a.pos in e.cells :
                                a.select(e,grap,scalx,scaly)
                    dis= (mx-a.pos[0],my-a.pos[1])
                    if abs(dis[0])+abs(dis[1])>1 :
                        if a.selecting:a.select(a.is_selected,grap,scalx,scaly)
                    if not a.move(list_cell_current,dis) :
                        if a.selecting:a.select(a.is_selected,grap,scalx,scaly)
                        a.move(list_cell_current,dis)


        for x in list_cell_current:
            if type(x) == virus and x.cells[0] == (0,3):
                win = True
                going = False

        screen.blit(bg,(0,0))
        for cell in list_cell_current:
            cell.draw(screen,xoff,yoff,scalx,scaly)
        a.draw(screen,placement(a.pos))
        pygame.draw.circle(screen,(100,100,100),(b.x,b.y),int(1.1*b.rayon))
        for bouton in liste_boutons:
            bouton.update()

        pygame.display.flip()
    if win == True :
        going = True
        font = pygame.font.Font("verdana.ttf", int(d[1]/9))
        c = font.render("Congrats",True,(0,255,0))
        screen.blit(c,(d[0]/5,d[1]/40))
        pygame.display.flip()
        while going :
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_x,pygame.K_ESCAPE] :
                    going = False
    return True


def filetolevel(path,grap = 0):
    coord = (1,3)
    i=0
    tot=[]
    with open(path) as f :
        for line in f:
            x=coord[0]+((i+1)//2)
            y=coord[1]+(i//2)
            line = line.split()
            if grap == 0 :
                for cel in line :
                    if cel[0] == 'V':
                        tot.append(virus((x,y)))
                    if cel[0] == 'o':
                        tot.append(o((x,y)))
                    if cel[0] == 'v':
                        tot.append(v((x,y),int(cel[1])))
                    if cel[0] == 'w':
                        tot.append(w((x,y),int(cel[1])))
                    if cel[0] == 'r':
                        tot.append(r((x,y),int(cel[1])))
                    if cel[0] == 'g':
                        tot.append(g((x,y),int(cel[1])))
                    if cel[0] == 'u':
                        tot.append(u((x,y),int(cel[1])))
                    if cel[0] == 'c':
                        tot.append(c((x,y),int(cel[1])))
                    if cel[0] == 'j':
                        tot.append(j((x,y),int(cel[1])))
                    if cel[0] == 'l':
                        tot.append(l((x,y),int(cel[1])))
                    x+=1
                    y-=1
            elif grap == 1:
                for cel in line :
                    if cel[0] == 'V':
                        tot.append(virus((x,y)))
                    if cel[0] == 'o':
                        tot.append(o((x,y)))
                    if cel[0] == 'v':
                        tot.append(v((x,y),int(cel[1])))
                    if cel[0] == 'w':
                        tot.append(w((x,y),int(cel[1])))
                    if cel[0] == 'r':
                        tot.append(r((x,y),int(cel[1])))
                    if cel[0] == 'g':
                        tot.append(g((x,y),int(cel[1])))
                    if cel[0] == 'u':
                        tot.append(u((x,y),int(cel[1])))
                    if cel[0] == 'c':
                        tot.append(c((x,y),int(cel[1])))
                    if cel[0] == 'j':
                        tot.append(j((x,y),int(cel[1])))
                    if cel[0] == 'l':
                        tot.append(l((x,y),int(cel[1])))
                    x+=1
                    y-=1
            i+=1
                
    return tot


import time 
def test():
    pygame.init()
    screen = pygame.display.set_mode((800,800))#,pygame.FULLSCREEN
    level(screen, [virus((4,3))],0,min(screen.get_size())//18)
    pygame.quit()
