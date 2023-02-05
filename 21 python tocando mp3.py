#É necessário digitar no cmd "pip install pygame --pre" sem as aspas para instalar o pygame para funcionar no vs code

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('zep_hurme_-_Strong_Man.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

#################################################################
#outros metodos mais simples
#Digitar no cmd "pip install playsound"

# playsound
'''from playsound import playsound

playsound('zep_hurme_-_Strong_Man.mp3')'''


###################################################################
# webbrowser
'''from webbrowser import open

open('zep_hurme_-_Strong_Man.mp3')'''