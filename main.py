import pygame
def rectangle_inscrit(rayon):
    return int((2*(rayon**2))**0.5)

class Bouton_circulaire():
    def __init__(self,x,y,rayon,couleur,surface):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.rayon=rayon
        self.surface=surface
        self.selectionné=False
        self.longueur=rectangle_inscrit(rayon)
        self.rect = pygame.Rect((self.x-(self.longueur//2),self.y-(self.longueur//2)),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y), self.rayon, 0)

class Bouton_rectangulaire():
    def __init__(self,x,y,hauteur,largeur,couleur,surface,nom,taille):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.hauteur=hauteur
        self.couleur=couleur
        self.surface=surface
        self.nom=nom
        self.taille=taille
        self.selectionné=False
        self.rect = pygame.Rect((self.x,self.y),(self.largeur,self.hauteur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))
        self.texte=pygame.font.SysFont(None,self.taille).render(self.nom,True,(0, 0, 0))

    def update(self):
            pygame.draw.rect(self.surface,self.couleur,self.rect)
            self.surface.blit(self.texte,(self.x+int(self.largeur-self.texte.get_size()[0])/2,self.y+int(self.hauteur-self.texte.get_size()[1])/2))

def starter():
   return

def junior():
   return

def expert():
   return

def maitre():
   return

def difficulte():
   return

def menu():
   return


def difficulte(surface,taille):
    background = pygame.Surface(surface.get_size())
    background.fill((200,200,200))
    background.convert()
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez la difficulté',True,(0, 0, 0))
    Starter=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Starter',3*taille)
    Junior=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Junior',3*taille)
    Expert=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Expert',3*taille)
    Master=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Master',3*taille)
    Wizard=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Wizard',3*taille)
    Bonus=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Bonus',3*taille)
    liste_boutons=[[Starter,Expert,Wizard],[Junior,Master,Bonus]]
    i=0
    j=0
    b=liste_boutons[i][j]
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                return
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    pygame.quit()
                    return

                elif event.key==pygame.K_RIGHT:
                    if j<len(liste_boutons[i])-1:
                        j+=1
                    else:
                        j=0
                    b=liste_boutons[i][j]

                elif event.key==pygame.K_LEFT:
                    if j>0:
                        j-=1
                    else:
                        j=len(liste_boutons[i])-1
                    b=liste_boutons[i][j]

                elif event.key==pygame.K_UP:
                    if i<len(liste_boutons)-1:
                        i+=1
                    else:
                        i=0
                    b=liste_boutons[i][j]

                elif event.key==pygame.K_DOWN:
                    if i>0:
                        i-=1
                    else:
                        i=len(liste_boutons)-1
                    b=liste_boutons[i][j]

                elif event.key==pygame.K_SPACE or event.key==pygame.K_RETURN:
                    if b.nom=='Starter':
                        return starter()
                    elif b.nom=='Junior':
                        return junior()
                    if b.nom=='Expert':
                        return expert()
                    elif b.nom=='Master':
                        return master()
                    if b.nom=='Wizard':
                        return wizard()
                    elif b.nom=='Bonus':
                        return bonus()

        rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))

        surface.blit(background,(0,0))
        surface.blit(titre,(int((surface.get_size()[0]-titre.get_size()[0])/2),int(surface.get_size()[1]/10)))

        pygame.draw.rect(surface,(100,100,100),rect_sel)

        Starter.update()
        Junior.update()
        Expert.update()
        Master.update()
        Wizard.update()
        Bonus.update()

        pygame.display.update()

def main():
   pygame.init()
   pygame.display.set_caption("Anti-virus")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   taille=(min(screen.get_size()))//18
   menu()
   
main()
