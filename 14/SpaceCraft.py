import arcade
from Bullet import Bullet

class SpaceCraft(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width=50
        self.height=50
        self.center_x=w//2
        self.center_y=self.height
        self.angle=0
        #self.change_angle=0
        self.change_x=0
        self.change_y=0
        self.speed=4
        self.bullet_list=[]
        self.game_width=w
    
    def rotate(self):
        #self.angle+=self.change_angle*self.speed
        if self.change_x == 1:
            if self.center_x< self.game_width:
                self.center_x+=self.speed
        elif self.change_x ==-1:
            if self.center_x>0:
                self.center_x-=self.speed


        #if self.center_x < self.game_width:
            #self.center_x+=self.change_x*self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))