import pygame

def menu():
   return

def selection_difficulté():
   return


def main():
   pygame.init()
   pygame.display.set_caption("Anti-virus")
   screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
   background,écart_x,écart_y=fond_d_écran(screen,"uni")
   taille=(min(screen.get_size()))//18
   menu()
   
main()
