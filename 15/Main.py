import random 
import arcade
from Fruit import Apple , Pear , Chili  
from Snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title='Snake')
        arcade.set_background_color(arcade.color.KHAKI)

        self.food = Apple()
        self.snake = Snake()
        self.chili = Chili()
        self.game = ""

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Score: {self.snake.score}",20, 20, arcade.color.WHITE, 14)
        self.food.draw()
        self.snake.draw()
        self.chili.draw()
        arcade.finish_render()

        if self.game=="gameover":
            arcade.exit()
            arcade.start_render()
            arcade.draw_text("Game Over",100, 250, arcade.color.WHITE, 45)
            score_taken_formatted = f"{round(self.snake.score, 2)}"
            arcade.draw_text(f"Score taken: {score_taken_formatted}",250,100,arcade.color.GRAY,font_size=15,anchor_x="center")  
            arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0


    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.food):
            self.snake.eat(self.food,self.food.add_score)
            self.food=random.choice([Apple(),Pear()])
        elif arcade.check_for_collision(self.snake,self.chili):
            self.snake.eat(self.chili,self.chili.add_score)
            self.chili=Chili()

        if self.snake.score==0:
            self.game="gameover"

        if self.snake.center_x >= 499 or self.snake.center_y >= 499 or self.snake.center_x <= 1 or self.snake.center_y <= 1:
            self.game="gameover"
        
        for cell in self.snake.body: 
            if self.snake.center_x == cell['x'] and self.snake.center_y == cell['y'] and len(self.snake.body) > 2 :
                self.game="gameover"

if __name__ == "__main__":
  game = Game()
  arcade.run()