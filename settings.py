class Settings():
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        
        self.rettangolo_direction = 1
        self.rettangolo_ammaccato = 3
        self.rettangolo_color = (0, 150, 3)
        
        self.ship_limit = 3
        self.bullet_width = 15
        self.bullet_height = 500
        self.bullet_speed = 3
        self.bullet_color = (250, 112, 213)
        self.speed_booster = 1.1
        self.dynamic_settings()

    def dynamic_settings(self):
        self.rettangolo_speed = 1.0
        self.ship_speed= 2

    def increase_speed(self):
        self.rettangolo_speed *= self.speed_booster
        self.ship_speed *= self.speed_booster

