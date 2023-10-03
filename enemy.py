import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0, width)
        self.center_y = height + 24
        self.angle = 180
        self.width = 50
        self.height = 50
        self.speed = 2

    def move(self):
        self.center_y -= self.speed