# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame

# Inicializar Pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 1000, 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ciudad de Hierro - Fondo y Edificios")

# Colores
CIELO = (90, 180, 255)
SUELO = (40, 160, 80)
GRIS = (130, 130, 130)
GRIS_OSCURO = (90, 90, 90)
AMARILLO = (255, 240, 120)
NEGRO = (0, 0, 0)

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # =========================
    # FONDO
    # =========================
    pantalla.fill(CIELO)

    # Suelo
    pygame.draw.rect(pantalla, SUELO, (0, 500, ANCHO, 200))

    # =========================
    # EDIFICIOS
    # =========================

    # Edificio 1 (alto)
    pygame.draw.rect(pantalla, GRIS, (80, 200, 140, 300))

    # Ventanas edificio 1
    for i in range(5):
        for j in range(3):
            pygame.draw.rect(
                pantalla,
                AMARILLO,
                (100 + j * 35, 230 + i * 55, 20, 25)
            )

    # Edificio 2 (mediano)
    pygame.draw.rect(pantalla, GRIS_OSCURO, (260, 260, 160, 240))

    # Ventanas
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(
                pantalla,
                AMARILLO,
                (275 + j * 35, 290 + i * 50, 18, 20)
            )

    # Edificio 3 (alto moderno)
    pygame.draw.rect(pantalla, GRIS, (470, 180, 130, 320))

    # Líneas decorativas (tipo hierro)
    for i in range(6):
        pygame.draw.line(
            pantalla,
            NEGRO,
            (470, 200 + i * 50),
            (600, 200 + i * 50),
            2
        )

    # Edificio 4 (bloque grande)
    pygame.draw.rect(pantalla, GRIS_OSCURO, (640, 230, 200, 270))

    # Ventanas simples
    for i in range(3):
        for j in range(5):
            pygame.draw.rect(
                pantalla,
                AMARILLO,
                (660 + j * 35, 260 + i * 70, 22, 30)
            )

    # =========================
    # EDIFICIO PEQUEÑO (CUADRADOS)
    # =========================
    pygame.draw.rect(pantalla, GRIS, (880, 300, 80, 200))

    for i in range(4):
        pygame.draw.rect(
            pantalla,
            AMARILLO,
            (890, 320 + i * 45, 20, 25)
        )

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
