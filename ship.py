import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.screen_rect = game.screen.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        self.color = (252, 19, 3)

        self.y = float (self.rect.y)
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_down and self.rect.bottom +60 < self.screen_rect.bottom: #Il + 60 serve a evitare che il cerchio esca dallo schermo quando va giù.
            self.y += self.settings.ship_speed 
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        self.rect.y = self.y
        
    # def draw_ship(self):
    #     pygame.draw.circle (self.screen, self.color, (80, int(self.y)), 70) # pygame.draw.circle(SCREEN, COLORE, CENTER1, RADIUS) self.y è la posizione verticale della ship.

    def draw_ship(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.x + 80, self.rect.y + 80), 70)

        
    def center_ship(self):
        self.rect.topleft = self.screen_rect.topleft
        self.y = float(self.rect.y)



# SUPERFICIE → Dove disegnare (nel tuo caso, self.screen).
# COLORE → Colore RGB del cerchio.
# (X, Y) → Coordinate del centro del cerchio.
# RAGGIO → Distanza dal centro al bordo del cerchio.

