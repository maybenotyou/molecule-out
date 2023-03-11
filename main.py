import pygame

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

def main():
   pygame.init()
   pygame.display.set_caption("Anti-virus")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   background,écart_x,écart_y=fond_d_écran(screen,"uni")
   taille=(min(screen.get_size()))//18
   menu()
   
main()
