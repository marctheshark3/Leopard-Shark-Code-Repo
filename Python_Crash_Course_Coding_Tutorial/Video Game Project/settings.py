class Settings:

    def __init__(self):
        ''' Initialize the game's static setting'''

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ships settings

        self.ship_limit = 1

        #Bullet Settings

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 20

        #alien settings

        self.fleet_drop_speed = 10


        #how quickly game is to speed up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initializing the dynamic settings'''
        self.ship_speed = 5 * 10
        self.bullet_speed = 5 * 7
        self.alien_speed = .5

        # fleet direction of 1 represents right and -1 left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        '''increase the speed settings'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


