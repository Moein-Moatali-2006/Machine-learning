import random
import arcade


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 16
        self.height = 16
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.speed = 4
        self.change_x = 0
        self.change_y = 0
        self.body = []
        self.score = 0
        self.color = arcade.color.BLACK
        self.colors = [arcade.color.RED]

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        for part in self.body:
            arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, random.choice(self.colors))

    def eat(self, food):
        del food
        self.score += 1

    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def move_ml(self,y_pred):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)

        if y_pred == 0 or y_pred == 0.0:
            self.change_x = 0
            self.change_y = 1
        elif y_pred == 1 or y_pred == 1.0:
            self.change_x = 1
            self.change_y = 0
        elif y_pred == 2 or y_pred == 2.0:
            self.change_x = 0
            self.change_y = -1
        elif y_pred == 3 or y_pred == 3.0:
            self.change_x = -1
            self.change_y = 0
        
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
