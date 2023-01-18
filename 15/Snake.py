import arcade

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=25
        self.height=25
        self.center_x=250
        self.center_y=250
        self.change_x=0
        self.change_y=0
        self.speed=4
        self.score=1
        self.body=[]
        self.color=arcade.color.RED_BROWN
 
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        for i in range (1,len(self.body)):
                if i%2==0:
                    arcade.draw_rectangle_filled(self.body[i]['x'] , self.body[i]['y'] , self.width , self.height, arcade.color.YELLOW)
                elif i%2 !=0:
                    arcade.draw_rectangle_filled(self.body[i]['x'] , self.body[i]['y'] , self.width , self.height, self.color)
            
    def move(self):
        self.body.append({'x':self.center_x,'y':self.center_y})  
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed

    def eat(self,food,add_score):
        del food
        self.score+=add_score  