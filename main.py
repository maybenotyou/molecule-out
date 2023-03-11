import pygame

def rectangle_inscrit(rayon):
    return int((2*(rayon**2))**0.5)

def carré_centré_dans_rectangle(x,y):
    if x==min(x,y):
        écart_x=0
        écart_y=(y-x)//2
        y=x
    elif y==min(x,y):
        écart_x=(x-y)//2
        écart_y=0
        x=y
    return x,y,écart_x,écart_y

def redimensionner(x1,y1,x2,y2):
    if x1/y1==x2/y2:
        x=x1
        y=y1
    elif x1/y1<x2/y2:
        x=x1
        y=int(y2*(x1/x2))
    else:
        x=int(x2*(y1/y2))
        y=y1
    return x,y
    
def main():
    pygame.init()
    pygame.display.set_caption("Anti-virus")
    screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    background,écart_x,écart_y=fond_d_écran(screen,"uni")
    commande="souris"
    taille=(min(screen.get_size()))//18

main()
