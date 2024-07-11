"""import pygame
import sys
from game import game_loop
from config import config_menu
from ranking import show_ranking
from game_over import game_over_screen

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Game')

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fuente
font = pygame.font.Font(None, 74)

def main_menu():
    while True:
        screen.fill(BLUE)

        title = font.render('Space Game', True, (0, 0, 0))
        play_button = font.render('Play', True, (0, 0, 0))
        config_button = font.render('Config', True, (0, 0, 0))
        ranking_button = font.render('Ranking', True, (0, 0, 0))

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(play_button, (SCREEN_WIDTH // 2 - play_button.get_width() // 2, 250))
        screen.blit(config_button, (SCREEN_WIDTH // 2 - config_button.get_width() // 2, 350))
        screen.blit(ranking_button, (SCREEN_WIDTH // 2 - ranking_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[1] < 250 + play_button.get_height():
                    game_loop(screen)
                elif 350 < event.pos[1] < 350 + config_button.get_height():
                    config_menu(screen)
                elif 450 < event.pos[1] < 450 + ranking_button.get_height():
                    show_ranking(screen)

if __name__ == '__main__':
    main_menu()"""


########################################

import pygame
from src.settings import *
from random import *
from src.functions import *
from pygame.locals import *
from sys import exit
import os
from game_guia_profe import game_loop
from config import config_menu
from ranking import show_ranking
from game_over import game_over_screen
#inicio


#inicializamos los modulos 
pygame.init()

#configuracion
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Juego Donkey Kong")

#texto
fuente = pygame.font.SysFont("Arial", 36)

#imagenes
imagen_banana = pygame.image.load("./src/assets/banana.png")#
imagen_fuego = pygame.image.load("./src/assets/fuego.png")#
imagen_background = pygame.transform.scale(pygame.image.load("./src/assets/pared_ladrillos.webp"), SCREEN_SIZE)#
imagen_inicio = pygame.transform.scale(pygame.image.load("./src/assets/selva.webp"), SCREEN_SIZE)#
imagen_fin = pygame.transform.scale(pygame.image.load("./src/assets/selva_talada.webp"), SCREEN_SIZE)#
imagen_start = pygame.transform.scale(pygame.image.load("./src/assets/start.png"), START_BUTTON)#
rect_start = imagen_start.get_rect(center = START_BUTTON_POS) # rect_start.center = START_BUTTON_POS
imagen_vida = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), VIDA_SIZE)#
rect_vida = imagen_vida.get_rect(center = VIDA_POS)
imagen_mono = pygame.transform.scale(pygame.image.load("./src/assets/mono.png"), MONO_SIZE)#
imagen_sierra = pygame.transform.scale(pygame.image.load("./src/assets/sierra.webp"), SIERRA_SIZE)#
imagen_arma = pygame.transform.scale(pygame.image.load("./src/assets/arma.png"), VIDA_SIZE)#
imagen_ranking = pygame.transform.scale(pygame.image.load("./src/assets/ranking.png"), RANK_BUTTON)#
rect_ranking = imagen_ranking.get_rect(center = RANK_BUTTON_POS)#
imagen_config = pygame.transform.scale(pygame.image.load("./src/assets/opciones.png"), CONFIG_BUTTON)#
rect_config = imagen_config.get_rect(center = CONFIG_BUTTON_POS)#


#sonidos
pygame.mixer.music.load("./src/assets/musica_fondo.mp3")#
sonido_pausa = pygame.mixer.Sound("./src/assets/pausa.mp3")#
sonido_disparo = pygame.mixer.Sound("./src/assets/disparo.mp3")#
sonido_vida = pygame.mixer.Sound("./src/assets/recompensa.mp3")#
sonido_explosion = pygame.mixer.Sound("./src/assets/explosion.mp3")#
sonido_gameover = pygame.mixer.Sound("./src/assets/perder.mp3")#
sonido_exito = pygame.mixer.Sound("./src/assets/ganar.mp3")#
sonido_dano = pygame.mixer.Sound("./src/assets/dano.ogg")#

sonido_disparo.set_volume(0.1)
sonido_pausa.set_volume(0.1)
pygame.mixer.music.set_volume(0.1)
sonido_vida.set_volume(0.1)
sonido_explosion.set_volume(0.1)
sonido_gameover.set_volume(0.1)
sonido_exito.set_volume(0.1)
sonido_dano.set_volume(0.1)



# evento personalizado
TIMER_LIFE = USEREVENT + 1
GAME_TIMEOUT = USEREVENT + 2

max_puntaje = 0


def menu():
    # bucle principal
    while True:

        # pantalla inicio
        pygame.mouse.set_visible(True)
        SCREEN.blit(imagen_inicio, ORIGEN)
        mostrar_texto(SCREEN, "Donkey Kong", fuente, TITULO_POS, WHITE)
        SCREEN.blit(imagen_start, rect_start)
        SCREEN.blit(imagen_ranking, rect_ranking)
        SCREEN.blit(imagen_config, rect_config)
        pygame.display.flip()
        esperar_click_usuario(rect_start)
        esperar_click_usuario(rect_ranking)
        esperar_click_usuario(rect_config)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_posicion = event.pos
                    if punto_en_rectangulo(click_posicion, rect_start):
                        game_loop(SCREEN)
                    elif punto_en_rectangulo(click_posicion, rect_ranking):
                        show_ranking(SCREEN)
                    elif punto_en_rectangulo(click_posicion, rect_start):
                        config_menu(SCREEN)

if __name__ == '__main__':
    menu()