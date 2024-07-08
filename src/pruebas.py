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
imagen_player = pygame.image.load("./src/assets/ovni.png")
imagen_asteroide = pygame.image.load("./src/assets/asteroide.png")
imagen_background = pygame.transform.scale(pygame.image.load("./src/assets/pared_ladrillos.webp"), SCREEN_SIZE)
imagen_start = pygame.transform.scale(pygame.image.load("./src/assets/start_button.png"), START_BUTTON)
rect_start = imagen_start.get_rect(center = START_BUTTON_POS)
# rect_start.center = START_BUTTON_POS


# evento personalizado
GAME_TIMEOUT = USEREVENT + 2

# bucle principal
while True:

    # pantalla inicio
    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Asteroides", fuente, PUNTUACION_POS, WHITE)
    SCREEN.blit(imagen_start, rect_start)
    pygame.display.flip()
    esperar_click_usuario(rect_start)




    pygame.mouse.set_visible(False)


    # juego principal
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    
    desplazamiento_y = 0
    potencia_salto = -18 #-15
    limite_velocidad_salto = 18 #15
    gravedad = 1
    esta_saltando = False

    pygame.time.set_timer(GAME_TIMEOUT, 10000)


    
    
    player = new_player(imagen_player, 20, 479, rect_width, rect_height, color_aleatorio(), 3, randrange(31), rect_height//2)#dir = choice(direcciones), radio=randint(-1,25)
    
    # Guardar la posición anterior del personaje
    old_player_x, old_player_y = player["rect"][0], player["rect"][1]


    # {"rect": pygame.Rect(pos_x,pos_y,rect_width,rect_height), "color":color, "dir":dir, "borde":borde, "radio":radio, "speed_x":speed_x, "speed_y":speed_y,"img":imagen}
    pisos = [{"rect":pygame.Rect(0,590,800,20), "color":BLACK, "speed_x":5, "speed_y":5},
            {"rect":pygame.Rect(0,450,650,20), "color":BLACK, "speed_x":5, "speed_y":5},
            {"rect":pygame.Rect(150,300,650,20), "color":BLACK, "speed_x":5, "speed_y":5},
            {"rect":pygame.Rect(0,150,650,20), "color":BLACK, "speed_x":5, "speed_y":5}]
    # [{'rect': <rect(95, 20, 20, 20)>, 'color': (0, 0, 0), 'dir': 3, 'borde': 0, 'radio': -1, 'speed_x': 10, 'speed_y': 10, 'img': <Surface(20x20x32 SW)>}, {'rect': <rect(70, 20, 20, 20)>, 'color': (0, 0, 0), 'dir': 3, 'borde': 0, 'radio': -1, 'speed_x': 10, 'speed_y': 10, 'img': <Surface(20x20x32SW)>}, {'rect': <rect(45, 20, 20, 20)>, 'color': (0, 0, 0), 'dir': 3, 'borde': 0, 'radio': -1, 'speed_x': 10, 'speed_y': 10, 'img': <Surface(20x20x32 SW)>}]
    
        
        
        
    

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

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
            
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


        def actualizar(plataformas):
                aplicar_gravedad(plataformas)

        def aplicar_gravedad(plataformas):#
                
                if esta_saltando:
                    player["rect"].y += desplazamiento_y
                    if desplazamiento_y + gravedad < limite_velocidad_salto:
                        desplazamiento_y += gravedad #esto hace que se mueva para arriba

                colicion_vertical(plataformas)
                #self.colision_horizontal(plataformas)

        def colicion_vertical(plataformas):
                for plataforma in plataformas:
                # Detectar colisión con el rectángulo y ajustar la posición del personaje
                    if player["rect"].colliderect(plataforma["rect"]):
                        player["rect"][0], player["rect"][1] = old_player_x, old_player_y
                        """
                    if plataforma["rect"].colliderect(player["rect"]):
                        print("chau")
                        if player["rect"].y > 0:
                            player["rect"].bottom = plataforma["rect"].top
                            esta_saltando = False
                            desplazamiento_y = 0
                            break
                        elif player["rect"].y < 0:
                            player["rect"].top = plataforma["rect"].bottom
                            esta_saltando = False
                            desplazamiento_y = 0
                            break
                        
                        if player["rect"].x < 0:
                            player["rect"].left = plataforma["rect"].right
                            esta_saltando = False
                            desplazamiento_y = 0
                            print("if")
                        elif player["rect"].x >= 0:
                            player["rect"].right = plataforma["rect"].left
                            esta_saltando = False
                            desplazamiento_y = 0
                            print("el")"""

                    else:
                        esta_saltando = True


                
    #dibujar pantalla
        SCREEN.blit(imagen_background, ORIGEN)
        

        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"], player["radio"]) # hitbox

        for piso in pisos:
            pygame.draw.rect(SCREEN, piso["color"], piso["rect"])


        SCREEN.blit(player["img"], player["rect"])
        actualizar(pisos)

    #actualizar pantalla
        pygame.display.flip()


    # pantalla final
    pygame.mouse.set_visible(True)
    SCREEN.fill(BLACK)
    mostrar_texto(SCREEN, "Game Over", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, START_POS, WHITE)
    esperar_usuario(K_SPACE)


salir_juego()
fin
"""
    
    def actualizar(self, pantalla, plataformas, lista_enemigos):

        tiempo_actual = py.time.get_ticks()
        if tiempo_actual > self.tiempo_anterior + self.tiempo_habilidad_especial:
            self.habilidad_especial = False


        accion = ""
        if self.habilidad_especial:
            match self.que_hace:
                case "quieto":
                    accion = "super_quieto"
                case "derecha":
                    accion = "super_derecha"
                case "izquierda":
                    accion = "super_izquierda"
                case "salta":
                    accion = "super_salta"      
            self.animacion_actual = self.animaciones[accion]

        else:
            self.animacion_actual = self.animaciones[self.que_hace]


        match self.que_hace:
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla)
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto


        self.actualizar_proyectiles(lista_enemigos, pantalla) ###
        self.aplicar_gravedad(pantalla, plataformas)




    def aplicar_gravedad(self, pantalla, plataformas):#
        
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad #esto hace que se mueva para arriba

        self.colicion_vertical(plataformas)
        #self.colision_horizontal(plataformas)



    def colicion_vertical(self, plataformas):
        for plataforma in plataformas:
            if plataforma["rectangulo"].colliderect(self.rectangulo_principal):
                print("chau")
                if self.rectangulo_principal.y > 0:
                    self.rectangulo_principal.bottom = plataforma["rectangulo"].top
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    break
                elif self.rectangulo_principal.y < 0:
                    self.rectangulo_principal.top = plataforma["rectangulo"].bottom
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    break
                
                if self.rectangulo_principal.x < 0:
                    self.rectangulo_principal.left = plataforma["rectangulo"].right
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    print("if")
                elif self.rectangulo_principal.x >= 0:
                    self.rectangulo_principal.right = plataforma["rectangulo"].left
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    print("el")
                    
                # self.esta_saltando = False
                # self.desplazamiento_y = 0
                # break

            else:
                self.esta_saltando = True
"""
