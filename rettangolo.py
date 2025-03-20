import pygame

class Rettangolo:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
    
        self.width, self.height = 150, 100
        self.rettangolo_color = (0, 150, 3)

        self.rect = pygame.Rect (0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

    def draw_rettangolo(self):
        self.screen.fill(self.rettangolo_color, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.top<=0) or (self.rect.bottom >=screen_rect.bottom)

    def invert(self):
        if self.check_edges():
            self.settings.rettangolo_direction*= -1

    def update(self):
        self.rect.y += self.settings.rettangolo_speed * self.settings.rettangolo_direction
        self.invert()



