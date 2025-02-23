import pandas as pd
#
import time
import arcade
from fruits import Apple
from fruits import Pear
from fruits import PP
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=400,title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.food=Apple(self)
        self.new_food=Pear(self)
        self.shit=PP(self)
        self.snake=Snake(self)
        self.game_over="Game Over"
        self.end_play=False
        self.play=True

        self.dataset = []

        

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
        self.new_food.draw()
        self.shit.draw()
        arcade.draw_text(f"Score:{self.snake.score}", self.width-120, 15, font_size=20, color=arcade.color.RED)
        if self.end_play:
            arcade.draw_text(self.game_over, 100, 100, font_size=50, color=arcade.color.BLACK)
            self.play=False
            
            
        arcade.finish_render()


    def on_update(self, delta_time: float):
        # جمع آوری دیتا
        data = {"w0":None,
                "w1":None,
                "w2":None,
                "w3":None,
                "a0":None,
                "a1":None,
                "a2":None,
                "a3":None,
                "b0":None,
                "b1":None,
                "b2":None,
                "b3":None,
                "direction":None}
        
        if self.snake.center_x == self.food.center_x and self.snake.center_y < self.food.center_y:
            data["a0"] = 1
            data["a1"] = 0
            data["a2"] = 0
            data["a3"] = 0
        
        elif self.snake.center_x == self.food.center_x and self.snake.center_y > self.food.center_y:
            data["a0"] = 0 
            data["a1"] = 0
            data["a2"] = 1
            data["a3"] = 0
        
        elif self.snake.center_x < self.food.center_x and self.snake.center_y == self.food.center_y:
            data["a0"] = 0 
            data["a1"] = 1
            data["a2"] = 0
            data["a3"] = 0
        
        elif self.snake.center_x < self.food.center_x and self.snake.center_y == self.food.center_y:
            data["a0"] = 0 
            data["a1"] = 0
            data["a2"] = 0
            data["a3"] = 1

        data["w0"] = self.height - self.snake.center_y
        data["w1"] = self.width - self.snake.center_x
        data["w2"] = self.snake.center_y
        data["w3"] = self.snake.center_x

        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y < part["y"]:
                data["b0"] = 1 
                data["b1"] = 0
                data["b2"] = 0
                data["b3"] = 0
            elif self.snake.center_x == part["x"] and self.snake.center_y > part["y"]:
                data["b0"] = 0 
                data["b1"] = 0
                data["b2"] = 1
                data["b3"] = 0
            elif self.snake.center_x < part["x"] and self.snake.center_y == part["y"]:
                data["b0"] = 0 
                data["b1"] = 1
                data["b2"] = 0
                data["b3"] = 0
            elif self.snake.center_x > part["x"] and self.snake.center_y == part["y"]:
                data["b0"] = 0 
                data["b1"] = 0
                data["b2"] = 0
                data["b3"] = 1

        self.dataset.append(data)
        self.snake.move_ai(self.food.center_x,self.food.center_y)

        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or (self.snake.center_y > self.height) or (self.snake.center_y < 0):
            self.end_play=True

        if arcade.check_for_collision(self.food , self.snake):
            self.snake.eat(self.food)
            self.food=Apple(self)

        if arcade.check_for_collision(self.snake , self.new_food):
            self.snake.eat(self.new_food)
            self.new_food=Pear(self)
            self.snake.score += 1

        if arcade.check_for_collision(self.snake ,self.shit):
            self.snake.eat(self.shit)
            self.shit=PP(self)
            self.snake.score = self.snake.score - 2
        
        if self.snake.score < 0 :
            self.end_play = True

        if self.play ==False:
            time.sleep(5)
            print(f"Your Score:{self.snake.score}")
            print("Thank you,I hope you will be good luck!")
            exit(0)
    
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            df = pd.DataFrame(self.dataset)
            df.to_csv("dataset.csv",index=False)
            arcade.close_window()
            exit(0)
            

game=Game()
arcade.run()