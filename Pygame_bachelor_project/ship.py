import pygame
from settings import Settings
from pygame.sprite import Sprite

# Klasa przeznaczona do zarządzania statkiem kosmicznym
class Ship(Sprite):
    # Inicjalizacja statku kosmicznego i jego położenie początkowe
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('./ship.bmp')
        self.rect = self.image.get_rect()
        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom
        # Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)
        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # Uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        # Wyświetlenie statu kosmicznego w jego aktualnym położeniu
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


