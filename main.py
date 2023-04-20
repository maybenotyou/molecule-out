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
        self.longueur=rectangle_inscrit(rayon)
        self.rect = pygame.Rect((self.x-(self.longueur//2),self.y-(self.longueur//2)),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)

class Bouton_menu(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Menu')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.rect[0]+self.rect[2],self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3),self.y),(int(2*self.longueur/3),int(self.longueur/2))))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y+int(self.longueur/12)),(int(self.longueur/3),int(self.longueur/3))))

class Bouton_éteindre(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Eteindre')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.circle(self.surface,(0,0,0),(self.x,self.y),int(self.longueur/2),int(self.longueur/8))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y-int(9*self.rayon/10)),(int(self.longueur/3),self.rayon)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/12),self.y-int(9*self.rayon/10)),(int(self.longueur/6),int(9*self.rayon/10))))

class Bouton_retour(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Retour')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.x,self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x,self.y-int(self.longueur/4)),(int(self.longueur/2),int(self.longueur/2))))

class Bouton_commande(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface,etat):
        super().__init__(x,y,rayon,couleur,surface,'Commande')
        self.etat=etat

    def update(self):
        if self.etat=="clavier":
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.longueur,int(self.longueur/2))),0,8)
        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(5*self.longueur/16),self.y-int(self.longueur/2)),(int(5*self.longueur/8),self.longueur)),0,80)
            pygame.draw.line(self.surface,self.couleur,(self.x,self.rect[1]),(self.x,self.y-int(self.rayon/6)),int(self.rayon*0.05))
            pygame.draw.line(self.surface,self.couleur,(self.rect[0],self.y-int(self.rayon/6)),(self.rect[0]+self.rect[2],self.y-int(self.rayon/6)),int(self.rayon*0.05))

class Bouton_Musique(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface,son):
        super().__init__(x,y,rayon,couleur,surface,'Musique')
        self.son=son

    def update(self):
        if self.son:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))

        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))
            pygame.draw.line(self.surface,(255,0,0),(self.rect[0]+int(0.9*self.rect[2]),self.rect[1]),(self.rect[0],self.rect[1]+int(0.9*self.rect[3])),int(self.rayon*0.1))

class Bouton_texte():
    def __init__(self,x,y,hauteur,largeur,couleur,surface,nom,taille):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.hauteur=hauteur
        self.couleur=couleur
        self.surface=surface
        self.nom=nom
        self.taille=taille
        self.rect = pygame.Rect((self.x,self.y),(self.largeur,self.hauteur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))
        self.texte=pygame.font.Font("verdana.ttf",int(self.hauteur*0.5)).render(self.nom,True,(255,255,255))

    def update(self):
        pygame.draw.rect(self.surface,self.couleur,(self.x,self.y,self.largeur,self.hauteur),border_radius=self.hauteur)
        self.surface.blit(self.texte,(self.x+int(self.largeur-self.texte.get_width())/2,self.y+int(self.hauteur-self.texte.get_height())/2))

def bouton_text_arrondi(texte,couleur,x,y,largeur,hauteur,surface):
    font = pygame.font.Font("verdana.ttf",int((largeur,hauteur)[1]*0.5))
    pygame.draw.rect(surface,couleur,(x,y,largeur,hauteur),border_radius=int(hauteur//1))
    texte = font.render(texte,True,(255,255,255))
    surface.blit(texte,texte.get_rect(center=pygame.Rect(x,y,largeur,hauteur).center))

def la_liste_bouton(R,V,B,surface,taille):
    niveau_1=Bouton_texte(int(1.6*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'1',3*taille)
    niveau_2=Bouton_texte(int(2.6*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'2',3*taille)
    niveau_3=Bouton_texte(int(3.6*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'3',3*taille)
    niveau_4=Bouton_texte(int(4.6*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'4',3*taille)
    niveau_5=Bouton_texte(int(5.6*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'5',3*taille)
    niveau_6=Bouton_texte(int(1.6*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'6',3*taille)
    niveau_7=Bouton_texte(int(2.6*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'7',3*taille)
    niveau_8=Bouton_texte(int(3.6*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'8',3*taille)
    niveau_9=Bouton_texte(int(4.6*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'9',3*taille)
    niveau_10=Bouton_texte(int(5.6*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,3*taille,(R,V,B),surface,'10',3*taille)
    Menu=Bouton_menu(4*taille,int(1.5*taille),taille,(255,255,255),surface)
    Retour=Bouton_retour(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)

    liste_boutons=[[niveau_1,niveau_2,niveau_3,niveau_4,niveau_5],[niveau_6,niveau_7,niveau_8,niveau_9,niveau_10],[Menu,Retour]]
    return liste_boutons

def lancement(page,taille,surface,background,titre,controle_actuel):

    if page=='options':
        Menu=Bouton_menu(int(7*surface.get_width()/18),int(4*surface.get_height()/9),2*taille,(255,255,255),surface)
        Eteindre=Bouton_éteindre(int(11*surface.get_width()/18),int(4*surface.get_height()/9),2*taille,(255,0,0),surface)
        Commande=Bouton_commande(int(7*surface.get_width()/18),int(7*surface.get_height()/9),2*taille,(255,255,255),surface,controle_actuel)
        Musique=Bouton_Musique(int(11*surface.get_width()/18),int(7*surface.get_height()/9),2*taille,(255,255,255),surface,True)
        liste_boutons=[[Menu,Eteindre],[Commande,Musique]]

    elif page=='difficulté':
        Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
        Starter=Bouton_texte(int(surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,10*taille,(0,250,0),surface,'Starter',3*taille)
        Junior=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,10*taille,(225,175,45),surface,'Junior',3*taille)
        Master=Bouton_texte(int(surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,10*taille,(250,0,0),surface,'Master',3*taille)
        Expert=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),3*taille,10*taille,(250,125,0),surface,'Expert',3*taille)
        Wizard=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),3*taille,10*taille,(0,0,250),surface,'Wizard',3*taille)
        Bonus=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(7*surface.get_size()[1]/10),3*taille,10*taille,(192,66,138),surface,'Bonus',3*taille)
        liste_boutons=[[Starter,Junior,Expert],[Master,Wizard,Bonus],[Menu]]

    else:
        if page=='starter':
            R=0
            V=250
            B=0
        elif page=='junior':
            R=225
            V=175
            B=45
        elif page=='master':
            R=250
            V=0
            B=0
        elif page=='expert':
            R=250
            V=125
            B=0
        elif page=='wizard':
            R=0
            V=0
            B=250
        elif page=='bonus':
            R=192
            V=66
            B=138

        liste_boutons=la_liste_bouton(R,V,B,surface,taille)

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
                            i-=1
                        else:
                            i=len(liste_boutons)-1
                        if j>len(liste_boutons[i])-1:
                            j=len(liste_boutons[i])-1
                        b=liste_boutons[i][j]

                    elif event.key==pygame.K_DOWN:
                        if i<len(liste_boutons)-1:
                            i+=1
                        else:
                            i=0
                        if j>len(liste_boutons[i])-1:
                            j=len(liste_boutons[i])-1
                        b=liste_boutons[i][j]

                    elif event.key==pygame.K_SPACE or event.key==pygame.K_RETURN:
                        if b.nom=='Menu':
                            return menu(surface,taille,controle_actuel,background)

                        elif page=='difficulté':
                            if b.nom=='Starter':
                                return starter(surface,taille,background,controle_actuel)
                            elif b.nom=='Junior':
                                return junior(surface,taille,background,controle_actuel)
                            elif b.nom=='Expert':
                                return expert(surface,taille,background,controle_actuel)
                            elif b.nom=='Master':
                                return master(surface,taille,background,controle_actuel)
                            elif b.nom=='Wizard':
                                return wizard(surface,taille,background,controle_actuel)
                            elif b.nom=='Bonus':
                                return bonus(surface,taille,background,controle_actuel)

                        elif page=='options':
                            if b.nom=='Commande':
                                if controle_actuel=='souris':
                                    controle_actuel='clavier'
                                    Commande.etat='clavier'
                                else:
                                    controle_actuel='souris'
                                    Commande.etat='souris'
                            elif b.nom=='Eteindre':
                                return
                            elif b.nom=="Musique":
                                if b.son:
                                    b.son=False
                                else:
                                    b.son=True

                        else:
                            if b.nom=='Retour':
                                return difficulte(surface,taille,controle_actuel,background)
                            if b.nom=='1':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='2':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='3':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='4':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='5':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='6':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='7':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='8':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='9':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """

                            elif b.nom=='10':
                                if page=='starter':
                                    return """retourner le niveau """
                                if page=='junior':
                                    return """retourner le niveau """
                                if page=='expert':
                                    return """retourner le niveau """
                                if page=='master':
                                    return """retourner le niveau """
                                if page=='wizard':
                                    return """retourner le niveau """
                                if page=='bonus':
                                    return """retourner le niveau """


            elif event.type==pygame.MOUSEBUTTONDOWN:
                if controle_actuel=='souris':
                    for rang in liste_boutons:
                        for bouton in rang:
                            if bouton.rect.collidepoint(event.pos):
                                if bouton.nom=='Menu':
                                    return menu(surface,taille,controle_actuel,background)

                                elif page=='difficulté':
                                    if bouton.nom=='Starter':
                                        return starter(surface,taille,background,controle_actuel)
                                    elif bouton.nom=='Junior':
                                        return junior(surface,taille,background,controle_actuel)
                                    elif bouton.nom=='Expert':
                                        return expert(surface,taille,background,controle_actuel)
                                    elif bouton.nom=='Master':
                                        return master(surface,taille,background,controle_actuel)
                                    elif bouton.nom=='Wizard':
                                        return wizard(surface,taille,background,controle_actuel)
                                    elif bouton.nom=='Bonus':
                                        return bonus(surface,taille,background,controle_actuel)

                                elif page=='options':
                                    if bouton.nom=='Commande':
                                        if controle_actuel=='souris':
                                            controle_actuel='clavier'
                                            Commande.etat='clavier'
                                        else:
                                            controle_actuel='souris'
                                            Commande.etat='souris'
                                    elif bouton.nom=='Eteindre':
                                        return
                                    elif bouton.nom=='Musique':
                                        if bouton.son:
                                            bouton.son=False
                                        else:
                                            bouton.son=True
                                else:
                                    if bouton.nom=='Retour':
                                        return difficulte(surface,taille,controle_actuel,background)
                                    elif bouton.nom=='1':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='2':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='3':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='4':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='5':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='6':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='7':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='8':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='9':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

                                    elif bouton.nom=='10':
                                        if page=='starter':
                                            return """retourner le niveau """
                                        elif page=='junior':
                                            return """retourner le niveau """
                                        elif page=='expert':
                                            return """retourner le niveau """
                                        elif page=='master':
                                            return """retourner le niveau """
                                        elif page=='wizard':
                                            return """retourner le niveau """
                                        elif page=='bonus':
                                            return """retourner le niveau """

        surface.blit(background,(0,0))
        surface.blit(titre,(int((surface.get_width()-titre.get_width())/2),int(4*surface.get_height()/25)))
        if controle_actuel=='souris':
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)

            if b.nom=='Menu' or b.nom=='Eteindre' or b.nom=='Commande' or b.nom=='Retour' or b.nom=='Musique':
                pygame.draw.circle(surface,(100,100,100),(b.x,b.y),int(1.1*b.rayon))

            else:
                rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))
                pygame.draw.rect(surface,(100,100,100),rect_sel,0,75)

        for rang in liste_boutons:
            for bouton in rang:
                bouton.update()

        pygame.display.update()

def starter(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('starter',taille,surface,background,titre,controle_actuel)

def junior(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('junior',taille,surface,background,titre,controle_actuel)

def expert(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('expert',taille,surface,background,titre,controle_actuel)

def master(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('master',taille,surface,background,titre,controle_actuel)

def wizard(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('wizard',taille,surface,background,titre,controle_actuel)

def bonus(surface,taille,background,controle_actuel):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('bonus',taille,surface,background,titre,controle_actuel)

def menu(surface,taille,controle_actuel,background):
    logo = pygame.image.load('images/OUT.png').convert_alpha()
    bouton_jouer = pygame.Rect(surface.get_width()*0.4,surface.get_height()*0.625,surface.get_width()*0.2,surface.get_height()*0.1)
    bouton_options = pygame.Rect(surface.get_width()*0.225,surface.get_height()*0.8,surface.get_width()*0.2,surface.get_height()*0.1)
    bouton_aide = pygame.Rect(surface.get_width()*0.575,surface.get_height()*0.8,surface.get_width()*0.2,surface.get_height()*0.1)

    b=2

    running = True
    while running:
        surface.blit(background,(0,0))
        surface.blit(logo,(surface.get_width()*0.28,surface.get_height()*-0.05))
        bouton_text_arrondi("Jouer",(0,255,0),surface.get_width()*0.4,surface.get_height()*0.625,surface.get_width()*0.2,surface.get_height()*0.1,surface)
        bouton_text_arrondi("Options",(0,0,255),surface.get_width()*0.225,surface.get_height()*0.8,surface.get_width()*0.2,surface.get_height()*0.1,surface)
        bouton_text_arrondi("Aide",(255,0,0),surface.get_width()*0.575,surface.get_height()*0.8,surface.get_width()*0.2,surface.get_height()*0.1,surface)
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
                        else:
                            b -= 1

                    elif event.key == pygame.K_RIGHT:
                        if b == 3:
                            b = 1
                        else:
                            b += 1

                    elif event.key in [pygame.K_SPACE,pygame.K_RETURN]:
                        if b == 1:
                            return options(surface,taille,controle_actuel,background)
                        elif b == 2:
                            return difficulte(surface,taille,controle_actuel,background)
                        elif b == 3:
                            return aide(surface,taille,controle_actuel,background)

            elif controle_actuel == "souris":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_jouer.collidepoint(event.pos):
                        return difficulte(surface,taille,controle_actuel,background)
                    elif bouton_options.collidepoint(event.pos):
                        return options(surface,taille,controle_actuel,background)
                    elif bouton_aide.collidepoint(event.pos):
                        return aide(surface,taille,controle_actuel,background)

        if controle_actuel=='clavier':
            pygame.mouse.set_visible(False)
            if b == 1:
                pygame.draw.rect(surface,(100,100,100),bouton_options,8,75)
            elif b == 2:
                pygame.draw.rect(surface,(100,100,100),bouton_jouer,8,75)
            elif b == 3:
                pygame.draw.rect(surface,(100,100,100),bouton_aide,8,75)
        else:
            pygame.mouse.set_visible(True)

        pygame.display.update()

def options(surface,taille,controle_actuel,background):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Options',True,(0,0,0))
    lancement('options',taille,surface,background,titre,controle_actuel)

def aide(surface,taille,controle_actuel,background):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Aide',True,(0,0,0))
    return

def difficulte(surface,taille,controle_actuel,background):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez la difficulté',True,(0,0,0))
    lancement('difficulté',taille,surface,background,titre,controle_actuel)

def main():
   pygame.init()
   pygame.display.set_caption("Molecule Out")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   taille=(min(screen.get_size()))//18
   controle_actuel='clavier'
   background = pygame.Surface(screen.get_size())
   background.fill((200,200,200))
   background.convert()

   menu(screen,taille,controle_actuel,background)
   pygame.quit()

main()
