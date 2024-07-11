
import pygame
from src.settings import *
from random import *
from src.functions import *
from pygame.locals import *
from sys import exit
import os
from src.
from config import config_menu
from ranking import ver_ranking
from game_over import game_over_screen


def loop_jugable(SCREEN):
    pygame.mouse.set_visible(False)

    # juego principal
    clock = pygame.time.Clock()
    puntuacion = 0
    laser_right = None
    laser_left = None
    vidas_actuales = 10##############
    vidas_a_mostrar = 10##############
    item_vida = None
    arma = None
    bandera_poder = False
    pygame.mixer.music.play(-1)
    sonando_musica = True
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    desplazamiento_y = 0
    potencia_salto = -18
    limite_velocidad_salto = 18
    gravedad = 1
    esta_saltando = False
    pygame.time.set_timer(TIMER_LIFE, 10000)
    # pygame.time.set_timer(GAME_TIMEOUT, 100000)

    

    #creamos al jugador/bloque
    player = new_player(imagen_banana, 20, 479, rect_width, rect_height, color_aleatorio(), 3, randrange(31), rect_height // 2)
    #piso
    pisos = [
        {"rect": pygame.Rect(0, 0, 800, 40), "color": WHITE, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(0, 590, 800, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(0, 450, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(150, 300, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(0, 150, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5}
    ]
    #monedas
    coins_left = []
    cargar_lista_coins_left(coins_left, CANT_COINS, imagen_fuego)
    coins_right = []
    cargar_lista_coins_right(coins_right, CANT_COINS, imagen_fuego)
    # vidas
    vidas = []
    cargar_lista_vidas(vidas, vidas_actuales, imagen_vida)#CANT_VIDAS
    bandera_vida = True
    #mono
    mono_win = ganar_juego(imagen_mono, 5, 60, mono_width, mono_height)
    #obstaculos
    obstaculos = [
        {"rect": pygame.Rect(200, 40, 50, 50), "color": BLACK, "img": imagen_sierra},
        {"rect": pygame.Rect(300, 120, 50, 50), "color": BLACK, "img": imagen_sierra},
        {"rect": pygame.Rect(400, 40, 50, 50), "color": BLACK, "img": imagen_sierra},
        {"rect": pygame.Rect(500, 120, 50, 50), "color": BLACK, "img": imagen_sierra},
        {"rect": pygame.Rect(600, 40, 50, 50), "color": BLACK, "img": imagen_sierra}
    ]

    #arma
    arma = power_up(imagen_arma, 250, 390, 45, 45)



    is_running = True
    while is_running:
        clock.tick(FPS)

    #analizar eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_left = True
                if event.key == K_RIGHT:
                    move_right = True
                if event.key == K_UP:
                    move_up = True
                if event.key == K_DOWN:
                    move_down = True        
                if event.key == K_m:
                    if sonando_musica:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    sonando_musica = not sonando_musica
                if event.key == K_p:
                    sonido_pausa.play()
                    pygame.mixer.music.pause()
                    mostrar_texto(SCREEN, "Pausa", fuente, PAUSA_POS, BLACK, None)
                    esperar_usuario(K_p)
                    if sonando_musica:
                        pygame.mixer.music.unpause()
                if event.key == K_d:
                    if not laser_right:
                        sonido_disparo.play()
                        if bandera_poder==True:
                            laser_right = crear_laser(player["rect"].midright,speed=35,laser_width=13,laser_height=13)
                        else:
                            laser_right = crear_laser(player["rect"].midright)
                if event.key == K_a:
                    if not laser_left:
                        sonido_disparo.play()
                        if bandera_poder==True:
                            laser_left = crear_laser(player["rect"].midleft,speed=35,laser_width=13,laser_height=13)
                        else:
                            laser_left = crear_laser(player["rect"].midleft)
            
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False

            if event.type == TIMER_LIFE:
                item_vida = new_life(imagen_vida ,500, 400, 25, 25)

            if event.type == GAME_TIMEOUT or vidas_actuales == 0:
                is_running = False
                """ir a pantalla game over"""


        # Guardar la posición anterior del personaje
        old_player_x, old_player_y = player["rect"].x, player["rect"].y


    #actualizar elementos

        #muevo el rectangulo de acuerdo su la direccion
        if move_left and player["rect"].left >= 0:
            if player["rect"].left - SPEED <= 0:
                player["rect"].left = 0
            else:
                player["rect"].left -= SPEED
        if move_right and player["rect"].right <= WIDTH:
            if player["rect"].right + SPEED >= WIDTH:
                player["rect"].right = WIDTH
            else:
                player["rect"].right += SPEED
        if move_up and player["rect"].top >= 0:
            if player["rect"].top - SPEED <= 0:
                player["rect"].top = 0
            else:
                player["rect"].top -= SPEED
        if move_down and player["rect"].bottom <= HEIGHT:
            if player["rect"].bottom + SPEED >= HEIGHT:
                player["rect"].bottom = HEIGHT
            else:
                player["rect"].bottom += SPEED


        if laser_right:
            laser_right["rect"].move_ip(+laser_right["speed"],0)
            if laser_right["rect"].left > WIDTH:
                laser_right = None

        if laser_left:
            laser_left["rect"].move_ip(-laser_left["speed"],0)
            if laser_left["rect"].right < 0:
                laser_left = None


        for coin in coins_left:
            rect_coins_left = coin["rect"]
            coin["rect"].move_ip(-coin["speed_x"], 0)
            if rect_coins_left.right < 0:
                rect_coins_left.left = WIDTH

        for coin in coins_left[:]:
            if len(coins_left)>0:
                if colision_circulos(coin["rect"], player["rect"]):
                    coins_left.remove(coin)
                    vidas_actuales -= 1
                    vidas_a_mostrar -= 1
                    vidas.remove(vidas[-1])
                    sonido_dano.play()
                    pygame.time.wait(100)
                if laser_right:
                    if detectar_colision(laser_right["rect"], coin["rect"]):
                        puntuacion += 1
                        sonido_explosion.play()  
                        coins_left.remove(coin)
                        coins_left.append(crear_coin_left(imagen_fuego))# no hace falta que aparezca otro meteorito
                        laser_right = None

        for coin in coins_right:
            rect_coins_right = coin["rect"]
            coin["rect"].move_ip(+coin["speed_x"], 0)
            if rect_coins_right.left > WIDTH:
                rect_coins_right.right = 0

        for coin in coins_right[:]:
            if len(coins_right)>0:
                if colision_circulos(coin["rect"], player["rect"]):
                    coins_right.remove(coin)
                    vidas_actuales -= 1
                    vidas_a_mostrar -= 1
                    vidas.remove(vidas[-1])
                    sonido_dano.play()
                    pygame.time.wait(100)
                if laser_left:
                    if detectar_colision(laser_left["rect"], coin["rect"]):
                        puntuacion += 1
                        sonido_explosion.play()  
                        coins_right.remove(coin)
                        coins_right.append(crear_coin_right(imagen_fuego))# no hace falta que aparezca otro meteorito
                        laser_left = None

        if item_vida:
            if detectar_colision(item_vida["rect"], player["rect"]):
                print(vidas)
                sonido_vida.play()
                vidas_actuales += 1
                vidas_a_mostrar += 1
                #vidas.append(1)
                cargar_lista_vidas(vidas,1,imagen_vida)
                bandera_vida = False
                item_vida = None

        if detectar_colision(mono_win["rect"], player["rect"]):
            sonido_exito.play()
            is_running = False
            """ir a pantalla victoria"""

        for obstaculo in obstaculos:
            if colision_circulos(obstaculo["rect"],player["rect"]):
                print("toco")
                player["rect"].x, player["rect"].y = old_player_x, old_player_y
                sonido_dano.play()
                vidas_actuales -= 1
                vidas_a_mostrar -= 1
                vidas.remove(vidas[-1])
                pygame.time.wait(250)

        if arma:
            if detectar_colision(arma["rect"], player["rect"]):
                sonido_vida.play()
                bandera_poder = True
                arma = None
        

                
    #dibujar pantalla
        SCREEN.blit(imagen_background, ORIGEN)

        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"], player["radio"])  #hitbox
        # for obstaculo in obstaculos:
        #     pygame.draw.rect(SCREEN, obstaculo["color"], obstaculo["rect"])  #hitbox

        if laser_right:
            pygame.draw.rect(SCREEN, laser_right["color"], laser_right["rect"])
        if laser_left:
            pygame.draw.rect(SCREEN, laser_left["color"], laser_left["rect"])

        for coin in coins_left:
            if coin["img"]:
                SCREEN.blit(coin["img"], coin["rect"])
            else:
                pygame.draw.rect(SCREEN, coin["color"], coin["rect"], coin["borde"], coin["radio"])

        for coin in coins_right:
            if coin["img"]:
                SCREEN.blit(coin["img"], coin["rect"])
            else:
                pygame.draw.rect(SCREEN, coin["color"], coin["rect"], coin["borde"], coin["radio"])


        for vida in vidas:
            if vida["img"]:
                SCREEN.blit(vida["img"], vida["rect"])
            else:
                pygame.draw.rect(SCREEN, vida["color"], vida["rect"], vida["borde"], vida["radio"])
            for _ in range(vidas_a_mostrar):
                vida["rect"].left += 25
            vidas_a_mostrar -= 1 # para que no se vaya de la pantalla

        if item_vida and bandera_vida==True:
            SCREEN.blit(item_vida["img"], item_vida["rect"])
            
        if arma:
            SCREEN.blit(arma["img"], arma["rect"])

        
        SCREEN.blit(mono_win["img"], mono_win["rect"])



        if not sonando_musica:
            mostrar_texto(SCREEN,f"Mute", fuente, MUTE_POS, BLACK, None)

        for obstaculo in obstaculos:
            SCREEN.blit(obstaculo["img"], obstaculo["rect"])

        for piso in pisos:
            pygame.draw.rect(SCREEN, piso["color"], piso["rect"])
            if player["rect"].colliderect(piso["rect"]):
                player["rect"].x, player["rect"].y = old_player_x, old_player_y

        mostrar_texto(SCREEN,f"Puntuacion: {puntuacion}", fuente, PUNTUACION_POS, BLACK, None)

        for vida in vidas:
            if vida["img"]:
                SCREEN.blit(vida["img"], vida["rect"])
            else:
                pygame.draw.rect(SCREEN, vida["color"], vida["rect"], vida["borde"], vida["radio"])
            for _ in range(vidas_a_mostrar):
                vida["rect"].left += 25
            vidas_a_mostrar -= 1 # para que no se vaya de la pantalla


        SCREEN.blit(player["img"], player["rect"])

    #actualizar pantalla
        pygame.display.flip()
        
        
        
        
    # Llamar a la pantalla de game over
    from src_guia_profe.main_guia_profe import game_over_screen
    game_over_screen(SCREEN, 100)
        

