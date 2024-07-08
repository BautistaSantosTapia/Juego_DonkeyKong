"""import pygame
import sys

def loop_jugable(pantalla):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                running = False
        

        # Lógica del juego aquí

        pantalla.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)

    # Llamar a la pantalla de game over
    from game_over import pantalla_game_over
    pantalla_game_over(pantalla, 100)"""

