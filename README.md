
<h1>Molecule Out</h1>
 
<p>Le projet consistait à créer un jeu à partir de la bibliothèque Pygame de Python en utilisant le concept du jeu de société Anti-virus.</p>

---

<h1>PRÉREQUIS POUR JOUER</h1>

<p>Afin de pouvoir lancer le jeu, il vous faut une version de Python 3.7 ou + et installer le module suivant :</p>
<ul>
  <li>Pygame 2.3.0</li>
</ul>

<p>Voici la commande afin d'installer ce module :</p>

```
>>> pip install -U pygame==2.3.0
```
---

<h2>Images:</h2>

<p>Le logo a été créé par Eliot et le fond d'écran par l'IA Dall-e avec un prompt d'Eliot.</p>

- [Logo](./images/OUT.png)
- [Fond d'écran](./images/back.png)

---


<h2>Son:</h2>

<p>Musique original est <a href="https://bit.ly/40MW20b">Future Science Technology by GentleJammers</a> qui a été remixé.</p>

- [Musique de fond](./son/Musique_de_fond.mp3) 


---


<h2>Documentation:</h2>

<p>Il est possible d’ouvrir le jeu de deux façon différentes : soit depuis l’exécutable Molecule Out.exe, soit
en lançant l’exécution du programme main.py. Le jeu commence en plein écran avec les commandes
clavier, pour changer de bouton sélectionné il faut utiliser les flèches directionnelles et pour valider, la
barre espace ou la touche entrée. Pour quitter le jeu à tout moment, il y a la touche echap. Les
instructions de commandes lors d’une partie sont détaillées dans le menu aide.</p>

<p>Le menu option permet de passer de clavier à souris et inversement, d’activer ou de désactiver la
musique de fond et de changer les graphismes du plateau. Il est aussi possible de quitter le jeu depuis
ce menu.</p>

<p>Attention, les deux graphismes utilisent des commandes légèrement différentes, le curseur n’existant
pas dans le graphisme 2, la sélection rapide fonctionne cependant dans tous les cas.</p>

<p>Pour fonctionner correctement, le jeu Molecule Out nécessite un ordinateur ayant pour système
d’exploitation Windows (testé sur Windows 10) ou Linux (testé sur Fedora 37) pour les fichiers
exécutables ainsi que d’une souris ou un pad tactile et une sortie son pour une meilleure expérience de
jeu. Pour les fichiers python, il faut en plus une version python égale ou supérieure à 3.7 et une version
de pygame supérieure à 2.3.0 ainsi que les bibliothèques de base random et os ainsi que les caractères
UTF-8.</p>

<p>Nous avons fait le choix de proposer un affichage adaptatif à l’écran de l’utilisateur afin d’optimiser la
résolution de l’écran, nous avons pour cela utilisé le minimum d’images possibles, dans la limite de
l’esthétisme, mais avons donc dû générer de nombreux logo avec des objets de dessin de pygame.
Durant la partie, il est possible d’utiliser différentes touches pour les mêmes commandes afin que
chacun puisse jouer avec les commandes qui lui sont les plus familières(azerty,qwerty,flèches).
Pour une question de facilité de modification de niveau et pour un gain de place dans le programme,
tous les niveaux sont stockés sous format txt.</p>

