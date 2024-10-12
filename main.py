import pygame
from game_logic import MemoryGame

# Inicializar Pygame
print("Inicializando Pygame...")  # Mensaje de depuración
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Memoria")

# Crear una instancia del juego
print("Creando el juego...")  # Mensaje de depuración
memory_game = MemoryGame(screen, WIDTH, HEIGHT)

# Loop principal
running = True
print("Entrando en el loop principal...")  # Mensaje de depuración
while running:
    screen.fill((255, 255, 255))  # Fondo blanco

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            memory_game.handle_click(event.pos)

    # Actualizar pantalla
    memory_game.draw()
    pygame.display.update()

print("Saliendo del juego...")
pygame.quit()