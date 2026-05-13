# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame
import math

pygame.init()

# Ventana
ANCHO = 900
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ciudad Pacman")

# Colores
AZUL = (120, 200, 255)
VERDE = (0, 180, 90)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (120, 120, 120)
ROJO = (255, 80, 80)
MORADO = (180, 100, 255)
NARANJA = (255, 150, 0)

# Fuente
fuente = pygame.font.SysFont("Arial", 35)

# Función para dibujar pacman
def dibujar_pacman(x, y, color):

    # cuerpo
    pygame.draw.circle(pantalla, color, (x, y), 35)

    # boca
    pygame.draw.polygon(pantalla,NEGRO,[(x, y), (x + 35, y - 12), (x + 35, y + 12)])

    # ojo
    pygame.draw.circle(pantalla, NEGRO, (x - 10, y - 12), 5)

# Función edificios
def edificio(x, y, color):

    pygame.draw.rect(pantalla, color, (x, y, 120, 250))


# Bucle principal
ejecutar = True

while ejecutar:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

    # Fondo
    pantalla.fill(AZUL)

    # Piso
    pygame.draw.rect(pantalla, VERDE, (0, 470, ANCHO, 130))

    # Sol
    pygame.draw.circle(pantalla, AMARILLO, (750, 80), 50)

    # Edificios
    edificio(50, 220, ROJO)
    edificio(250, 180, MORADO)
    edificio(450, 200, GRIS)

    # Rueda de la fortuna
    pygame.draw.circle(pantalla, NARANJA, (730, 300), 90, 7)

    # Líneas rueda
    pygame.draw.line(pantalla, BLANCO, (730, 210), (730, 390), 4)
    pygame.draw.line(pantalla, BLANCO, (640, 300), (820, 300), 4)

    pygame.draw.line(pantalla, BLANCO, (670, 240), (790, 360), 4)
    pygame.draw.line(pantalla, BLANCO, (790, 240), (670, 360), 4)

    # Base rueda
    pygame.draw.line(pantalla, NEGRO, (700, 470), (730, 390), 5)
    pygame.draw.line(pantalla, NEGRO, (760, 470), (730, 390), 5)

    # Camino
    pygame.draw.rect(pantalla, GRIS, (0, 430, 900, 50))

    # Pacmans
    dibujar_pacman(150, 520, AMARILLO)
    dibujar_pacman(420, 520, ROJO)
    dibujar_pacman(620, 520, MORADO)

    # Texto
    titulo = fuente.render("PACMAN CITY", True, BLANCO)
    pantalla.blit(titulo, (320, 20))
    fuente_Georgia = pygame.font.SysFont("Georgia", 35, 1 , 1)
    texto = fuente_Georgia.render("Maria Paula",1,BLANCO)
    pantalla.blit(texto, (0,50))

    pygame.display.update()
pygame.quit()