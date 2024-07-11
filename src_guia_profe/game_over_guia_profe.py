"""import pygame
import sys

def game_over_screen(screen, score):
    clock = pygame.time.Clock()
    running = True


    """ """
    nombre = input("Ingrese su nombre: ")
    # def subir_ranking_csv(nombre_archivo, puntuacion):
    #     directorio_actual = os.path.dirname(__file__)
    #     path = os.path.join(directorio_actual, nombre_archivo)

    #     with open(path, mode= "a", encoding= "utf-8") as archivo:
    #             archivo.write(f "{nombre} - {puntuacion}\n")
                """ """

    # Guardar el puntaje en el archivo
    name = input("Enter your initials: ")
    with open('scores.txt', 'a') as file:
        file.write(f'{name} {score}\n')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False
                from main_guia_profe import main_menu
                main_menu()

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        prompt_text = font.render('Press Enter', True, (0, 0, 0))

        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 200))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300))
        screen.blit(prompt_text, (screen.get_width() // 2 - prompt_text.get_width() // 2, 400))

        pygame.display.flip()
        clock.tick(60)
"""


############################

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



# pantalla final
def game_over_screen(SCREEN, puntuacion):
    clock = pygame.time.Clock()
    is_running = True
    pygame.mouse.set_visible(True)


    nombre = input("Ingrese su nombre: ")
    # def subir_ranking_csv(nombre, puntuacion):
    #     directorio_actual = os.path.dirname(__file__)
    #     path = os.path.join(directorio_actual, "Ranking.csv")

    #     with open(path, mode= "a", encoding= "utf-8") as archivo:
    #             archivo.write(f "{nombre} - {puntuacion}\n")
                
    subir_ranking_csv(nombre,str(puntuacion))
    
    
    if puntuacion > max_puntaje:
        max_puntaje = puntuacion
    pygame.mixer.music.stop()
    sonido_gameover.play()
    SCREEN.blit(imagen_fin, ORIGEN)
    mostrar_texto(SCREEN, "Game Over", fuente, SCREEN_CENTER, BLACK)
    mostrar_texto(SCREEN, "Pulsa SPACE para volver a jugar", fuente, START_POS, BLACK)
    mostrar_texto(SCREEN,f"Ultima Puntuacion: {puntuacion}", fuente, ULT_PUNTUACION_POS, BLACK, None)
    mostrar_texto(SCREEN,f"Maxima Puntuacion: {max_puntaje}", fuente, MAX_PUNTUACION_POS, BLACK, None)
    esperar_usuario(K_SPACE)
    
    # pygame.display.flip()
    # clock.tick(60)
