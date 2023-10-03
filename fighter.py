import arcade
from bullet import Bullet

class Fighter(arcade.Sprite):
    def __init__(self, game, w, h, name):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")        
        self.center_x = game.width // 2
        self.center_y = 80
        self.width = 50
        self.height = 50
        self.speed = 4
        self.name = name
        self.change_x = 0
        self.change_y = 0
        self.game_width = w
        self.game_height = h
        self.bullet_list = []
    
    def move(self):

        if self.change_x == -1 :
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1 :
            if self.center_x < self.game_width :
                self.center_x += self.speed

        elif self.change_y == 1 :
            if self.center_y < self.game_height:
                self.center_y += self.speed
                
        elif self.change_y == -1 :
            if self.center_y > 0:
                self.center_y -= self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
