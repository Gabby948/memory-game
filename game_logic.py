import pygame

class MemoryGame:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        self.cards = self.shuffle_cards()
        self.card_size = 80
        self.font = pygame.font.Font(None, 60)
        self.revealed = [False] * len(self.cards)
        self.selected = []
        self.matches = []

    def shuffle_cards(self):
        import random
        random.shuffle(self.cards)
        return self.cards

    def draw(self):
        for i, card in enumerate(self.cards):
            x = (i % 4) * (self.card_size + 10) + 50
            y = (i // 4) * (self.card_size + 10) + 50
            rect = pygame.Rect(x, y, self.card_size, self.card_size)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)

            if self.revealed[i] or i in self.selected or i in self.matches:
                text = self.font.render(card, True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)

    def handle_click(self, pos):
        for i, card in enumerate(self.cards):
            x = (i % 4) * (self.card_size + 10) + 50
            y = (i // 4) * (self.card_size + 10) + 50
            rect = pygame.Rect(x, y, self.card_size, self.card_size)

            if rect.collidepoint(pos) and not self.revealed[i]:
                self.selected.append(i)
                if len(self.selected) == 2:
                    self.check_match()

    def check_match(self):
        if self.cards[self.selected[0]] == self.cards[self.selected[1]]:
            self.matches.extend(self.selected)
        self.revealed = [i in self.matches for i in range(len(self.cards))]
        self.selected.clear()

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