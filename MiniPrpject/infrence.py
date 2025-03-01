import arcade
import pandas as pd
import numpy as np
import tensorflow as tf
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
        self.model = tf.keras.models.load_model("Snake_game_model_ML_ANN_Classification.h5")
        print("Model loaded...!")
        

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

        x_test = {
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
        }

    
        if self.snake.center_x == self.apple.center_x:
            if self.snake.center_y < self.apple.center_y:
                x_test["apple up"] = 1  
            else:
                x_test["apple down"] = 1  
        elif self.snake.center_y == self.apple.center_y:
            if self.snake.center_x < self.apple.center_x:
                x_test["apple right"] = 1  
            else:
                x_test["apple left"] = 1   

        
        # for part in self.snake.body:
        #     if self.snake.center_x == part["x"]:
        #         if self.snake.center_y < part["y"]:
        #             x_test["b0"] = 1  
        #         else:
        #             x_test["b2"] = 1  
        #     elif self.snake.center_y == part["y"]:
        #         if self.snake.center_x < part["x"]:
        #             x_test["b1"] = 1  
        #         else:
        #             x_test["b3"] = 1  

        # move
        x_test_array = np.array(list(x_test.values())).reshape(1,-1)
        y_pred = self.model.predict(x_test_array)
        print(y_pred)
        output = np.argmax(y_pred)
        print(output)
        self.snake.move_ml(output)
       
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
            arcade.close_window()
            exit(0)


game = Game()
arcade.run()