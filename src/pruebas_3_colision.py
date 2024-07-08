import pygame
from settings import *
from random import *
from functions import *
from pygame.locals import *
from sys import exit

# Inicializamos los módulos 
pygame.init()
clock = pygame.time.Clock()

# Configuración
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

# Texto
fuente = pygame.font.SysFont("Arial", 42)

# Imágenes
imagen_player = pygame.image.load("./src/assets/banana.png")
imagen_asteroide = pygame.image.load("./src/assets/fuego.png")
imagen_background = pygame.transform.scale(pygame.image.load("./src/assets/pared_ladrillos.webp"), SCREEN_SIZE)
imagen_start = pygame.transform.scale(pygame.image.load("./src/assets/start_button.png"), START_BUTTON)
rect_start = imagen_start.get_rect(center=START_BUTTON_POS)
imagen_tiro = pygame.transform.scale(pygame.image.load("./src/assets/semilla.png"), START_BUTTON)

# Evento personalizado
GAME_TIMEOUT = USEREVENT + 2

# Bucle principal
while True:
    # Pantalla de inicio
    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, PUNTUACION_POS, WHITE)
    SCREEN.blit(imagen_start, rect_start)
    pygame.display.flip()
    esperar_click_usuario(rect_start)

    pygame.mouse.set_visible(False)

    # Juego principal
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    
    desplazamiento_y = 0
    potencia_salto = -18
    limite_velocidad_salto = 18
    gravedad = 1
    esta_saltando = False

    pygame.time.set_timer(GAME_TIMEOUT, 100000)
    
    player = new_player(imagen_player, 20, 479, rect_width, rect_height, color_aleatorio(), 3, randrange(31), rect_height // 2)

    # {"rect": pygame.Rect(pos_x, pos_y, rect_width, rect_height), "color": color, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y, "img": imagen}
    pisos = [
        {"rect": pygame.Rect(0, 590, 800, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(0, 450, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(150, 300, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5},
        {"rect": pygame.Rect(0, 150, 650, 20), "color": BLACK, "speed_x": 5, "speed_y": 5}
    ]

    is_running = True
    while is_running:
        clock.tick(FPS)

        # Analizar eventos
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

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
            
            if event.type == GAME_TIMEOUT:
                is_running = False

        # Guardar la posición anterior del personaje
        old_player_x, old_player_y = player["rect"].x, player["rect"].y

        # Mover el rectángulo de acuerdo a la dirección
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



        # Dibujar pantalla
        SCREEN.blit(imagen_background, ORIGEN)
        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"], player["radio"])  # Hitbox

        for piso in pisos:
            pygame.draw.rect(SCREEN, piso["color"], piso["rect"])
            if player["rect"].colliderect(piso["rect"]):
                player["rect"].x, player["rect"].y = old_player_x, old_player_y

        SCREEN.blit(player["img"], player["rect"])
        

        # Actualizar pantalla
        pygame.display.flip()

    # Pantalla final
    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Game Over", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    esperar_usuario(K_SPACE)

salir_juego()