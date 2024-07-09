# colors 
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
CUSTOM = (226,203,95)
colors = [RED,GREEN,BLUE,CYAN,MAGENTA,YELLOW,BLACK,WHITE]

# medidas
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH,HEIGHT)
MID_WIDTH_SCREEN = WIDTH//2
MID_HEIGHT_SCREEN = HEIGHT//2
SCREEN_CENTER = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN)
ORIGEN = (0,0)
FPS = 30
SPEED = 5
CANT_COINS = 25
CANT_VIDAS = 3
PUNTUACION_POS = (MID_WIDTH_SCREEN,50)
ULT_PUNTUACION_POS = (200,50)
MAX_PUNTUACION_POS = (WIDTH - 200,50)
MUTE_POS = (50,HEIGHT-50)
START_POS = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN+ 100)
PAUSA_POS = (WIDTH//2,HEIGHT//2)
START_BUTTON = (250,250)
START_BUTTON_POS = SCREEN_CENTER
VIDA_POS = (20,20)

#DIRECCIONES
move_left = False
move_right = False
move_up = False
move_down = False

rect_width = 60
rect_height = 60
laser_width = 5
laser_height = 5
vida_width = 20
vida_height = 20
VIDA_SIZE = (vida_width,vida_height)

min_coin_speed = 3
max_coin_speed = 10


#player
SIZE_PLAYER = (300,300,200,100)# x y w h