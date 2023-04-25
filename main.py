import pygame
import level as lv

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

class Bouton_menu(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Menu')

    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.rect[0]+self.rect[2],self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3),self.y),(int(2*self.longueur/3),int(self.longueur/2))))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y+int(self.longueur/12)),(int(self.longueur/3),int(self.longueur/3))))
            
class Bouton_next(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface,page_aide):
        super().__init__(x,y,rayon,couleur,surface,'Next')
        self.page_aide = page_aide

    def update(self):
        if self.page_aide == 1:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0]+40,self.y+44),(self.rect[0]+self.rect[2]+10,self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3)*1.8,self.y-20),(int(2*self.longueur/3),int(self.longueur/2))))
        if self.page_aide == 2:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0]+40,self.y+44),(self.rect[0]+self.rect[2]-90,self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3)+20,self.y-20),(int(2*self.longueur/3),int(self.longueur/2))))
            

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
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.longueur,int(self.longueur/2))),0,10)
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(3*self.longueur/8),self.y+int(3*self.longueur/24)),(int(3*self.longueur/4),int(self.longueur/12))))
            for i in range (2):
                for j in range (7):
                    pygame.draw.rect(self.surface,self.couleur,((self.x-int(5*self.longueur/12)+int(j*self.longueur/8),self.y-int(self.longueur/24)-int(3*i*self.longueur/24)),(int(self.longueur/12),int(self.longueur/12))))

        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(5*self.longueur/16),self.y-int(self.longueur/2)),(int(5*self.longueur/8),self.longueur)),border_radius=35,border_top_left_radius=25,border_top_right_radius=25)
            pygame.draw.line(self.surface,self.couleur,(self.x,self.rect[1]),(self.x,self.y-int(self.rayon/6)),int(self.rayon*0.05))
            pygame.draw.line(self.surface,self.couleur,(self.rect[0],self.y-int(self.rayon/6)),(self.rect[0]+self.rect[2],self.y-int(self.rayon/6)),int(self.rayon*0.05))

class Bouton_Musique(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Musique')

    def update(self):
        if pygame.mixer.music.get_busy() == True:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))

        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))
            pygame.draw.line(self.surface,(255,0,0),(self.rect[0]+int(0.9*self.rect[2]),self.rect[1]),(self.rect[0],self.rect[1]+int(0.9*self.rect[3])),int(self.rayon*0.1))

class Bouton_texte():
    def __init__(self,x,y,largeur,longueur,couleur,surface,nom,taille):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.longueur=longueur
        self.couleur=couleur
        self.surface=surface
        self.nom=nom
        self.taille=taille
        self.rect = pygame.Rect((self.x,self.y),(self.largeur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))
        self.texte=pygame.font.Font("verdana.ttf",int(self.taille/2)).render(self.nom,True,(255,255,255))

    def update(self):
        pygame.draw.rect(self.surface,self.couleur,(self.x,self.y,self.largeur,self.longueur),border_radius=int(self.longueur))
        self.surface.blit(self.texte,(self.x+int(self.largeur-self.texte.get_width())/2,self.y+int(self.longueur-self.texte.get_height())/2))

class Bouton_graphisme():
    def __init__(self,x,y,longueur,couleur,surface,taille):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.couleur=couleur
        self.surface=surface
        self.taille=taille
        self.rect = pygame.Rect((self.x,self.y),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))
        self.nom='Graphisme'
        self.texte=pygame.font.Font("verdana.ttf",int(self.taille/2)).render('Graphisme :',True,(0,0,0))

    def update(self):
        pygame.draw.rect(self.surface,self.couleur,(self.x,self.y,self.longueur,self.longueur),border_radius=int(self.longueur/8))
        self.surface.blit(self.texte,(self.x+int(self.longueur-self.texte.get_width())/2,self.y+int(self.longueur/10)))


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

    return [[niveau_1,niveau_2,niveau_3,niveau_4,niveau_5],
            [niveau_6,niveau_7,niveau_8,niveau_9,niveau_10],
            [Menu,Retour]]

def lancement(page,taille,surface,background,titre,controle_actuel,page_aide,autre_texte=None):
    
    if page == 'accueil':
        Logo = pygame.image.load('images/OUT.png').convert_alpha()
        Jouer = Bouton_texte(int(3.375*surface.get_width()/6-5*taille),int(6.5*surface.get_height()/10),6.5*taille,1.8*taille,(0, 255, 0),surface,"Jouer",2*taille)
        Options = Bouton_texte(int(2.25*surface.get_width()/6-5*taille),int(8*surface.get_height()/10),6.5*taille,1.8*taille,(0, 0, 255),surface,"Options",2*taille)
        Aide = Bouton_texte(int(4.5*surface.get_width()/6-5*taille),int(8*surface.get_height()/10),6.5*taille,1.8*taille,(255, 0, 0),surface,"Aide",2*taille)
        liste_boutons=[[Jouer,Aide,Options]]
        

    elif page=='options':
        Menu=Bouton_menu(int(2*surface.get_width()/9),int(4*surface.get_height()/9),2*taille,(255,255,255),surface)
        Eteindre=Bouton_éteindre(int(7*surface.get_width()/18),int(4*surface.get_height()/9),2*taille,(255,0,0),surface)
        Commande=Bouton_commande(int(2*surface.get_width()/9),int(7*surface.get_height()/9),2*taille,(255,255,255),surface,controle_actuel)
        Musique=Bouton_Musique(int(7*surface.get_width()/18),int(7*surface.get_height()/9),2*taille,(255,255,255),surface)
        Graphisme=Bouton_graphisme(int(3*surface.get_width()/4-7*taille),int(7*surface.get_height()/12-7*taille),14*taille,(255,255,255),surface,3*taille)
        liste_boutons=[[Menu,Eteindre,Graphisme],[Commande,Musique,Graphisme]]

    elif page=='aide':
        Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
        if page_aide == 1:
            Next=Bouton_next(int(30.5*taille),int(10.1*taille),taille,(255,255,255),surface,page_aide)
        if page_aide == 2:
            Next=Bouton_next(int(1.5*taille),int(10.1*taille),taille,(255,255,255),surface,page_aide)
            
        liste_boutons=[[Menu],[Next]]
    
    elif page=='difficulté':
        Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
        Starter=Bouton_texte(int(surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(0,250,0),surface,'Starter',3*taille)
        Junior=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(225,175,45),surface,'Junior',3*taille)
        Master=Bouton_texte(int(surface.get_width()/6-5*taille),int(7*surface.get_height()/10),10*taille,3*taille,(250,0,0),surface,'Master',3*taille)
        Expert=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(250,125,0),surface,'Expert',3*taille)
        Wizard=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),10*taille,3*taille,(0,0,250),surface,'Wizard',3*taille)
        Bonus=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(7*surface.get_size()[1]/10),10*taille,3*taille,(192,66,138),surface,'Bonus',3*taille)
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
                            return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide)

                        elif page=='difficulté':
                            if b.nom=='Starter':
                                return starter(surface,taille,background,controle_actuel,page_aide)
                            elif b.nom=='Junior':
                                return junior(surface,taille,background,controle_actuel,page_aide)
                            elif b.nom=='Expert':
                                return expert(surface,taille,background,controle_actuel,page_aide)
                            elif b.nom=='Master':
                                return master(surface,taille,background,controle_actuel,page_aide)
                            elif b.nom=='Wizard':
                                return wizard(surface,taille,background,controle_actuel,page_aide)
                            elif b.nom=='Bonus':
                                return bonus(surface,taille,background,controle_actuel,page_aide)

                        elif page=='accueil':
                            if b.nom=='Jouer':
                                return difficulte(surface,taille,controle_actuel,background,page_aide)
                            elif b.nom=='Options':
                                return options(surface,taille,controle_actuel,background,page_aide)
                            elif b.nom=='Aide':
                                return aide(surface,taille,controle_actuel,background,page_aide)
                        
                        elif page=='aide':
                            if page_aide == 1:
                                if b.nom=='Next':
                                    page_aide = 2
                                    aide(surface,taille,controle_actuel,background,page_aide)
                            elif page_aide == 2:
                                if b.nom=='Next':
                                    page_aide = 1
                                    aide(surface,taille,controle_actuel,background,page_aide)
                                
                        
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
                                if pygame.mixer.music.get_busy() == True:
                                    pygame.mixer.music.stop()
                                else:
                                    pygame.mixer.music.play(-1)

                        else:
                            if b.nom=='Retour':
                                return difficulte(surface,taille,controle_actuel,background,page_aide)
                            else :
                                lv.level(surface,lv.filetolevel(os.getcwd()+'/'+page+'/'+b.nom),0,taille)
                                if lv.home.x == 1:
                                    lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide)
                                

                            
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if controle_actuel=='souris':
                    for rang in liste_boutons:
                        for bouton in rang:
                            if bouton.rect.collidepoint(event.pos):
                                if bouton.nom=='Menu':
                                    return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide)

                                elif page=='difficulté':
                                    if bouton.nom=='Starter':
                                        return starter(surface,taille,background,controle_actuel,page_aide)
                                    elif bouton.nom=='Junior':
                                        return junior(surface,taille,background,controle_actuel,page_aide)
                                    elif bouton.nom=='Expert':
                                        return expert(surface,taille,background,controle_actuel,page_aide)
                                    elif bouton.nom=='Master':
                                        return master(surface,taille,background,controle_actuel,page_aide)
                                    elif bouton.nom=='Wizard':
                                        return wizard(surface,taille,background,controle_actuel,page_aide)
                                    elif bouton.nom=='Bonus':
                                        return bonus(surface,taille,background,controle_actuel,page_aide)
                                
                                
                                elif page=='accueil':
                                    if bouton.nom=='Jouer':
                                        return difficulte(surface,taille,controle_actuel,background,page_aide)
                                    elif bouton.nom=='Options':
                                        return options(surface,taille,controle_actuel,background,page_aide)
                                    elif bouton.nom=='Aide':
                                        return aide(surface,taille,controle_actuel,background,page_aide)
                                
                                elif page=='aide':
                                    if page_aide == 1:
                                        if bouton.nom=='Next':
                                            page_aide = 2
                                            aide(surface,taille,controle_actuel,background,page_aide)
                                    elif page_aide == 2:
                                        if bouton.nom=='Next':
                                            page_aide = 1
                                            aide(surface,taille,controle_actuel,background,page_aide)
                                            
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
                                        if pygame.mixer.music.get_busy() == True:
                                            pygame.mixer.music.stop()
                                        else:
                                            pygame.mixer.music.play(-1)
                                else:
                                    if bouton.nom=='Retour':
                                        return difficulte(surface,taille,controle_actuel,background)
                                    else :
                                        lv.level(surface,lv.filetolevel(os.getcwd()+'/'+page+'/'+bouton.nom),0,taille)
                                        
                                    

        surface.blit(background,(0,0))
        if page == 'accueil':
            logo = pygame.transform.scale(Logo, (10*taille,10*taille))
            surface.blit(logo,(int((surface.get_width()-logo.get_width())/1.95),int(0.75*surface.get_height()/15)))
            
        if page == 'aide':    
            pygame.draw.rect(surface,(255,255,255),(int(1.25*surface.get_width()/4-7*taille),int(7*surface.get_height()/12-7*taille),26*taille,14*taille),border_radius=int(14*taille/8))
            if page_aide == 1:
                surface.blit(pygame.font.SysFont("verdana.ttf",2*taille).render('Règle du Jeu :',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/2.25),int(4*surface.get_height()/18)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('Le but de Molecule Out est de faire sortire la molecule rouge du plateau avec des mouvement en diagonale.',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('Les molecules ne peuvent être tourné et la molecule seul (gris par défaut) ne peuvent pas être bougé.',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/9)))            
            elif page_aide == 2:
                surface.blit(pygame.font.SysFont("verdana.ttf",2*taille).render('Contrôles :',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/2.05),int(4*surface.get_height()/18))) 
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('Flèche Directionnelles ou 7,9,1,3 pour se déplacer',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('R  pour recommencer le niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/9)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('ENTER, X, Z ou W pour sélectionner une molecule',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/7.9)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('TAB pour changer la sélection de bouton dans un niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/7.1)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('ESPACE pour sélectionner un bouton dans un niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/6.4)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('ECHAP pour quitter le jeu',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/5.8)))       
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('SUPPR pour retourner au menu de sélection',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/5.3)))
                surface.blit(pygame.font.Font("verdana.ttf",taille-33).render('A, Q ou 5 pour le changement de molecule rapide',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/6.5),int(4*surface.get_height()/4.9)))               
        if page=='options' or page=='aide':
            surface.blit(titre,(int((surface.get_width()-titre.get_width())/2),int(surface.get_height()/25)))
            
        elif page != 'accueil' and page != 'options':
            surface.blit(titre,(int((surface.get_width()-titre.get_width())/2),int(4*surface.get_height()/25)))
            
        

        if controle_actuel=='souris':
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)

            if b.nom=='Menu' or b.nom=='Eteindre' or b.nom=='Commande' or b.nom=='Retour' or b.nom=='Musique' or b.nom=='Next':
                pygame.draw.circle(surface,(100,100,100),(b.x,b.y),int(1.1*b.rayon))
                
            elif b.nom=='Graphisme':
                rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))
                pygame.draw.rect(surface,(100,100,100),rect_sel,0,int(b.longueur/8))

            else:
                rect_sel=pygame.Rect((b.rect[0]-int(taille/10),b.rect[1]-int(taille/10)),(b.rect[2]+2*int(taille/10),b.rect[3]+2*int(taille/10)))
                pygame.draw.rect(surface,(100,100,100),rect_sel,0,int(b.longueur))

        for rang in liste_boutons:
            for bouton in rang:
                bouton.update()

        pygame.display.update()

def starter(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('starter',taille,surface,background,titre,controle_actuel,page_aide)

def junior(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('junior',taille,surface,background,titre,controle_actuel,page_aide)

def expert(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('expert',taille,surface,background,titre,controle_actuel,page_aide)

def master(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('master',taille,surface,background,titre,controle_actuel,page_aide)

def wizard(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('wizard',taille,surface,background,titre,controle_actuel,page_aide)

def bonus(surface,taille,background,controle_actuel,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    lancement('bonus',taille,surface,background,titre,controle_actuel,page_aide)

def options(surface,taille,controle_actuel,background,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Options',True,(0,0,0))
    lancement('options',taille,surface,background,titre,controle_actuel,page_aide)

def aide(surface,taille,controle_actuel,background,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Aide',True,(0,0,0))
    lancement('aide',taille,surface,background,titre,controle_actuel,page_aide)

def difficulte(surface,taille,controle_actuel,background,page_aide):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez la difficulté',True,(0,0,0))
    lancement('difficulté',taille,surface,background,titre,controle_actuel,page_aide)

def main():
   pygame.init()
   pygame.display.set_caption("Molecule Out")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   taille=(min(screen.get_size()))//18
   pygame.mixer.music.load("son/Musique de fond.mp3")
   pygame.mixer.music.set_volume(30)
   pygame.mixer.music.stop()
   titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Logo',True,(0,0,0))
   controle_actuel='clavier'
   page_aide = 1
   background = pygame.image.load('images/back.png').convert_alpha()
   background = pygame.transform.scale(background, (screen.get_size()))
   background.convert()

   lancement('accueil',taille,screen,background,titre,controle_actuel,page_aide)
   pygame.quit()

main()
