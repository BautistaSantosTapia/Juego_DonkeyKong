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

# bucle principal
while True:

    # pantalla inicio
    pygame.mouse.set_visible(True)
    SCREEN.blit(imagen_inicio, ORIGEN)
    mostrar_texto(SCREEN, "Donkey Kong", fuente, TITULO_POS, WHITE)
    SCREEN.blit(imagen_start, rect_start)
    pygame.display.flip()
    esperar_click_usuario(rect_start)



    pygame.mouse.set_visible(False)

    # juego principal
    puntuacion = 0
    laser_right = None
    laser_left = None
    vidas_actuales = 10##############
    vidas_a_mostrar = 10##############
    item_vida = None
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
    pygame.time.set_timer(TIMER_LIFE, 30000)
    pygame.time.set_timer(GAME_TIMEOUT, 100000)

    

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
                        laser_right = crear_laser(player["rect"].midright)
                if event.key == K_a:
                    if not laser_left:
                        sonido_disparo.play()
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
                item_vida = new_life(imagen_vida ,20, 200, 25, 25)

            if event.type == GAME_TIMEOUT or vidas_actuales == 0:
                is_running = False


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


    # pantalla final
    pygame.mouse.set_visible(True)
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


salir_juego()
#fin