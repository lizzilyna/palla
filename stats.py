class Stats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        self.rettangolo_ammaccato = self.settings.rettangolo_ammaccato