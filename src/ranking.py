import pygame
from settings import SCREEN_SIZE, ORIGEN, MID_WIDTH_SCREEN

def ver_rankings(pantalla):
    print("hosn")
    clock = pygame.time.Clock()
    running = True

    # Leer los scores desde un archivo
    try:
        with open('./src/Ranking.csv', 'r',encoding='utf-8') as file:
            scores = [line.strip().split() for line in file.readlines()]
    except FileNotFoundError:
        scores = []
        print("fallo")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    running = False

        pantalla.blit(pygame.transform.scale(pygame.image.load("./src/assets/selva_ranking.webp"), SCREEN_SIZE), ORIGEN)

        font = pygame.font.Font(None, 36)
        y_offset = 60
        for score in scores:
            score_text = font.render(f'Puntuacion: {score[0]}', True, (0, 0, 0))
            pantalla.blit(score_text, (300, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(60)