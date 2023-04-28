###importation de pygame, des fichiers level et cellule puis random pour pouvoir utiliser l'aléatoire (notamment pour les niveaux bonus)
import pygame
import level as lv
from cellule import *
from random import choice


import os

#cette fonction permet de retourner la longueur du coté d'un carré inscrit dans un cercle a partir de son rayon
def rectangle_inscrit(rayon):
    return int((2*(rayon**2))**0.5)

#cette classe crée des boutons de forme ronde
class Bouton_circulaire():
    def __init__(self,x,y,rayon,couleur,surface,nom):
        #coordonée du bouton
        self.x=x 
        self.y=y
        #sa couleur, son rayon, la surface ou ce bouton est visible et son nom
        self.couleur=couleur
        self.rayon=rayon
        self.surface=surface
        self.nom=nom
        #appel la fonction rectangle inscrit
        self.longueur=rectangle_inscrit(rayon)
        # création de la partie du bouton sur laquelle on peut cliquer pour entrainer son action (soit la surface dans le réctrangle inscrit)
        self.rect = pygame.Rect((self.x-(self.longueur//2),self.y-(self.longueur//2)),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))

        #dessine le  bouton circulaire a partir de ses attributs
    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)

#cette classe est une classe fille de bouton_circulaire permettant de créer le bouton pour retrouner au Menu
class Bouton_menu(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Menu')
    
    #dessine le bouton, ainsi que  son logo (la maison au centre: pour le distinguer et reconnaitre facilement )
    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.rect[0]+self.rect[2],self.y)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/3),self.y),(int(2*self.longueur/3),int(self.longueur/2))))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y+int(self.longueur/12)),(int(self.longueur/3),int(self.longueur/3))))
            
#cette classe est une classe fille de bouton_circulaire permettant de créer le bouton pour changer de page dans le menu aide
class Bouton_next(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface,page_aide):
        super().__init__(x,y,rayon,couleur,surface,'Next')
        self.page_aide = page_aide
    
    #dessine le bouton, ainsi que la flèche en son centre(la flèche change de sens en fonction de si l'on revient en arrière ou si l'on va a la page suivante)
    def update(self):
        if self.page_aide == 1:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0]+self.rect[2],self.y),(self.x,self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(int(self.longueur/2),int(self.longueur/2))))
        if self.page_aide == 2:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.x,self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x,self.y-int(self.longueur/4)),(int(self.longueur/2),int(self.longueur/2))))

#cette classe est une classe fille de bouton_circulaire permettant de créer le bouton pour fermer le jeu, il se trouve dans le menu option
class Bouton_éteindre(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Eteindre')
#dessine le bouton en rouge, ainsi que le logo au centre (celui génralement utiliser a cet effet: le cercle avec un petite barre verticale a son sommet)
    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.circle(self.surface,(0,0,0),(self.x,self.y),int(self.longueur/2),int(self.longueur/8))
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(self.longueur/6),self.y-int(9*self.rayon/10)),(int(self.longueur/3),self.rayon)))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/12),self.y-int(9*self.rayon/10)),(int(self.longueur/6),int(9*self.rayon/10))))

#cette classe est une classe fille de bouton_circulaire permettant de créer le bouton pour revenir au menu de choix de difficulté depuis le menu de selection de niveau
class Bouton_retour(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Retour')
        
#dessine le bouton, ainsi que la flèche (orienté vers la gauche) en son centre
    def update(self):
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x,self.rect[1]),(self.rect[0],self.y),(self.x,self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x,self.y-int(self.longueur/4)),(int(self.longueur/2),int(self.longueur/2))))

#cette classe est une classe fille de bouton_circulaire et permet de créer le bouton pour passer de commande clavier a souris (disponible dans le menu option)
class Bouton_commande(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface,etat):
        super().__init__(x,y,rayon,couleur,surface,'Commande')
        self.etat=etat

    #dessine le bouton, ainsi qu'un clavier (si l'on est en commande clavier) en son centre
    def update(self):
        if self.etat=="clavier":
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.longueur,int(self.longueur/2))),0,10)
            pygame.draw.rect(self.surface,self.couleur,((self.x-int(3*self.longueur/8),self.y+int(3*self.longueur/24)),(int(3*self.longueur/4),int(self.longueur/12))))
            for i in range (2):
                for j in range (7):
                    pygame.draw.rect(self.surface,self.couleur,((self.x-int(5*self.longueur/12)+int(j*self.longueur/8),self.y-int(self.longueur/24)-int(3*i*self.longueur/24)),(int(self.longueur/12),int(self.longueur/12))))

  #dessine le bouton, ainsi qu'une souris (si l'on es en comande souris) en son centre
        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(5*self.longueur/16),self.y-int(self.longueur/2)),(int(5*self.longueur/8),self.longueur))border_radius=int(self.longueur/2),border_top_left_radius=int(self.longueur/3),border_top_right_radius=int(self.longueur/3))
            pygame.draw.line(self.surface,self.couleur,(self.x,self.rect[1]),(self.x,self.y-int(self.rayon/6)),int(self.rayon*0.05))
            pygame.draw.line(self.surface,self.couleur,(self.rect[0],self.y-int(self.rayon/6)),(self.rect[0]+self.rect[2],self.y-int(self.rayon/6)),int(self.rayon*0.05))

 # cette classe est une classe fille de bouton_circulaire et permet de créer le bouton pour allumer et éteindre le son
class Bouton_Musique(Bouton_circulaire):
    def __init__(self,x,y,rayon,couleur,surface):
        super().__init__(x,y,rayon,couleur,surface,'Musique')

#dessine le bouton, ainsi que le logo de musique (haut parleur) (si la musique est activé)
    def update(self):
        if pygame.mixer.music.get_busy() == True:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))
            
#rajoute au bouton et au logo de haut parleur un trait oblique rouge pour signifier que le son est coupé (si la musique est désactivé)
        else:
            pygame.draw.circle(self.surface,self.couleur,(self.x,self.y),self.rayon)
            pygame.draw.polygon(self.surface,(0,0,0),((self.x+int(3*self.rayon/8),self.rect[1]),(self.rect[0],self.y),(self.x+int(3*self.rayon/8),self.rect[1]+self.rect[3])))
            pygame.draw.rect(self.surface,(0,0,0),((self.x-int(self.longueur/2),self.y-int(self.longueur/4)),(self.rayon,int(self.longueur/2))))
            pygame.draw.line(self.surface,(255,0,0),(self.rect[0]+int(0.9*self.rect[2]),self.rect[1]),(self.rect[0],self.rect[1]+int(0.9*self.rect[3])),int(self.rayon*0.1))

#cette classe crée des boutons avec du texte a l'interieur
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

    #dessine le bouton ainsi que le texte qui y est inscrit
    def update(self):
        pygame.draw.rect(self.surface,self.couleur,(self.x,self.y,self.largeur,self.longueur),border_radius=int(self.longueur))
        self.surface.blit(self.texte,(self.x+int(self.largeur-self.texte.get_width())/2,self.y+int(self.longueur-self.texte.get_height())/2))
        
# cette classe crée le bouton pour changer les graphismes du jeu (graphisme du plateau de jeu) avec l'exemple du virus (ce bouton se trouve dans le menu option)
class Bouton_graphisme():
    def __init__(self,x,y,longueur,couleur,surface,taille,graphisme):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.couleur=couleur
        self.surface=surface
        self.taille=taille
        self.graphisme=graphisme
        self.rect = pygame.Rect((self.x,self.y),(self.longueur,self.longueur))
        self.surface_bouton=pygame.Surface((self.rect[2],self.rect[3]))
        self.set_virus()
        self.nom='Graphisme'
        self.texte=pygame.font.Font("verdana.ttf",int(self.taille/2)).render('Graphisme :',True,(0,0,0))

    #crée le design virus en fonction du
    def set_virus(self) :
        self.virus = virus((0,0))
        self.virus.set_image(self.longueur/4,self.longueur/5,self.graphisme)

    #change le graphisme du jeu et du virus exemple
    def change_graphisme(self):
        self.graphisme+=1
        if self.graphisme>1:
            self.graphisme=0
        self.set_virus()

#dessin le bouton de changement d'esthétique et la molecule du virus (en fonction du design choisi)
    def update(self):
        pygame.draw.rect(self.surface,self.couleur,(self.x,self.y,self.longueur,self.longueur),border_radius=int(self.longueur/8))
        pygame.draw.rect(self.surface,(150,150,150),(self.x+int((self.longueur/10+1.1*self.texte.get_height())/2),self.y+(int(self.longueur/10+4*self.texte.get_height()/3)),self.longueur-(int(self.longueur/10+1.1*self.texte.get_height())),self.longueur-(int(self.longueur/10+2*self.texte.get_height()))),border_radius=int(self.longueur/8))
        self.surface.blit(self.texte,(self.x+int(self.longueur-self.texte.get_width())/2,self.y+int(self.longueur/10)))
        self.virus.draw(self.surface,self.x-self.longueur/4,self.y,0,0)

#cette fonction permet de créer  tous les boutons pour sélectionner son niveau et ce qu'importe le niveau de difficulté choisi (cependant la couleur et le niveau retourné changent en fonction de cette dernière)
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
    #créer les boutons menu et retour
    Menu=Bouton_menu(4*taille,int(1.5*taille),taille,(255,255,255),surface)
    Retour=Bouton_retour(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
#retourne un tableau de tableau permetant en format clavier de séléctioner le bon bouton/niveau
    return [[niveau_1,niveau_2,niveau_3,niveau_4,niveau_5],
            [niveau_6,niveau_7,niveau_8,niveau_9,niveau_10],
            [Menu,Retour]]
#fonction pricipale par laquelle passe tous les menus
def lancement(page,taille,surface,background,titre,controle_actuel,page_aide,graphisme):
#vérification de quel menu doit être lancer et création des boutons et liste de bouton en conséquence

#lancement de la page d'accueil
    if page == 'accueil':
        Logo = pygame.image.load('images/OUT.png').convert_alpha()
        Jouer = Bouton_texte(int(3.375*surface.get_width()/6-5*taille),int(6.5*surface.get_height()/10),6.5*taille,1.8*taille,(0, 255, 0),surface,"Jouer",2*taille)
        Options = Bouton_texte(int(2.25*surface.get_width()/6-5*taille),int(8*surface.get_height()/10),6.5*taille,1.8*taille,(0, 0, 255),surface,"Options",2*taille)
        Aide = Bouton_texte(int(4.5*surface.get_width()/6-5*taille),int(8*surface.get_height()/10),6.5*taille,1.8*taille,(255, 0, 0),surface,"Aide",2*taille)
        liste_boutons=[[Jouer,Aide,Options]]

#lancement du menu option
    elif page=='options':
        Menu=Bouton_menu(int(2*surface.get_width()/9),int(4*surface.get_height()/9),2*taille,(255,255,255),surface)
        Eteindre=Bouton_éteindre(int(7*surface.get_width()/18),int(4*surface.get_height()/9),2*taille,(255,0,0),surface)
        Commande=Bouton_commande(int(2*surface.get_width()/9),int(7*surface.get_height()/9),2*taille,(255,255,255),surface,controle_actuel)
        Musique=Bouton_Musique(int(7*surface.get_width()/18),int(7*surface.get_height()/9),2*taille,(255,255,255),surface)
        Graphisme=Bouton_graphisme(int(3*surface.get_width()/4-7*taille),int(7*surface.get_height()/12-7*taille),14*taille,(255,255,255),surface,3*taille,graphisme)
        liste_boutons=[[Menu,Eteindre,Graphisme],[Commande,Musique,Graphisme]]

      #lancement des pages d'aide
    elif page=='aide':
        Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
        if page_aide == 1:
            Next=Bouton_next(int(30.5*taille),int(10.1*taille),taille,(255,255,255),surface,page_aide)
        if page_aide == 2:
            Next=Bouton_next(int(1.5*taille),int(10.1*taille),taille,(255,255,255),surface,page_aide)

        liste_boutons=[[Menu,Next],[Next]]
        
#lancement du menu de selection de difficulté
    elif page=='difficulté':
        Menu=Bouton_menu(int(1.5*taille),int(1.5*taille),taille,(255,255,255),surface)
        Starter=Bouton_texte(int(surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(0,250,0),surface,'Starter',3*taille)
        Junior=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(225,175,45),surface,'Junior',3*taille)
        Master=Bouton_texte(int(surface.get_width()/6-5*taille),int(7*surface.get_height()/10),10*taille,3*taille,(250,0,0),surface,'Master',3*taille)
        Expert=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(4*surface.get_height()/10),10*taille,3*taille,(250,125,0),surface,'Expert',3*taille)
        Wizard=Bouton_texte(int(3*surface.get_width()/6-5*taille),int(7*surface.get_height()/10),10*taille,3*taille,(0,0,250),surface,'Wizard',3*taille)
        Bonus=Bouton_texte(int(5*surface.get_width()/6-5*taille),int(7*surface.get_size()[1]/10),10*taille,3*taille,(192,66,138),surface,'Bonus',3*taille)
        liste_boutons=[[Starter,Junior,Expert],[Master,Wizard,Bonus],[Menu]]

    else: #Définit une couleur pour le bouton de chaque difficulté
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
        
#création des variables i, j et b qui quand la commande est en clavier permettent de parcourir la liste (grace a des coordoné dans le tableau) des boutons et de séléctionner le bon bouton
    i=0
    j=0
    b=liste_boutons[i][j]
    #boucle permettant d'actualiser la page en permanance et de vérifier si des actions y sont effectués
    running=True
    while running:
        
        #détecte si il y a un changment (un touche pressé, un clique avec la souris...)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                return
            
            elif event.type==pygame.KEYDOWN:
                #si on appuis sur ECHAP on quitte le jeu
                if event.key==pygame.K_ESCAPE:
                    running=False
                    pygame.quit()
                    return
                
                #permet l'utilisation du clavier uniquement en commande clavier et pas en commande souris
                elif controle_actuel=='clavier':
                    # si l'on appuis sur la touche flèche droite :décale le bouton séléctioner de 1 vers la droite si l'on est sur le bouton le plus a droite on reviens sur le bouton le plus à gauche
                    if event.key==pygame.K_RIGHT:
                        if j<len(liste_boutons[i])-1:
                            j+=1
                        else:
                            j=0
                        b=liste_boutons[i][j]

                    #si l'on appuis sur la touche flèche gauche: décale le bouton séléctioner de 1 vers la gauche si l'on est sur le bouton le plus a gauche on reviens sur le bouton le plus à droite
                    elif event.key==pygame.K_LEFT:
                        if j>0:
                            j-=1
                        else:
                            j=len(liste_boutons[i])-1
                        b=liste_boutons[i][j]

                    #si l'on appuis sur la touche flèche haut: décale le bouton séléctioner de 1 vers le haut si l'on est sur le bouton le plus en haut on reviens sur le bouton le plus en bas
                    elif event.key==pygame.K_UP:
                        if i>0:
                            i-=1
                        else:
                            i=len(liste_boutons)-1
                        if j>len(liste_boutons[i])-1:
                            j=len(liste_boutons[i])-1
                        b=liste_boutons[i][j]

                     #si l'on appuis sur la touche flèche bas: décale le bouton séléctioner de 1 vers le bas si l'on est sur le bouton le plus en bas on reviens sur le bouton le plus en haut
                    elif event.key==pygame.K_DOWN:
                        if i<len(liste_boutons)-1:
                            i+=1
                        else:
                            i=0
                        if j>len(liste_boutons[i])-1:
                            j=len(liste_boutons[i])-1
                        b=liste_boutons[i][j]
                    
                    #si l'on appuis sur la touche espace ou entrer: 
                    elif event.key in [pygame.K_SPACE,pygame.K_RETURN]:
                        if b.nom=='Menu':
                            return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

                        elif page=='difficulté':
                            if b.nom=='Starter':
                                return starter(surface,taille,background,controle_actuel,page_aide,graphisme)
                            elif b.nom=='Junior':
                                return junior(surface,taille,background,controle_actuel,page_aide,graphisme)
                            elif b.nom=='Expert':
                                return expert(surface,taille,background,controle_actuel,page_aide,graphisme)
                            elif b.nom=='Master':
                                return master(surface,taille,background,controle_actuel,page_aide,graphisme)
                            elif b.nom=='Wizard':
                                return wizard(surface,taille,background,controle_actuel,page_aide,graphisme)
                            elif b.nom=='Bonus':
                                return bonus(surface,taille,background,controle_actuel,page_aide,graphisme)

                        elif page=='accueil':
                            if b.nom=='Jouer':
                                return difficulte(surface,taille,controle_actuel,background,page_aide,graphisme)
                            elif b.nom=='Options':
                                return options(surface,taille,controle_actuel,background,page_aide,graphisme)
                            elif b.nom=='Aide':
                                return aide(surface,taille,controle_actuel,background,page_aide,graphisme)

                        elif page=='aide':
                            if page_aide == 1:
                                if b.nom=='Next':
                                    page_aide = 2
                                    return aide(surface,taille,controle_actuel,background,page_aide,graphisme)
                            elif page_aide == 2:
                                if b.nom=='Next':
                                    page_aide = 1
                                    return aide(surface,taille,controle_actuel,background,page_aide,graphisme)

                        elif page=='options':
                            if b.nom=='Commande':
                                if controle_actuel=='souris':
                                    controle_actuel='clavier'
                                    Commande.etat='clavier'
                                else:
                                    controle_actuel='souris'
                                    Commande.etat='souris'
                            elif b.nom=='Eteindre':
                                running=False
                                pygame.quit()
                                return
                            elif b.nom=='Musique':
                                if pygame.mixer.music.get_busy() == True:
                                    pygame.mixer.music.stop()
                                else:
                                    pygame.mixer.music.play(-1)
                            elif b.nom=='Graphisme':
                                b.change_graphisme()
                                graphisme=b.graphisme

                        else:
                            if b.nom=='Retour':
                                return difficulte(surface,taille,controle_actuel,background,page_aide,graphisme)
                            else :
                                if page == 'bonus': miror = choice([(False,True),(True,False),(True,True)]) # Mets une des 3 versions de miroir pour les niveaux bonus

                                else : miror = (False,False)

                                if not lv.level(surface,lv.filetolevel(os.getcwd()+'/'+page+'/'+b.nom,graphisme),graphisme,taille,miror): running = False
                                if lv.home.x == 1:
                                    return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

            # vérifie la collision de chaque bouton avec la souris selon le menu si celle-ci est activée et cliquée et agis en conséquence
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if controle_actuel=='souris':
                    doublon=False
                    for rang in liste_boutons:
                        for bouton in rang:
                            if bouton.rect.collidepoint(event.pos):
                                if bouton.nom=='Menu':
                                    return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

                                elif page=='difficulté':
                                    if bouton.nom=='Starter':
                                        return starter(surface,taille,background,controle_actuel,page_aide,graphisme)
                                    elif bouton.nom=='Junior':
                                        return junior(surface,taille,background,controle_actuel,page_aide,graphisme)
                                    elif bouton.nom=='Expert':
                                        return expert(surface,taille,background,controle_actuel,page_aide,graphisme)
                                    elif bouton.nom=='Master':
                                        return master(surface,taille,background,controle_actuel,page_aide,graphisme)
                                    elif bouton.nom=='Wizard':
                                        return wizard(surface,taille,background,controle_actuel,page_aide,graphisme)
                                    elif bouton.nom=='Bonus':
                                        return bonus(surface,taille,background,controle_actuel,page_aide,graphisme)


                                elif page=='accueil':
                                    if bouton.nom=='Jouer':
                                        return difficulte(surface,taille,controle_actuel,background,page_aide,graphisme)
                                    elif bouton.nom=='Options':
                                        return options(surface,taille,controle_actuel,background,page_aide,graphisme)
                                    elif bouton.nom=='Aide':
                                        return aide(surface,taille,controle_actuel,background,page_aide,graphisme)

                                elif page=='aide':
                                    if page_aide == 1:
                                        if bouton.nom=='Next':
                                            page_aide = 2
                                            return aide(surface,taille,controle_actuel,background,page_aide,graphisme)
                                    elif page_aide == 2:
                                        if bouton.nom=='Next':
                                            page_aide = 1
                                            return aide(surface,taille,controle_actuel,background,page_aide,graphisme)

                                elif page=='options':
                                    if bouton.nom=='Commande':
                                        if controle_actuel=='souris':
                                            controle_actuel='clavier'
                                            Commande.etat='clavier'
                                        else:
                                            controle_actuel='souris'
                                            Commande.etat='souris'

                                    elif bouton.nom=='Eteindre':
                                        running=False
                                        pygame.quit()
                                        return

                                    elif bouton.nom=='Musique':
                                        if pygame.mixer.music.get_busy() == True:
                                            pygame.mixer.music.stop()
                                        else:
                                            pygame.mixer.music.play(-1)

                                    elif bouton.nom=='Graphisme' and not doublon:
                                        doublon=True
                                        bouton.change_graphisme()
                                        graphisme=bouton.graphisme
                                else:
                                    if bouton.nom=='Retour':
                                        return difficulte(surface,taille,controle_actuel,background,page_aide,graphisme)
                                    else :
                                        # vérifie si la page est en bonus ou non et prépare l'effet mirroir en conséquence
                                        if page == 'bonus':
                                            miror = choice([(False,True),(True,False),(True,True)]) # Mets une des 3 versions de miroir pour les niveaux bonus

                                        else :
                                            miror = (False,False)

                                        # lance la partie et interrompt le jeu si l'utilisateur a quitté le jeu durant la partie
                                        if not lv.level(surface,lv.filetolevel(os.getcwd()+'/'+page+'/'+bouton.nom,graphisme),graphisme,taille,miror):
                                            running = False
                                        # retourne au menu d'accueil si le joueur a demandé à retourner au menu durant la partie
                                        if lv.home.x == 1:
                                            return lancement('accueil',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

        # affiche le fond d'écran
        surface.blit(background,(0,0))

        # affiche les différents textes selon la page active
        if page == 'accueil':
            logo = pygame.transform.scale(Logo, (10*taille,10*taille))
            surface.blit(logo,(int((surface.get_width()-logo.get_width())/1.95),int(0.75*surface.get_height()/15)))

        if page == 'aide':
            pygame.draw.rect(surface,(255,255,255),(int(1.25*surface.get_width()/4-7*taille),int(7*surface.get_height()/12-7*taille),26*taille,14*taille),border_radius=int(14*taille/8))
            if page_aide == 1:
                surface.blit(pygame.font.SysFont("verdana.ttf",2*taille).render('Règle du Jeu :',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/2.25),int(4*surface.get_height()/18)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('Le but de Molecule Out est de faire sortir la molécule rouge,le virus,du plateau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4.55*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('avec des mouvement en diagonale.',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(5.5*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('Aucune molécule ne peut être tournée et les molécules uniques (grises par défaut)',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(7*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('ne peuvent pas être bougées.',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(8*surface.get_height()/10.5)))
            elif page_aide == 2:
                surface.blit(pygame.font.SysFont("verdana.ttf",2*taille).render('Contrôles de jeu :',True,(0,0,0)),(int((surface.get_width()-int(2*titre.get_width()))/2),int(4*surface.get_height()/18)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('Flèches directionnelles ou 7,9,1,3 pour se déplacer',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/10.5)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('R  pour recommencer le niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/9)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('ENTER, X, Z ou W pour sélectionner une molecule',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/7.9)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('TAB pour changer la sélection de bouton dans un niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/7.1)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('ESPACE pour sélectionner un bouton dans un niveau',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/6.4)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('ECHAP pour quitter le jeu',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/5.8)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('SUPPR pour retourner au menu',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/5.3)))
                surface.blit(pygame.font.Font("verdana.ttf",int(taille*0.6)).render('A, Q ou 5 pour le changement de molecule rapide',True,(0,0,0)),(int((surface.get_width()-titre.get_width())/7),int(4*surface.get_height()/4.9)))
        if page=='options' or page=='aide':
            surface.blit(titre,(int((surface.get_width()-titre.get_width())/2),int(surface.get_height()/25)))

        elif page != 'accueil' and page != 'options':
            surface.blit(titre,(int((surface.get_width()-titre.get_width())/2),int(4*surface.get_height()/25)))


        # affiche la souris si les commandes sont en souris
        if controle_actuel=='souris':
            pygame.mouse.set_visible(True)

        # dessine la selection selon la forme du bouton sélectionné si les commandes sont en clavier
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

# met à jour l'aperçut des boutons

        for rang in liste_boutons:
            for bouton in rang:
                bouton.update()

# met à jour l'aperçut de l'écran

        pygame.display.update()

# initialise la page de selection de niveau de difficulte starter

def starter(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('starter',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page de selection de niveau de difficulte junior

def junior(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('junior',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page de selection de niveau de difficulte expert

def expert(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('expert',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page de selection de niveau de difficulte master

def master(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('master',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page de selection de niveau de difficulte wizard

def wizard(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('wizard',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page bonus

def bonus(surface,taille,background,controle_actuel,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez un niveau',True,(0,0,0))
    return lancement('bonus',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page options

def options(surface,taille,controle_actuel,background,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Options',True,(0,0,0))
    return lancement('options',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page aide

def aide(surface,taille,controle_actuel,background,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Aide',True,(0,0,0))
    return lancement('aide',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

# initialise la page de selection de difficulte

def difficulte(surface,taille,controle_actuel,background,page_aide,graphisme):
    titre=pygame.font.SysFont("verdana.ttf",4*taille).render('Choisissez la difficulté',True,(0,0,0))
    return lancement('difficulté',taille,surface,background,titre,controle_actuel,page_aide,graphisme)

def main():
   # initialise pygame
   pygame.init()
   # initialise la page
   pygame.display.set_caption("Molecule Out")
   # initialise le plein écran
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   # unité de mesure arbitraire variant selon l'écran
   taille=min(screen.get_size())//18
   # Importer son
   pygame.mixer.music.load("son/Musique_de_fond.mp3")
   pygame.mixer.music.play(-1) # "-1" fait une boucle
   # prépare les variables pour lancer le jeu
   titre=None
   controle_actuel='clavier'
   page_aide = 1
   graphisme = 0
   background = pygame.image.load('images/back.png').convert_alpha() # Importer l'image
   background = pygame.transform.scale(background, (screen.get_size())) # Modifier l'image pour s'adapter à l'écran
   background.convert()
   # démarre le jeu
   lancement('accueil',taille,screen,background,titre,controle_actuel,page_aide,graphisme)
   # arrête le jeu
   pygame.quit()

main()
