import pygame
from random import randrange, randint
from settings import *
from pygame.locals import *
from sys import exit

def get_color(lista:list):
    return lista[randint(0, len(lista) - 1)]

def color_aleatorio():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r, g, b)

def new_player(imagen=None, pos_x=1, pos_y=1, rect_width=50, rect_height=50, color=(0,0,0), dir=3, borde=0, radio=-1, speed_x=10, speed_y=10)->dict:
    if imagen:
        imagen = pygame.transform.scale(imagen, (rect_width, rect_height))
    return {"rect": pygame.Rect(pos_x,pos_y,rect_width,rect_height), "color":color, "dir":dir, "borde":borde, "radio":radio, "speed_x":speed_x, "speed_y":speed_y,"img":imagen}

def detectar_colision(rect_1, rect_2)->bool:
    if punto_en_rectangulo(rect_1.topleft, rect_2) or \
       punto_en_rectangulo(rect_1.topright, rect_2) or \
       punto_en_rectangulo(rect_1.bottomleft, rect_2) or \
       punto_en_rectangulo(rect_1.bottomright, rect_2) or \
       punto_en_rectangulo(rect_2.topleft, rect_1) or \
       punto_en_rectangulo(rect_2.topright, rect_1) or \
       punto_en_rectangulo(rect_2.bottomleft, rect_1) or \
       punto_en_rectangulo(rect_2.bottomright, rect_1):
        return True
    else:
        return False
    
    
    # agarras una esquina del rectangulo 1 y preguntas si esta dentro del rectangulo 2

def punto_en_rectangulo(punto, rect):
    x = punto[0]
    y = punto[1]

    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
    # if x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom:
    #     return True
    # else:
    #     return False

def distancia_entre_puntos(p1:tuple[int,int], p2:tuple[int,int])->float:
    ca = p1[0] - p2[0]
    co = p1[1] - p2[1]
    distancia = (ca ** 2 + co ** 2) ** 0.5 #math.sqrt()
    return distancia

def colision_circulos(rect_1, rect_2)->bool:
    r1 = rect_1.width // 2
    r2 = rect_2.width // 2
    distancia = distancia_entre_puntos(rect_1.center,rect_2.center)
    return distancia <= r1 + r2


def crear_coin_left(imagen=None)->dict:
    width_coin = 47
    height_coin = 47

    return new_player(imagen, randint(WIDTH + width_coin, WIDTH*2), randint(460, HEIGHT - height_coin), width_coin, height_coin, YELLOW, 0, 0, height_coin//2, speed_y= randint(min_coin_speed,max_coin_speed))
def crear_coin_right(imagen=None)->dict:
    width_coin = 47
    height_coin = 47

    return new_player(imagen, randint(-WIDTH, 0-width_coin), randint(155,270), width_coin, height_coin, YELLOW, 0, 0, height_coin//2, speed_y= randint(min_coin_speed,max_coin_speed))
                            
def cargar_lista_coins_left(lista:list, cant:int, imagen=None):
    for _ in range(cant):
        lista.append(crear_coin_left(imagen))
def cargar_lista_coins_right(lista:list, cant:int, imagen=None):
    for _ in range(cant):
        lista.append(crear_coin_right(imagen))


def crear_vida(imagen=None)->dict:
    return new_player(imagen, VIDA_POS[0], VIDA_POS[1], VIDA_SIZE[0], VIDA_SIZE[1])

def cargar_lista_vidas(lista:list, cant:int, imagen=None):
    for _ in range(cant):
        lista.append(crear_vida(imagen))

def new_life(imagen, x, y, width, height):
    return new_player(imagen, x, y, width, height)

def power_up(imagen, x, y, width, height):
    return new_player(imagen, x, y, width, height)

def ganar_juego(imagen, x, y, width, height):
    return new_player(imagen, x, y, width, height)
        
def crear_laser(posicion:tuple[int,int],color:tuple[int,int,int]=(0,0,0), speed:int=15, laser_width=6, laser_height=6):
    r = pygame.Rect(0, 0, laser_width, laser_height)
    r.midbottom = posicion
    return {"rect": r, "color":color,"speed":speed}


def crear_piso(imagen=BLACK, posicion=(800,600)):
    return new_player(None, 0, 650, 650, 40, BLACK)

def cargar_lista_pisos(lista:list, cant:int, imagen=None, posicion=(800,600)):
    for _ in range(cant):
        lista.append(crear_piso(imagen,posicion))


def salir_juego():
    pygame.quit()
    exit()

def mostrar_texto(superficie:pygame.Surface, texto:str, fuente:pygame.font.Font, posicion:tuple[int,int], color:tuple[int,int,int], color_fondo:tuple[int,int,int]=None):
    sup_texto = fuente.render(texto, True, color, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = posicion
    superficie.blit(sup_texto, rect_texto)
    pygame.display.flip()

def esperar_usuario(tecla:int):
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == KEYDOWN:
                if event.key == tecla:
                    continuar = False

def esperar_click_usuario(rect:pygame.Rect):  
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir_juego()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_posicion = event.pos
                    if punto_en_rectangulo(click_posicion, rect):
                        continuar = False
