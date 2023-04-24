import pygame
from cellule import *
import os

def level(screen,list_cell_ini):
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
    def generation_image_cell():
        for cell in list_cell_current : cell.set_image(scalx,scaly)
        a.set_img(scalx,scaly)
    generation_image_cell()
    #-----------------------------------------------------

    going=True
    while going :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r :
                a.selecting = False
                list_cell_current=[i.copy() for i in list_cell_ini]
                generation_image_cell()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP :
                a.move(list_cell_current,(0,-1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN :
                a.move(list_cell_current,(0,1))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT :
                a.move(list_cell_current,(-1,0))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT :
                a.move(list_cell_current,(1,0))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x :
                for e in list_cell_current :
                    if a.pos in e.cells :
                        a.select(e)
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
                                a.select(e)
                    d= (mx-a.pos[0],my-a.pos[1])
                    if abs(d[0])+abs(d[1])>1 : a.selecting = False
                    if not a.move(list_cell_current,d) :
                        a.selecting = False
                        a.move(list_cell_current,d)
                    
            
        for x in list_cell_current:
            if type(x) == virus and x.cells[0] == (0,3):
                win = True
                going = False
                
        screen.blit(bg,(0,0))
        for i in list_cell_current:
            i.draw(screen,xoff,yoff,scalx,scaly)
        a.draw(screen,placement(a.pos))
        pygame.display.flip()
    if win == True :
        going = True
        font = pygame.font.SysFont(None, int(d[1]/8))
        c = font.render("Congrats",True,(0,255,0))
        screen.blit(c,(d[0]/5,d[1]/18))
        pygame.display.flip()
        while going :
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x :
                    going = False


def filetolevel(path):
    coord = (1,3)
    i=0
    tot=[]
    with open(path) as f :
        for line in f:
            x=coord[0]+((i+1)//2)
            y=coord[1]+(i//2)
            line = line.split()
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
    level(screen, [virus((4,3))])
    pygame.quit()


