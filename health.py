                        # LIVES

import arcade

class Health ( arcade.Sprite ) :

    def __init__ ( self , x ) :
        super().__init__ ( "New folder\image heart.png" )
        self.width = 22
        self.height = 22
        self.center_x = x
        self.center_y = 20

# resources:images/space_shooter/playerhealth1_orange.png
