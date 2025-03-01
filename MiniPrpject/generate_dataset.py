import arcade
import pandas as pd
from apple import Apple
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=400, title="Snake game ML 🐍 V2")
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(self)
        self.snake = Snake(self)
        self.game_over = "Game Over"
        self.end_play = False
        self.play = True
        self.dataset = []

    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()
        arcade.draw_text(f"Score:{self.snake.score}", self.width - 120, 15, font_size=20, color=arcade.color.RED)
        if self.end_play:
            arcade.draw_text(self.game_over, 100, 100, font_size=50, color=arcade.color.BLACK)
            self.play = False
        arcade.finish_render()

    def on_update(self, delta_time: float):
        distance_x = self.snake.center_x - self.apple.center_x
        distance_y = self.snake.center_y - self.apple.center_y

        data = {
            "wall up": self.height - self.snake.center_y,  
            "wall right": self.width - self.snake.center_x,       
            "wall down": self.snake.center_y,                    
            "wall left": self.snake.center_x,                    
            "apple up":0,  
            "apple right":0,  
            "apple down":0,  
            "apple left":0,  
            'distance x': distance_x,
            'distance y': distance_y,   
            "direction": None 
        }

    
        if self.snake.center_x == self.apple.center_x:
            if self.snake.center_y < self.apple.center_y:
                data["apple up"] = 1  
            else:
                data["apple down"] = 1  
        elif self.snake.center_y == self.apple.center_y:
            if self.snake.center_x < self.apple.center_x:
                data["apple right"] = 1  
            else:
                data["apple left"] = 1  
        
        if self.snake.change_x == 0 and self.snake.change_y == 1:
            data["direction"] = 0  
        elif self.snake.change_x == 1 and self.snake.change_y == 0:
            data["direction"] = 1  
        elif self.snake.change_x == 0 and self.snake.change_y == -1:
            data["direction"] = 2  
        elif self.snake.change_x == -1 and self.snake.change_y == 0:
            data["direction"] = 3  

        self.dataset.append(data)

        if self.snake.center_x < self.apple.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif self.snake.center_y > self.apple.center_y :
            self.snake.change_y = -1
            self.snake.change_x = 0
        elif self.snake.center_y < self.apple.center_y :
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif self.snake.center_x > self.apple.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
        
        self.snake.move()

        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or (self.snake.center_y > self.height) or (self.snake.center_y < 0):
            self.end_play = True
   
        if arcade.check_for_collision(self.apple, self.snake):
            self.snake.eat(self.apple)
            self.apple = Apple(self)
       
        if self.snake.score < 0:
            self.end_play = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            if self.dataset: 
                df = pd.DataFrame(self.dataset)
                df.to_csv("dataset.csv", index=False)
            arcade.close_window()
            exit(0)


game = Game()
arcade.run()