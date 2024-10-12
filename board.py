import pygame
import random

class Card:
    def __init__(self, emoji, rect):
        self.emoji = emoji
        self.rect = rect
        self.revealed = False
        self.matched = False

    def draw(self, screen, font):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)  # Fondo de la carta
        if self.revealed or self.matched:
            text = font.render(self.emoji, True, (0, 0, 0))
            screen.blit(text, (self.rect.x + 20, self.rect.y + 20))

    def reveal(self):
        self.revealed = True

    def hide(self):
        if not self.matched:
            self.revealed = False


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.emojis = ['🍎', '🍌', '🍓', '🍍', '🍇', '🍉', '🥝', '🍒']
        self.cards = []
        self.font = pygame.font.SysFont(None, 55)
        self.create_board()

    def create_board(self):
        all_emojis = self.emojis * 2
        random.shuffle(all_emojis)

        for i in range(16):
            x = (i % 4) * 100 + 50
            y = (i // 4) * 120 + 50
            rect = pygame.Rect(x, y, 80, 100)
            card = Card(all_emojis[i], rect)
            self.cards.append(card)

    def draw(self):
        for card in self.cards:
            card.draw(self.screen, self.font)

    def get_card_at(self, pos):
        for card in self.cards:
            if card.rect.collidepoint(pos):
                return card
        return None