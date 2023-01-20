import arcade
import random

class Ball(arcade.Sprite):
    def __init__(self ,game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.speed = 3
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = random.choice([-1,1])
        self.change_y = random.choice([-1,1])
        self.radius = 15
        self.color = arcade.color.PINK

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

class Rocket(arcade.Sprite):
    def __init__(self,x ,y ,c):
        super().__init__()
        self.width = 10
        self.height = 60
        self.speed = 4
        self.change_x = 0
        self.change_y = 0
        self.center_x = x
        self.center_y = y
        self.color = c
        self.score = 0

    def move(self):
        self.center_y += self.change_y * self.speed
        if self.center_y < 60:
            self.center_y = 60
        if self.center_y > 800-60:
            self.center_y = 800-60
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x ,self.center_y ,self.width ,self.height ,self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title="Pong")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.rocket1 = Rocket(40,self.height//2,arcade.color.RED)
        self.rocket2 = Rocket(self.width-40,self.height//2,arcade.color.BLUE)
        self.ball = Ball(self)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width-30, self.height-30, arcade.color.WHITE, border_width=10)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, arcade.color.WHITE, line_width=10)
        arcade.draw_text(f"Score Player 1: {self.rocket1.score}",50, 40, arcade.color.WHITE, 14)
        arcade.draw_text(f"Score Player 2: {self.rocket2.score}",self.width-200, 40, arcade.color.WHITE, 14)
        self.rocket1.draw()
        self.rocket2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x:int, y:int, dx:int, dy:int):
        if self.rocket1.height < y < self.height-self.rocket1.height:
            self.rocket1.center_y = y

    def on_update(self, delta_time:float):
        self.ball.move()
        if self.ball.center_y < 30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1
        
        if arcade.check_for_collision(self.rocket1,self.ball) or arcade.check_for_collision(self.rocket2,self.ball):
            self.ball.change_x *= -1

        #if arcade.check_for_collision_with_list(self.ball,[self.rocket1,self.rocket2]):
        #    self.ball.change_x *= -1

        if self.ball.center_x < 0 :
            self.rocket2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            self.rocket1.score += 1
            del self.ball
            self.ball = Ball(self)
        
        if self.ball.center_x >= self.width-250 :
            if self.ball.center_y > ((self.rocket2.center_y)+self.rocket2.height//2):
                self.rocket2.change_y = 1
                self.rocket2.move()
            elif self.ball.center_y < ((self.rocket2.center_y)+self.rocket2.height//2):
                self.rocket2.change_y = -1
                self.rocket2.move()

game = Game()
arcade.run()