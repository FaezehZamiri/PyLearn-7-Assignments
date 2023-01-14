import arcade
import math

class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed=4
        self.angle=host.angle
        self.center_x=host.center_x
        self.center_y=host.center_y

    def move(self):
        angle_rad=math.radians(self.angle)
        self.center_x-=self.speed*math.sin(angle_rad)
        self.center_y+=self.speed*math.cos(angle_rad)