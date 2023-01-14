import arcade
import random

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width=random.randint(30,50)
        self.height=self.width
        self.speed=1
        self.angle=180
        self.center_x=random.randint(0,600)
        self.center_y=600
    
    def move(self,k):
        self.center_y-=self.speed*k