class Settings:

    def __init__(self):
        ''' Initialize the game's setting'''

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ships settings
        self.ship_speed = 5 * 10
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed = 5 * 7
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20

        #alien settings
        self.alien_speed = .5
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right and -1 left
        self.fleet_direction = 1



