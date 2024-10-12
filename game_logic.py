import pygame
import random
from board import Board

class MemoryGame:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.board = Board(screen)
        self.first_card = None
        self.second_card = None
        self.matched_pairs = 0

    def handle_click(self, pos):
        clicked_card = self.board.get_card_at(pos)

        if clicked_card is not None and not clicked_card.revealed:
            if self.first_card is None:
                self.first_card = clicked_card
                clicked_card.reveal()
            elif self.second_card is None:
                self.second_card = clicked_card
                clicked_card.reveal()
                self.check_match()

    def check_match(self):
        if self.first_card.emoji == self.second_card.emoji:
            self.first_card.matched = True
            self.second_card.matched = True
            self.matched_pairs += 1
        else:
            pygame.time.wait(1000)
            self.first_card.hide()
            self.second_card.hide()

        self.first_card = None
        self.second_card = None

    def draw(self):
        self.board.draw()






# import pygame
# import random
# import time

# # Inicializar Pygame
# pygame.init()

# # Colores
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (150, 150, 150)
# GREEN = (100, 255, 100)
# RED = (255, 100, 100)

# # Configurar la pantalla
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Juego de Memoria")

# # Fuentes y textos
# font = pygame.font.SysFont(None, 55)

# # Cartas y variables
# emojis = ['🍎', '🍌', '🍓', '🍍', '🍇', '🍉', '🥝', '🍒']
# cards = emojis * 2
# random.shuffle(cards)

# # Dimensiones de las cartas
# CARD_WIDTH = 80
# CARD_HEIGHT = 100
# MARGIN = 10

# # Variables del juego
# first_card = None
# second_card = None
# matched_pairs = 0
# game_over = False
# board = [None] * 16
# revealed = [False] * 16
# start_time = time.time()

# # Función para dibujar texto
# def draw_text(text, font, color, x, y):
#     text_obj = font.render(text, True, color)
#     screen.blit(text_obj, (x, y))

# # Función para dibujar el tablero
# def draw_board():
#     screen.fill(WHITE)
#     for i in range(16):
#         x = (i % 4) * (CARD_WIDTH + MARGIN) + 50
#         y = (i // 4) * (CARD_HEIGHT + MARGIN) + 50
#         if revealed[i]:
#             draw_text(cards[i], font, BLACK, x + 20, y + 20)
#         else:
#             pygame.draw.rect(screen, GRAY, (x, y, CARD_WIDTH, CARD_HEIGHT))

# # Verificar si el juego se ha ganado
# def check_win():
#     global matched_pairs, game_over
#     if matched_pairs == len(emojis):
#         game_over = True
#         draw_text("¡Ganaste!", font, GREEN, 200, 180)
#         pygame.display.update()
#         time.sleep(3)

# # Loop principal del juego
# running = True
# while running:
#     screen.fill(WHITE)
#     draw_board()

#     # Evento de cierre de la ventana
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x, y = pygame.mouse.get_pos()
#             row = (y - 50) // (CARD_HEIGHT + MARGIN)
#             col = (x - 50) // (CARD_WIDTH + MARGIN)
#             index = row * 4 + col

#             if 0 <= index < 16 and not revealed[index]:
#                 if first_card is None:
#                     first_card = index
#                     revealed[first_card] = True
#                 elif second_card is None:
#                     second_card = index
#                     revealed[second_card] = True

#                     # Verificar si coinciden
#                     if cards[first_card] == cards[second_card]:
#                         matched_pairs += 1
#                         first_card = None
#                         second_card = None
#                         check_win()
#                     else:
#                         pygame.display.update()
#                         time.sleep(1)
#                         revealed[first_card] = False
#                         revealed[second_card] = False
#                         first_card = None
#                         second_card = None

#     # Mostrar el tiempo restante
#     elapsed_time = int(time.time() - start_time)
#     draw_text(f"Tiempo: {elapsed_time}s", font, BLACK, 400, 10)

#     pygame.display.update()

# pygame.quit()