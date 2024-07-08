
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Colisión con Pared y Límites de Pantalla')

# Definir colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Definir las dimensiones y posición del rectángulo
rect_x, rect_y = 300, 200
rect_width, rect_height = 200, 150

# Definir las dimensiones y posición inicial del personaje
player_x, player_y = 50, 50
player_width, player_height = 50, 50
player_speed = 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Guardar la posición anterior del personaje
    old_player_x, old_player_y = player_x, player_y

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Crear rectángulos para el personaje y el rectángulo de colisión
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Detectar colisión con el rectángulo y ajustar la posición del personaje
    if player_rect.colliderect(rect):
        player_x, player_y = old_player_x, old_player_y

    # Verificar límites de la pantalla
    if player_x < 0:
        player_x = 0
    if player_x + player_width > width:
        player_x = width - player_width
    if player_y < 0:
        player_y = 0
    if player_y + player_height > height:
        player_y = height - player_height

    # Crear el rectángulo actualizado del personaje después de ajustar la posición
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Rellenar la pantalla con color blanco
    screen.fill(white)

    # Dibujar el rectángulo
    pygame.draw.rect(screen, black, rect)

    # Dibujar el personaje
    pygame.draw.rect(screen, red, player_rect)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()