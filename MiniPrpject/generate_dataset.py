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

        data = {
            "w0": self.height - self.snake.center_y,  
            "w1": self.width - self.snake.center_x,       
            "w2": self.snake.center_y,                    
            "w3": self.snake.center_x,                    
            "a0": 0,  
            "a1": 0,  
            "a2": 0,  
            "a3": 0,  
            "b0": 0,  
            "b1": 0,  
            "b2": 0,  
            "b3": 0,  
            "direction": None 
        }

    
        if self.snake.center_x == self.apple.center_x:
            if self.snake.center_y < self.apple.center_y:
                data["a0"] = 1  
            else:
                data["a2"] = 1  
        elif self.snake.center_y == self.apple.center_y:
            if self.snake.center_x < self.apple.center_x:
                data["a1"] = 1  
            else:
                data["a3"] = 1  

        
        for part in self.snake.body:
            if self.snake.center_x == part["x"]:
                if self.snake.center_y < part["y"]:
                    data["b0"] = 1  
                else:
                    data["b2"] = 1  
            elif self.snake.center_y == part["y"]:
                if self.snake.center_x < part["x"]:
                    data["b1"] = 1  
                else:
                    data["b3"] = 1  

        
        if self.snake.change_x == 0 and self.snake.change_y == 1:
            data["direction"] = 0  
        elif self.snake.change_x == 1 and self.snake.change_y == 0:
            data["direction"] = 1  
        elif self.snake.change_x == 0 and self.snake.change_y == -1:
            data["direction"] = 2  
        elif self.snake.change_x == -1 and self.snake.change_y == 0:
            data["direction"] = 3  

        
        self.dataset.append(data)

        
        self.snake.move_ai(self.apple.center_x, self.apple.center_y)

       
        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or \
           (self.snake.center_y > self.height) or (self.snake.center_y < 0):
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