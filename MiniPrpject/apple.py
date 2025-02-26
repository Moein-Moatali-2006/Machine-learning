import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("pictures\Apple.png")
        self.width = 16
        self.height = 16
        self.center_x = random.randint( 15 , game.width-15 ) // 8 * 8 
        self.center_y = random.randint( 15 , game.height-15 ) // 8 * 8
        self.change_x = 0
        self.change_y = 0
