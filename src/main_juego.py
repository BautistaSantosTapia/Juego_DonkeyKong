
import pygame
from src.settings import *
from random import *
from src.functions import *
from pygame.locals import *
from sys import exit
import os
# from Juego_DonkeyKong.src.juego_jugable import game_loop
# from config import config_menu
# from ranking import show_ranking
# from game_over_juego import game_over_screen
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
                        loop_jugable(SCREEN)
                    elif punto_en_rectangulo(click_posicion, rect_ranking):
                        ver_ranking(SCREEN)
                    elif punto_en_rectangulo(click_posicion, rect_start):
                        config_menu(SCREEN)

if __name__ == '__main__':
    menu()