"""import pygame
import sys

def config_menu(screen):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((255, 255, 255))

        # Dibujar elementos de configuración aquí

        pygame.display.flip()
        clock.tick(60)
"""


#######################

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


def config_menu(screen):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((255, 255, 255))

        # Dibujar elementos de configuración aquí

        pygame.display.flip()
        clock.tick(60)