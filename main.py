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

class Bouton_menu(Bouton_circulaire):
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
            pygame.draw.polygon(self.surface,(0,0,0),((self.rect[0]+int(self.rect[2]/2),self.rect[1]),(self.rect[0],self.rect[1]+int(self.rect[3]/2)),(self.rect[0]+self.rect[2],self.rect[1]+int(self.rect[3]/2))))
            pygame.draw.rect(self.surface,(0,0,0),((self.rect[0]+int(self.rect[2]/8),self.rect[1]+int(self.rect[3]/2)),(int(3*self.rect[2]/4),int(self.rect[3]/2))))
            pygame.draw.rect(self.surface,(255,255,255),((self.rect[0]+int(self.rect[2]/3),self.rect[1]+int(3*self.rect[2]/5)),(int(self.rect[2]/3),int(2*self.rect[3]/5))))

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

def bouton_text_arrondi(texte, couleur, x, y, largeur, hauteur, surface):
    font = pygame.font.Font("verdana.ttf", int((largeur, hauteur)[1]*0.5))
    pygame.draw.rect(surface, couleur, (x, y, largeur, hauteur), border_radius=int(hauteur//1))
    texte = font.render(texte, True, (255, 255, 255))
    surface.blit(texte, texte.get_rect(center=pygame.Rect(x, y, largeur, hauteur).center))

def la_liste_bouton(R,V,B, surface, taille):
    niveau_1=Bouton_rectangulaire(int(1.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'1',3*taille)
    niveau_2=Bouton_rectangulaire(int(2.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'2',3*taille)
    niveau_3=Bouton_rectangulaire(int(3.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'3',3*taille)
    niveau_4=Bouton_rectangulaire(int(4.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'4',3*taille)
    niveau_5=Bouton_rectangulaire(int(5.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'5',3*taille)
    niveau_6=Bouton_rectangulaire(int(1.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'6',3*taille)
    niveau_7=Bouton_rectangulaire(int(2.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'7',3*taille)
    niveau_8=Bouton_rectangulaire(int(3.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'8',3*taille)
    niveau_9=Bouton_rectangulaire(int(4.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'9',3*taille)
    niveau_10=Bouton_rectangulaire(int(5.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'10',3*taille)
    Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(250,250,250),surface,'Menu')

    liste_boutons=[[Menu],[niveau_1,niveau_2,niveau_3,niveau_4, niveau_5],[niveau_6,niveau_7,niveau_8,niveau_9, niveau_10]]
    return liste_boutons

def options(controle_actuel):
    if controle_actuel== 'sourie':
        return 'clavier'
    else:
        return 'sourie'


def aide():
    return

def lancement(niveau, taille, surface, background, titre,controle_actuel):
    Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(250,250,250),surface,'Menu')
    if niveau=='starter':
        R=0
        V=250
        B=0
    if niveau=='junior':
        R=225
        V=175
        B=45
    if niveau=='master':
        R=250
        V=0
        B=0
    if niveau=='expert':
        R=250
        V=125
        B=0
    if niveau=='wizard':
        R=0
        V=0
        B=250
    if niveau=='bonus':
        R=192
        V=66
        B=138
    if niveau=='aucun':
        Starter=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Starter',3*taille)
        Master=Bouton_rectangulaire(int(surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Master',3*taille)
        Junior=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Junior',3*taille)
        Wizard=Bouton_rectangulaire(int(3*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Wizard',3*taille)
        Expert=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Expert',3*taille)
        Bonus=Bouton_rectangulaire(int(5*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(250,250,250),surface,'Bonus',3*taille)
        liste_boutons=[[Menu],[Starter,Junior,Expert],[Master,Wizard,Bonus]]
    else:
        niveau_1=Bouton_rectangulaire(int(1.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'1',3*taille)
        niveau_2=Bouton_rectangulaire(int(2.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'2',3*taille)
        niveau_3=Bouton_rectangulaire(int(3.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'3',3*taille)
        niveau_4=Bouton_rectangulaire(int(4.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'4',3*taille)
        niveau_5=Bouton_rectangulaire(int(5.6*surface.get_size()[0]/6-5*taille),int(4*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'5',3*taille)
        niveau_6=Bouton_rectangulaire(int(1.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'6',3*taille)
        niveau_7=Bouton_rectangulaire(int(2.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'7',3*taille)
        niveau_8=Bouton_rectangulaire(int(3.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'8',3*taille)
        niveau_9=Bouton_rectangulaire(int(4.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'9',3*taille)
        niveau_10=Bouton_rectangulaire(int(5.6*surface.get_size()[0]/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,3*taille,(R,V,B),surface,'10',3*taille)
        liste_boutons=[[Menu],[niveau_1,niveau_2,niveau_3,niveau_4, niveau_5],[niveau_6,niveau_7,niveau_8,niveau_9, niveau_10]]

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
                elif controle_actuel=='clavier':
                    if event.key==pygame.K_RIGHT:
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

                    elif event.key==pygame.K_SPACE or event.key==pygame.K_RETURN:
                        if b.nom=='Menu':
                            return menu(surface,taille,controle_actuel,background)
                        elif b.nom=='Starter':
                            return starter(surface, taille,background,controle_actuel)
                        elif b.nom=='Junior':
                            return junior(surface, taille,background,controle_actuel)
                        if b.nom=='Expert':
                            return expert(surface, taille,background,controle_actuel)
                        elif b.nom=='Master':
                            return master(surface, taille,background,controle_actuel)
                        if b.nom=='Wizard':
                            return wizard(surface, taille,background,controle_actuel)
                        elif b.nom=='Bonus':
                            return bonus(surface, taille,background,controle_actuel)

                        elif b.nom=='1':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='2':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='3':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='4':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='5':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='6':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='7':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='8':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='9':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif b.nom=='10':
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """


            elif event.type==pygame.MOUSEBUTTONDOWN:
                if controle_actuel=='sourie' :
                    if Menu.rect.collidepoint(event.pos):
                        return menu(surface,taille,controle_actuel,background)
                    if niveau=='aucun':
                        if Starter.rect.collidepoint(event.pos):
                            return starter(surface, taille,background,controle_actuel)
                        elif Junior.rect.collidepoint(event.pos):
                            return junior(surface, taille,background,controle_actuel)
                        if Expert.rect.collidepoint(event.pos):
                            return expert(surface, taille,background,controle_actuel)
                        elif Master.rect.collidepoint(event.pos):
                            return master(surface, taille,background,controle_actuel)
                        if Wizard.rect.collidepoint(event.pos):
                            return wizard(surface, taille,background,controle_actuel)
                        elif Bonus.rect.collidepoint(event.pos):
                            return bonus(surface, taille,background,controle_actuel)
                    else:
                        if niveau_1.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_2.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_3.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_4.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_5.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_6.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_7.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_8.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_9.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

                        elif niveau_10.rect.collidepoint(event.pos):
                            if niveau=='starter':
                                return """retourner le niveau """
                            if niveau=='junior':
                                return """retourner le niveau """
                            if niveau=='expert':
                                return """retourner le niveau """
                            if niveau=='master':
                                return """retourner le niveau """
                            if niveau=='wizard':
                                return """retourner le niveau """
                            if niveau=='bonus':
                                return """retourner le niveau """

        surface.blit(background,(0,0))
        surface.blit(titre,(int((surface.get_size()[0]-titre.get_size()[0])/2),int(4*surface.get_size()[1]/25)))
        if controle_actuel=='sourie':
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)

            if i==0:
                pygame.draw.circle(surface,(100,100,100),(b.x,b.y), int(1.1*b.rayon))

            else:
                rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))
                pygame.draw.rect(surface,(100,100,100),rect_sel)

        for rang in liste_boutons:
            for bouton in rang:
                bouton.update()

        pygame.display.update()

def starter(surface, taille,background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('starter',taille, surface, background, titre,controle_actuel)

def junior(surface, taille, background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('junior',taille, surface, background, titre, controle_actuel)

def expert(surface, taille, background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('expert',taille, surface, background, titre,controle_actuel)

def master(surface, taille,background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('master',taille, surface, background, titre,controle_actuel)

def wizard(surface, taille,background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('wizard',taille, surface, background, titre,controle_actuel)

def bonus(surface, taille,background,controle_actuel):
    titre=pygame.font.SysFont(None,4*taille).render('Choisissez un niveau',True,(0, 0, 0))
    lancement('bonus',taille, surface, background, titre,controle_actuel)

def menu(surface,taille,controle_actuel,background):
    logo = pygame.image.load('images/OUT.png').convert_alpha()
    bouton_jouer = pygame.Rect(surface.get_width()*0.4, surface.get_height()*0.625, surface.get_width()*0.2, surface.get_height()*0.1)
    bouton_options = pygame.Rect(surface.get_width()*0.225, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1)
    bouton_aide = pygame.Rect(surface.get_width()*0.575, surface.get_height()*0.8, surface.get_width()*0.2, surface.get_height()*0.1)

    b=2

    running = True
    while running:
        surface.blit(background,(0,0))
        surface.blit(logo, (surface.get_width()*0.28, surface.get_height()*-0.05))
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
                elif controle_actuel == "clavier":
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
                            controle_actuel= options(controle_actuel)
                        elif b == 2:
                            return difficulte(surface, taille, controle_actuel, background)
                        elif b == 3:
                            return aide()

            elif controle_actuel == "sourie":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_jouer.collidepoint(event.pos):
                        return difficulte(surface, taille, controle_actuel, background)
                    elif bouton_options.collidepoint(event.pos):
                        controle_actuel=options(controle_actuel)
                    elif bouton_aide.collidepoint(event.pos):
                        return aide()

        if controle_actuel=='clavier':
            pygame.mouse.set_visible(False)
            if b == 1:
                pygame.draw.rect(surface,(100,100,100), bouton_options, 8,75)
            elif b == 2:
                pygame.draw.rect(surface,(100,100,100), bouton_jouer, 8,75)
            elif b == 3:
                pygame.draw.rect(surface,(100,100,100), bouton_aide, 8,75)
        else:
            pygame.mouse.set_visible(True)

        pygame.display.update()

def difficulte(surface,taille, controle_actuel,background):

    titre=pygame.font.SysFont(None,4*taille).render('Choisissez la difficulté',True,(0, 0, 0))
    lancement('aucun', taille, surface, background, titre, controle_actuel)

def main():
   pygame.init()
   pygame.display.set_caption("Anti-virus")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   taille=(min(screen.get_size()))//18
   controle_actuel='sourie'
   background = pygame.Surface(screen.get_size())
   background.fill((200,200,200))
   background.convert()

   menu(screen,taille,controle_actuel,background)
   pygame.quit()

main()
