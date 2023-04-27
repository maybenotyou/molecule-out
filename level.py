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
home = Bouton_circulaire(2,0,800,(255,255,255),300,'home')

class Bouton_menu(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Menu')

    def update(self,screen):
            self.surface = screen
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.rect[0]+self.rect[2],self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3),self.y),(int(2*self.longueur/3),int(self.longueur/2))))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y+int(self.longueur/12)),(int(self.longueur/3),int(self.longueur/3))))

class Bouton_recommencer(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Recommencer')

    def update(self,screen):
            self.surface = screen
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.circle(self.surface,(0,0,0),(self.x,self.y),self.rayon*0.8)
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon*0.6)
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/4),self.y),(int(self.longueur/2),+int(9*self.rayon/10))))
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.y+self.rayon*0.75),(self.x-int(self.longueur/2.5),self.y+self.rayon*0.75),(self.x-int(self.longueur/5),self.y+self.rayon*0.35)))

class Bouton_next(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Next')

    def update(self,screen):
        self.surface = screen
        pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
        pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0]+self.rect[2],self.y),(self.x,self.rect[1]+self.rect[3])))
        pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(int(self.longueur/2),int(self.longueur/2))))

def level(screen,list_cell_ini,grap,taille, miror = (False,False)):
    q_select = 0
    a= cursor((4,3))
    bg = pygame.Surface(screen.get_size())
    bg.fill((0,0,0))
    truescreen = screen
    notbg = pygame.Surface(screen.get_size())
    screen = notbg
    d=bg.get_size()
    xoff=d[0]*4/10
    yoff=-d[1]*3/10
    def placement(pos):
        x=pos[0]
        y=pos[1]
        return ((xoff + (x-y+0.5)*scalx),yoff+(x+y+0.5)*scaly)

    win = False

#-----------Generation du plateau-----------
    if grap==0:
        scalx=d[0]/9
        scaly=d[1]/9
        xoff=d[0]*4/10
        yoff=-d[1]*3/10

        wid = scalx*3/4
        hei = scaly*3/4
        for x in range(8):
            for y in range(8):
                if (1+abs(y-3)<=x<=7-abs(y-3)) or (x==0 and y == 3):
                    coordonnées=placement((x,y))
                    pygame.draw.ellipse(bg,(255,255,255),pygame.Rect(((coordonnées[0]-wid/2),coordonnées[1]-hei/2),(wid,hei)))
    elif grap==1:
        scalx=d[1]/9
        scaly=d[1]/9
        xoff=d[0]*4/10
        yoff=-d[1]/3

        bg = pygame.image.load('images/back.png').convert_alpha()
        bg = pygame.transform.scale(bg, (screen.get_size()))
        bg.convert()

        pygame.draw.rect(bg,(50,50,50),[[placement((0,3))[0]-taille,placement((0,3))[1]-taille],[placement((4,0))[0]-placement((0,4))[0]+2*taille,placement((8,3))[1]-placement((0,3))[1]+2*taille]],0,taille)
        for x in range(8):
            for y in range(8):
                if (1+abs(y-3)<=x<=7-abs(y-3)) or (x==0 and y == 3):
                    coordonnées=placement((x,y))

                    if (1+abs(y-3)<=x) and not (x==0 and y == 3):
                        pygame.draw.line(bg, (255,255,255), placement((x,y)),placement((x,y-1)), int(taille*1/5))
                        pygame.draw.line(bg, (255,255,255), placement((x,y)),placement((x,y+1)), int(taille*1/5))
                    if (1+abs(y-3)<=x<=7-abs(y-3)) and not (x==0 and y==3):
                        pygame.draw.line(bg, (255,255,255), placement((x,y)),placement((x-1,y)), int(taille*1/5))
                        pygame.draw.line(bg, (255,255,255), placement((x,y)),placement((x+1,y)), int(taille*1/5))

                    pygame.draw.circle(bg,(255,255,255),(coordonnées[0],coordonnées[1]),(taille*1/4))

        # haut
        pygame.draw.rect(bg,(150,150,150),[placement((1,2))[0],placement((1,2))[1]-taille,placement((4,-1))[0]-placement((1,2))[0],taille*4/3])
        # droite
        pygame.draw.rect(bg,(150,150,150),[placement((4,-1))[0]-taille/3,placement((4,-1))[1],taille*4/3,placement((8,3))[1]-placement((4,-1))[1]])
        # gauche
        pygame.draw.rect(bg,(150,150,150),[placement((1,4))[0]-taille,placement((1,4))[1],taille*4/3,placement((4,7))[1]-placement((1,4))[1]])
        # bas
        pygame.draw.rect(bg,(150,150,150),[placement((4,7))[0],placement((4,7))[1]-taille/3,placement((4,-1))[0]-(placement((4,7))[0]),taille*4/3])

        # Cercles de la bordure
        for c in range(1,5):
            pygame.draw.circle(bg,(150,150,150),placement((c,c+3)),taille)

        for c in range(1,5):
            pygame.draw.circle(bg,(150,150,150),placement((c,3-c)),taille)

        for c in range(4):
            pygame.draw.circle(bg,(150,150,150),placement((c+5,c)),taille)

        for c in range(3):
                pygame.draw.circle(bg,(150,150,150),placement((7-c,c+4)),taille)

    #--------------------------------------------

    #------- set base image of cells and the cursor ------------
    for cell in list_cell_ini :
        cell.set_image(scalx,scaly,grap)


    list_cell_current=[i.copy() for i in list_cell_ini]

    a.set_img(scalx,scaly,grap)
    #-----------------------------------------------------
    
    if grap == 1 :
        for i in range(len(list_cell_current)):
            if type(list_cell_current[i]) == virus :
                q_select = i
        q_cell = list_cell_current[q_select]
        q_cell_pos = q_cell.cells[1]
        dis= (q_cell_pos[0]-a.pos[0],q_cell_pos[1]-a.pos[1])
        a.move(list_cell_current,dis)
        a.select(q_cell,grap,scalx,scaly)
        

    Menu=Bouton_menu(int(2*taille),screen.get_height()-int(2*taille),taille,(255,255,255),screen)
    Recommencer=Bouton_recommencer((2*taille),screen.get_height()-int(5*taille),taille,(255,255,255),screen)
    liste_boutons=[Menu,Recommencer]
    i=0
    b=liste_boutons[i]
    going=True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home.x = 2
                going=False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    home.x = 2
                    return False

                elif not pygame.mouse.get_visible():
                    if event.key==pygame.K_TAB:
                        if i>0:
                            i-=1
                        else:
                            i=len(liste_boutons)-1
                        b=liste_boutons[i]
                    elif event.key == pygame.K_SPACE:
                        if b.nom=='Menu':
                            home.x = 1
                            going=False

                        elif b.nom=='Recommencer':
                            return level(screen,list_cell_ini,grap,taille)
                    elif event.key in [pygame.K_DELETE, pygame.K_BACKSPACE]:
                        home.x = 2
                        going=False
                    elif     event.key == pygame.K_r :
                        a.selecting = False
                        list_cell_current=[i.copy() for i in list_cell_ini]
                    elif event.key in [pygame.K_UP,pygame.K_KP9] :
                        a.move(list_cell_current,(0,-1))
                    elif event.key in [pygame.K_DOWN,pygame.K_KP1] :
                        a.move(list_cell_current,(0,1))
                    elif event.key in [pygame.K_LEFT,pygame.K_KP7] :
                        a.move(list_cell_current,(-1,0))
                    elif event.key in [pygame.K_RIGHT,pygame.K_KP3] :
                        a.move(list_cell_current,(1,0))

                    elif grap!=1:
                        if event.key in [pygame.K_x, pygame.K_z, pygame.K_w] :
                            for e in list_cell_current :
                                if a.pos in e.cells :
                                    a.select(e,grap,scalx,scaly)

                    if event.key in [pygame.K_a, pygame.K_q,pygame.K_KP5]:
                        if a.selecting:a.select(a.is_selected,grap,scalx,scaly)
                        while True :
                            q_select += 1
                            if q_select == len(list_cell_current): q_select = 0
                            if type(list_cell_current[q_select]) == o:
                                continue
                            break
                        q_cell = list_cell_current[q_select]
                        q_cell_pos = q_cell.cells[1]
                        dis= (q_cell_pos[0]-a.pos[0],q_cell_pos[1]-a.pos[1])
                        a.move(list_cell_current,dis)
                        a.select(q_cell,grap,scalx,scaly)

            elif event.type==pygame.MOUSEBUTTONDOWN and  pygame.mouse.get_visible():
                for bouton in liste_boutons:
                    if bouton.rect.collidepoint(event.pos):
                        if bouton.nom=='Menu':
                            home.x = 1
                            going=False

                        elif bouton.nom=='Recommencer':
                            return level(screen,list_cell_ini,grap,taille)

        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_visible():
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
        if not pygame.mouse.get_visible():
            pygame.draw.circle(screen,(100,100,100),(b.x,b.y),int(1.1*b.rayon))
        for bouton in liste_boutons:
            bouton.update(screen)
        screen=pygame.transform.flip(screen,miror[0],miror[1])
        truescreen.blit(screen,(0,0))

        pygame.display.flip()
    screen = truescreen
    if win == True :
        going = True
        bg = pygame.image.load('images/back.png').convert_alpha()
        bg = pygame.transform.scale(bg, (screen.get_size()))
        bg.convert()
        Menu=Bouton_menu(int(screen.get_width()/3.3),int(10.1*taille),int(2*taille),(255,255,255),screen)
        Recommencer=Bouton_recommencer(int(screen.get_width()/2),int(10.1*taille),int(2*taille),(255,255,255),screen)
        Next=Bouton_next(int(screen.get_width()/1.4),int(10.1*taille),int(2*taille),(255,255,255),screen)
        liste_boutons=[Menu,Recommencer,Next]
        i=0
        b=liste_boutons[i]
        pygame.display.flip()
        while going :
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_x,pygame.K_ESCAPE] :
                        return False

                    elif event.key==pygame.K_RIGHT:
                        if i<len(liste_boutons)-1:
                            i+=1
                        else:
                            i=0
                        b=liste_boutons[i]

                    elif event.key==pygame.K_LEFT:
                        if i>0:
                            i-=1
                        else:
                            i=len(liste_boutons)-1
                        b=liste_boutons[i]

                    elif event.key in [pygame.K_SPACE,pygame.K_RETURN]:
                        if b.nom=='Menu':
                            home.x = 1
                            going=False

                        elif b.nom=='Recommencer':
                            return level(screen,list_cell_ini,grap,taille)

                        elif b.nom=='Next':
                            home.x = 2
                            going=False
                elif event.type==pygame.MOUSEBUTTONDOWN and  pygame.mouse.get_visible():
                        for bouton in liste_boutons:
                            if bouton.rect.collidepoint(event.pos):
                                if bouton.nom=='Menu':
                                    home.x = 1
                                    going=False

                                elif bouton.nom=='Recommencer':
                                    return level(screen,list_cell_ini,grap,taille)

                                elif bouton.nom=='Next':
                                    home.x = 2
                                    going=False

            screen.blit(bg,(0,0))
            screen.blit(pygame.font.Font("verdana.ttf", int(d[1]/11)).render("Félicitations, le virus est sorti !",True,(9,145,0)),(d[0]/9,d[1]/8))
            if not pygame.mouse.get_visible():
                pygame.draw.circle(screen,(100,100,100),(b.x,b.y),int(1.1*b.rayon))
            for bouton in liste_boutons:
                bouton.update(screen)
            pygame.display.update()
    return True


def filetolevel(path,grap):
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
                        tot.append(virus((x,y),(255,150,150),(0,-150,-150)))
                    if cel[0] == 'o':
                        tot.append(o((x,y),(255,255,255)))
                    if cel[0] == 'v':
                        tot.append(v((x,y),int(cel[1]),(255,200,100),(0,-50,-100)))
                    if cel[0] == 'w':
                        tot.append(w((x,y),int(cel[1]),(100,255,255),(-100,-15,-15)))
                    if cel[0] == 'r':
                        tot.append(r((x,y),int(cel[1]),(255,200,225),(0,-50,-25)))
                    if cel[0] == 'g':
                        tot.append(g((x,y),int(cel[1]),(100,225,100),(-100,-50,-100)))
                    if cel[0] == 'u':
                        tot.append(u((x,y),int(cel[1]),(100,100,255),(-100,-100,-100)))
                    if cel[0] == 'c':
                        tot.append(c((x,y),int(cel[1]),(150,100,150),(0,-100,0)))
                    if cel[0] == 'j':
                        tot.append(j((x,y),int(cel[1]),(160,255,100),(-60,-55,-100)))
                    if cel[0] == 'l':
                        tot.append(l((x,y),int(cel[1]),(255,255,150),(-5,-15,-150)))
                    x+=1
                    y-=1
            i+=1

    return tot


import time
def test():
    pygame.init()
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    level(screen, [virus((1,3))],0,min(screen.get_size())//18)
    pygame.quit()
