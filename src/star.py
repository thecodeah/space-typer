import random

import arcade

class Star:
    def __init__(self, screen_width, screen_height):
        self.x = random.randrange(screen_width + 200)
        self.y = random.randrange(screen_height)
        self.size = random.randrange(4)
        self.speed = random.randrange(20, 40)
        self.color = random.choice([arcade.color.PURPLE, arcade.color.BLUEBERRY])
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
    
    def reset_pos(self, screen_width, screen_height):
        self.x = random.randrange(screen_width, screen_width + 100)
        self.y = random.randrange(screen_height)