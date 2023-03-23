import pygame

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
        self.selectionné=False
        self.longueur=rectangle_inscrit(rayon)
        self.rect = pygame.Rect((self.x-(self.longueur//2),self.y-(self.longueur//2)),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y), self.rayon)
            
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

def options():
    return

def aide():
    return

def starter():
    return

def junior():
    return

def expert():
    return

def master():
    return

def wizard():
    return

def bonus():
    return


def difficulte(surface,taille,background):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez la difficulté',True,(0, 0, 0))

    Starter=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Starter',3*taille)
    Junior=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Junior',3*taille)
    Expert=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Expert',3*taille)
    Master=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Master',3*taille)
    Wizard=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Wizard',3*taille)
    Bonus=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Bonus',3*taille)
    Menu=Bouton_circulaire(int(1.5*taille),int(1.5*taille),taille,(250,250,250),surface,'Menu')

    liste_boutons=[[Menu],[Starter,Expert,Wizard],[Junior,Master,Bonus]]
    i=1
    j=1
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
                    if i>0:
                        if i==1:
                            j=0
                        i-=1
                    else:
                        i=len(liste_boutons)-1
                    b=liste_boutons[i][j]

                elif event.key==pygame.K_DOWN:
                    if i<len(liste_boutons)-1:
                        i+=1
                    else:
                        i=0
                        j=0
                    b=liste_boutons[i][j]

                elif event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                    if b.nom == 'Bonus':
                        return bonus()

                    elif b.nom == 'Expert':
                        return expert()
                    elif b.nom == 'Junior':
                        return junior()
                    elif b.nom == 'Master':
                        return master()
                    elif b.nom == 'Menu':
                        return main()
                    elif b.nom == 'Starter':
                        return starter()
                    elif b.nom == 'Wizard':
                        return wizard()
        surface.blit(background,(0,0))
        surface.blit(titre,(int((surface.get_size()[0]-titre.get_size()[0])/2),int(4*surface.get_size()[1]/25)))

        if i==0:
            pygame.draw.circle(surface,(100,100,100),(b.x,b.y), int(1.1*b.rayon))

        else:
            rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))
            pygame.draw.rect(surface,(100,100,100),rect_sel)

        for rang in liste_boutons:
            for bouton in rang:
                bouton.update()

        pygame.display.update()


def menu(surface,background,taille):
    logo = pygame.image.load('images/OUT.png').convert_alpha()
    bouton_jouer = pygame.Rect(surface.get_width()*0.4, surface.get_height()*0.625, surface.get_width()*0.2, surface.get_height()*0.1)
    bouton_options = pygame.Rect(surface.get_width()*0.225, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1)
    bouton_aide = pygame.Rect(surface.get_width()*0.575, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1)
    b = 2
    controle = "Clavier"
    running = True
    while running:
        surface.blit(background,(0,0))
        surface.blit(logo, (surface.get_width()*0.345, surface.get_height()*0.05))
        bouton_text_arrondi("Jouer", (0, 255, 0), surface.get_width()*0.4, surface.get_height()*0.625, surface.get_width()*0.2, surface.get_height()*0.1, surface)
        bouton_text_arrondi("Options", (0, 0, 255), surface.get_width()*0.225, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1, surface)
        bouton_text_arrondi("Aide", (255, 0, 0), surface.get_width()*0.575, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1, surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif controle == "Clavier":
                    if event.key == pygame.K_LEFT:
                        if b == 1:
                            b = 3
                        elif b == 3:
                            b = 2
                        elif b == 2:
                            b = 1

                    elif event.key == pygame.K_RIGHT:
                        if b == 3:
                            b = 1
                        elif b == 1:
                            b = 2
                        elif b == 2:
                            b = 3

                    elif event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                        if b == 1:
                            return options()
                        elif b == 2:
                            return difficulte(surface, taille, background)
                        elif b == 3:
                            return aide()

            elif controle == "Sourie":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_jouer.collidepoint(event.pos):
                        difficulte(surface, taille, background)
                    elif bouton_options.collidepoint(event.pos):
                        options()
                    elif bouton_aide.collidepoint(event.pos):
                        aide()

        if b == 1:
            pygame.draw.rect(surface,(100,100,100), bouton_options, 14,75)
        elif b == 2:
            pygame.draw.rect(surface,(100,100,100), bouton_jouer, 14,75)
        elif b == 3:
            pygame.draw.rect(surface,(100,100,100), bouton_aide, 14,75)

        pygame.display.update()
            

def bouton_text_arrondi(texte, couleur, x, y, largeur, hauteur, surface):
    font = pygame.font.Font("verdana.ttf", int((largeur, hauteur)[1]*0.5))
    pygame.draw.rect(surface, couleur, (x, y, largeur, hauteur), border_radius=int(hauteur//2))
    texte = font.render(texte, True, (255, 255, 255))
    surface.blit(texte, texte.get_rect(center=pygame.Rect(x, y, largeur, hauteur).center))

def main():
    pygame.init()
    pygame.display.set_caption("Molécule out")
    screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    background = pygame.Surface(screen.get_size())
    background.fill((200,200,200))
    background.convert()
    taille=(min(screen.get_size()))//18
    return menu(screen,background,taille)

main()