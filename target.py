import sys
from time import sleep
import pygame
from settings import Settings
from rettangolo import Rettangolo
from ship import Ship
from bullet import Bullet
from stats import Stats
from button import Button

class Target():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = (self.settings.bg_color)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('🔥 PALLA CONTRO RETTANGOLO! 🔥')
        self.rettangolo = Rettangolo(self)
        self.rettangolo_active = True
        self.ship = Ship(self)
        self.stats = Stats(self)
        self.bullets = pygame.sprite.Group()
        self.game_active = False
        self.play_button = Button (self, "Play")

    def run_game (self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.rettangolo.update()
                self._update_rettangolo()
            self._update_screen()
            self.clock.tick(60)
            self.rettangolo_active=True

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.dynamic_settings()
            self._play_game()

    def _play_game(self):
        self.stats.reset_stats()
        self.game_active = True
        self.bullets.empty()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet ()
        elif event.key == pygame.K_p:
            self._play_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet (self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
            self._check_bullet_rettangolo_collisions()
    
    def _check_bullet_rettangolo_collisions(self):
        collisions = pygame.sprite.spritecollideany(self.rettangolo, self.bullets)
        if not self.rettangolo:
            self.bullets.empty()
            self.rettangolo.draw_rettangolo()
    
    def _update_rettangolo(self):
        if pygame.sprite.spritecollideany(self.rettangolo, self.bullets):
            self._rettangolo_hit()

    def _rettangolo_hit(self):
        if self.stats.rettangolo_ammaccato > 0:
            self.stats.rettangolo_ammaccato -=1
            self.bullets.empty()
            self.settings.increase_speed()
        else:
            self.rettangolo_active=False
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if self.rettangolo_active:
            self.rettangolo.draw_rettangolo()
        self.ship.draw_ship()

        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    game = Target()
    game.run_game()
