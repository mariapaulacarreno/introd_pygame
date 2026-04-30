# importamos la libreria pygame
import pygame

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana 
pygame.display.set_caption("pygame Guanentá")

# definir colores
azul = (0,0,255)

# creamos una superficie
superficie_1 = pygame.Surface((400,400))

# Rellenamos la superficie de color
superficie_1.fill(azul)

#agregar o mover la superficie a la ventana 
ventana.blit(superficie_1, (0,0))

# Actualizar visualización de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()
