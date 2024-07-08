"""import pygame
from settings import *
from random import *
from functions import *
from pygame.locals import *
from sys import exit
#inicio


#inicializamos los modulos 
pygame.init()
clock = pygame.time.Clock()

#configuracion
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

#texto
fuente = pygame.font.SysFont("Arial", 42)

#imagenes
imagen_player = pygame.image.load("./src/assets/ovni.png")
imagen_asteroide = pygame.image.load("./src/assets/asteroide.png")
imagen_background = pygame.transform.scale(pygame.image.load("./src/assets/pared_ladrillos.webp"), SCREEN_SIZE)
imagen_start = pygame.transform.scale(pygame.image.load("./src/assets/start_button.png"), START_BUTTON)
rect_start = imagen_start.get_rect(center = START_BUTTON_POS)
# rect_start.center = START_BUTTON_POS
imagen_vida = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), VIDA_SIZE)
rect_vida = imagen_vida.get_rect(center = VIDA_POS)


#sonidos
sonido_coin = pygame.mixer.Sound("./src/assets/coin.mp3")
sonido_exito = pygame.mixer.Sound("./src/assets/exito.mp3")
sonido_gameover = pygame.mixer.Sound("./src/assets/game_over.mp3")

sonido_coin.set_volume(0.01)
sonido_exito.set_volume(0.1)
sonido_gameover.set_volume(0.01)
pygame.mixer.music.load("./src/assets/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.01)


# evento personalizado
TIMER_COIN = USEREVENT + 1
GAME_TIMEOUT = USEREVENT + 2

max_puntaje = 0

# bucle principal
while True:

    # pantalla inicio
    """ """SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    esperar_usuario(K_SPACE)""" """

    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, PUNTUACION_POS, WHITE)
    SCREEN.blit(imagen_start, rect_start)
    pygame.display.flip()
    esperar_click_usuario(rect_start)




    pygame.mouse.set_visible(False)


    # juego principal
    puntuacion = 0
    laser = None
    vidas_actuales = 3
    vidas_a_mostrar = 3
    pygame.mixer.music.play(-1)
    sonando_musica = True
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    pygame.time.set_timer(TIMER_COIN, 5000)
    pygame.time.set_timer(GAME_TIMEOUT, 100000)

    

    #creamos al jugador/bloque
    player = new_player(imagen_player, randint(0, WIDTH - rect_width), randint(0, HEIGHT - rect_height), rect_width, rect_height, color_aleatorio(), 3, randrange(31), rect_height//2)#dir = choice(direcciones), radio=randint(-1,25)
    #monedas
    coins = []
    cargar_lista_coins(coins, CANT_COINS, imagen_asteroide)
    # vidas
    vidas = []
    cargar_lista_vidas(vidas, vidas_actuales, imagen_vida)#CANT_VIDAS

    #piso 
    # pisos = []
    # cargar_lista_pisos(pisos, 1, BLACK)
    piso = pygame.rect.Rect(0,650,600,40)
    """ """
    def new_player(imagen=None, pos_x=1, pos_y=1, rect_width=50, rect_height=50, color=(0,0,0), dir=3, borde=0, radio=-1, speed_x=10, speed_y=10)->dict:
    if imagen:
        imagen = pygame.transform.scale(imagen, (rect_width, rect_height))
    return {"rect": pygame.Rect(pos_x,pos_y,rect_width,rect_height), "color":color, "dir":dir, "borde":borde, "radio":radio, "speed_x":speed_x, "speed_y":speed_y,"img":imagen}""" """



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
                    pygame.mixer.music.pause()
                    mostrar_texto(SCREEN, "Pausa", fuente, PAUSA_POS, BLACK, RED)
                    esperar_usuario(K_p)
                    if sonando_musica:
                        pygame.mixer.music.unpause()
                if event.key == K_f:
                    if not laser:
                        """ """
                            sonido laser
                        """ """
                        laser = crear_laser(player["rect"].midtop)
            
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_coin = crear_coin()
                    new_coin["color"] = CYAN
                    new_coin["rect"].center = event.pos
                    coins.append(new_coin)
                if event.button == 3:
                    player["rect"].center = SCREEN_CENTER
            
            if event.type == MOUSEMOTION:
                if event.buttons[2] == 1:
                    player["rect"].center = event.pos

            if event.type == TIMER_COIN:
                new_coin = crear_coin(imagen_asteroide)
                coins.append(new_coin)

            if event.type == GAME_TIMEOUT:# or vidas_actuales == 0
                is_running = False



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

        pygame.mouse.set_pos(player["rect"].center)


        if laser:
            laser["rect"].move_ip(0,-laser["speed"])
            if laser["rect"].bottom < 0:
                laser = None


        for coin in coins:
            rect_coin = coin["rect"]
            coin["rect"].move_ip(0, coin["speed_y"])
            if rect_coin.top > HEIGHT:
                rect_coin.bottom = 0
                """ """aca puso algo no se porque""" """


        """"""# borra y restaura monedas
        for coin in coins[:]: # es una copia de la lista [desde:hasta]
            if colision_circulos(coin["rect"], player["rect"]):
                sonido_coin.play()  
                #contador Score
                puntuacion+=1    
                coins.remove(coin)
                if len(coins) == 0:
                    sonido_exito.play()
                    cargar_lista_coins(coins, CANT_COINS, imagen_asteroide_2)""" """
        
        # 
        for coin in coins[:]:
            if len(coins)>0:
                if colision_circulos(coin["rect"], player["rect"]):
                    coins.remove(coin)
                    # coins.append(crear_coin(imagen_asteroide_2)) no hace falta que aparezca otro meteorito
                    # vidas_actuales -= 1
                    # vidas_a_mostrar -= 1
                    # vidas.remove(vidas[-1])
                    """ """
                        sonido choque
                        y algo comentado
                    """ """
                if laser:
                    if detectar_colision(laser["rect"], coin["rect"]):
                        puntuacion += 1
                        sonido_coin.play()  
                        coins.remove(coin)
                        # coins.append(crear_coin(imagen_asteroide_2)) no hace falta que aparezca otro meteorito
                        laser = None


                
    #dibujar pantalla
        print(vidas)
        SCREEN.blit(imagen_background, ORIGEN)

        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"], player["radio"]) # hitbox

        if laser:
            pygame.draw.rect(SCREEN, laser["color"], laser["rect"])

        for coin in coins:
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

        # for piso in pisos:
        #     if piso["img"]:
        #         SCREEN.blit(piso["img"], piso["rect"])
        #     else:
        #         pygame.draw.rect(SCREEN, piso["color"], piso["rect"], piso["borde"], piso["radio"])


        pygame.draw.rect(SCREEN ,BLACK, (0,590,800,20))
        pygame.draw.rect(SCREEN ,BLACK, (0,450,650,20))
        pygame.draw.rect(SCREEN ,BLACK, (150,300,650,20))
        pygame.draw.rect(SCREEN ,BLACK, (0,150,650,20))




        mostrar_texto(SCREEN,f"Puntuacion: {puntuacion}", fuente, PUNTUACION_POS, BLACK, RED)

        if not sonando_musica:
            mostrar_texto(SCREEN,f"Mute", fuente, MUTE_POS, BLACK, RED)

        SCREEN.blit(player["img"], player["rect"])

    #actualizar pantalla
        pygame.display.flip()


    # pantalla final
    pygame.mouse.set_visible(True)
    if puntuacion > max_puntaje:
        max_puntaje = puntuacion
    pygame.mixer.music.stop()
    sonido_gameover.play()
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Game Over", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    mostrar_texto(SCREEN,f"Ultima Puntuacion: {puntuacion}", fuente, ULT_PUNTUACION_POS, BLACK, GREEN)
    mostrar_texto(SCREEN,f"Maxima Puntuacion: {max_puntaje}", fuente, MAX_PUNTUACION_POS, BLACK, GREEN)
    esperar_usuario(K_SPACE)


salir_juego()
#fin"""

import pygame
from settings import *
from random import *
from functions import *
from pygame.locals import *
from sys import exit
#inicio


#inicializamos los modulos 
pygame.init()
clock = pygame.time.Clock()

#configuracion
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

#texto
fuente = pygame.font.SysFont("Arial", 42)

#imagenes
imagen_ovni = pygame.image.load("./src/assets/ovni.png")
imagen_asteroide = pygame.image.load("./src/assets/asteroide.png")
imagen_asteroide_2 = pygame.image.load("./src/assets/asteroide2.png")
imagen_background = pygame.transform.scale(pygame.image.load("./src/assets/fondo.jpg"), SCREEN_SIZE)
imagen_start = pygame.transform.scale(pygame.image.load("./src/assets/start_button.png"), START_BUTTON)
rect_start = imagen_start.get_rect(center = START_BUTTON_POS)
# rect_start.center = START_BUTTON_POS
imagen_vida = pygame.transform.scale(pygame.image.load("./src/assets/corazon.png"), VIDA_SIZE)
rect_vida = imagen_vida.get_rect(center = VIDA_POS)


#sonidos
sonido_coin = pygame.mixer.Sound("./src/assets/coin.mp3")
sonido_exito = pygame.mixer.Sound("./src/assets/exito.mp3")
sonido_gameover = pygame.mixer.Sound("./src/assets/game_over.mp3")

sonido_coin.set_volume(0.01)
sonido_exito.set_volume(0.1)
sonido_gameover.set_volume(0.01)
pygame.mixer.music.load("./src/assets/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.01)


# evento personalizado
TIMER_COIN = USEREVENT + 1
GAME_TIMEOUT = USEREVENT + 2

max_puntaje = 0

# bucle principal
while True:

    # pantalla inicio
    """SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    esperar_usuario(K_SPACE)"""

    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, PUNTUACION_POS, WHITE)
    SCREEN.blit(imagen_start, rect_start)
    pygame.display.flip()
    esperar_click_usuario(rect_start)




    pygame.mouse.set_visible(False)


    # juego principal
    puntuacion = 0
    laser = None
    vidas_actuales = 3
    vidas_a_mostrar = 3
    pygame.mixer.music.play(-1)
    sonando_musica = True
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    pygame.time.set_timer(TIMER_COIN, 5000)
    pygame.time.set_timer(GAME_TIMEOUT, 10000)

    

    #creamos al jugador/bloque
    player = new_player(imagen_ovni, randint(0, WIDTH - rect_width), randint(0, HEIGHT - rect_height), rect_width, rect_height, color_aleatorio(), 3, randrange(31), rect_height//2)#dir = choice(direcciones), radio=randint(-1,25)
    #monedas
    coins = []
    cargar_lista_coins(coins, CANT_COINS, imagen_asteroide_2)
    # vidas
    vidas = []
    cargar_lista_vidas(vidas, vidas_actuales, imagen_vida)#CANT_VIDAS



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
                    pygame.mixer.music.pause()
                    mostrar_texto(SCREEN, "Pausa", fuente, PAUSA_POS, BLACK, RED)
                    esperar_usuario(K_p)
                    if sonando_musica:
                        pygame.mixer.music.unpause()
                if event.key == K_f:
                    if not laser:
                        """
                            sonido laser
                        """
                        laser = crear_laser(player["rect"].midtop)
            
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_coin = crear_coin()
                    new_coin["color"] = CYAN
                    new_coin["rect"].center = event.pos
                    coins.append(new_coin)
                if event.button == 3:
                    player["rect"].center = SCREEN_CENTER
            
            if event.type == MOUSEMOTION:
                if event.buttons[2] == 1:
                    player["rect"].center = event.pos

            if event.type == TIMER_COIN:
                new_coin = crear_coin(imagen_asteroide)
                coins.append(new_coin)

            if event.type == GAME_TIMEOUT or vidas_actuales == 0:
                is_running = False



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

        pygame.mouse.set_pos(player["rect"].center)


        if laser:
            laser["rect"].move_ip(0,-laser["speed"])
            if laser["rect"].bottom < 0:
                laser = None


        for coin in coins:
            rect_coin = coin["rect"]
            coin["rect"].move_ip(0, coin["speed_y"])
            if rect_coin.top > HEIGHT:
                rect_coin.bottom = 0
                """aca puso algo no se porque"""


        """# borra y restaura monedas
        for coin in coins[:]: # es una copia de la lista [desde:hasta]
            if colision_circulos(coin["rect"], player["rect"]):
                sonido_coin.play()  
                #contador Score
                puntuacion+=1    
                coins.remove(coin)
                if len(coins) == 0:
                    sonido_exito.play()
                    cargar_lista_coins(coins, CANT_COINS, imagen_asteroide_2)"""
        
        # 
        for coin in coins[:]:
            if len(coins)>0:
                if colision_circulos(coin["rect"], player["rect"]):
                    coins.remove(coin)
                    # coins.append(crear_coin(imagen_asteroide_2)) no hace falta que aparezca otro meteorito
                    vidas_actuales -= 1
                    vidas_a_mostrar -= 1
                    vidas.remove(vidas[-1])
                    """
                        sonido choque
                        y algo comentado
                    """
                if laser:
                    if detectar_colision(laser["rect"], coin["rect"]):
                        puntuacion += 1
                        sonido_coin.play()  
                        coins.remove(coin)
                        # coins.append(crear_coin(imagen_asteroide_2)) no hace falta que aparezca otro meteorito
                        laser = None


                
    #dibujar pantalla
        SCREEN.blit(imagen_background, ORIGEN)

        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"], player["radio"]) # hitbox

        if laser:
            pygame.draw.rect(SCREEN, laser["color"], laser["rect"])

        for coin in coins:
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

        mostrar_texto(SCREEN,f"Puntuacion: {puntuacion}", fuente, PUNTUACION_POS, BLACK, RED)

        if not sonando_musica:
            mostrar_texto(SCREEN,f"Mute", fuente, MUTE_POS, BLACK, RED)

        SCREEN.blit(player["img"], player["rect"])

    #actualizar pantalla
        pygame.display.flip()


    # pantalla final
    pygame.mouse.set_visible(True)
    if puntuacion > max_puntaje:
        max_puntaje = puntuacion
    pygame.mixer.music.stop()
    sonido_gameover.play()
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Game Over", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    mostrar_texto(SCREEN,f"Ultima Puntuacion: {puntuacion}", fuente, ULT_PUNTUACION_POS, BLACK, GREEN)
    mostrar_texto(SCREEN,f"Maxima Puntuacion: {max_puntaje}", fuente, MAX_PUNTUACION_POS, BLACK, GREEN)
    esperar_usuario(K_SPACE)


salir_juego()
#fin