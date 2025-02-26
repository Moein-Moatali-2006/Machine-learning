import time
import arcade
from apple import Apple
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=400,title="Snake game AI 🐍 V2")
        arcade.set_background_color(arcade.color.KHAKI)

        self.apple=Apple(self)
        self.snake=Snake(self)
        self.game_over="Game Over"
        self.end_play=False
        self.play=True
        
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()
        arcade.draw_text(f"Score:{self.snake.score}", self.width-120, 15, font_size=20, color=arcade.color.RED)
        if self.end_play:
            arcade.draw_text(self.game_over, 100, 100, font_size=50, color=arcade.color.BLACK)
            self.play=False
    
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move_ai(self.apple.center_x,self.apple.center_y)

        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or (self.snake.center_y > self.height) or (self.snake.center_y < 0):
            self.end_play=True

        if arcade.check_for_collision(self.apple , self.snake):
            self.snake.eat(self.apple)
            self.apple=Apple(self)

        if self.snake.score < 0 :
            self.end_play = True

        if self.play ==False:
            time.sleep(5)
            print(f"Your Score:{self.snake.score}")
            print("Thank you")
            exit(0)

game=Game()
arcade.run()