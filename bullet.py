import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midright = game.ship.rect.midright 

        self.x= float (self.rect.x)

    def update (self):
        self.x += self.settings.bullet_speed # aggiorna la posizione, quindi lo fa muovere
        self.rect.x = self.x

    def draw_bullet (self):
        pygame.draw.rect (self.screen, self.color, self.rect)# la funzione draw.rect riempie la parte di schermo definita dal rect del bullet col colore del bullet; parametri: superficie, colore e oggetto pygame Rect.