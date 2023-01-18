import random 
import arcade

class Pear(arcade.Sprite):
    def __init__(self):
        super().__init__("pear.png")
        self.width=35
        self.height=35
        self.center_x=random.randint(10,450)
        self.center_y=random.randint(10,450)
        self.change_x=0
        self.change_y=0
        self.add_score=2
        
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__("apple.png")
        self.width=35
        self.height=35
        self.center_x=random.randint(10,450)
        self.center_y=random.randint(10,450)
        self.change_x=0
        self.change_y=0
        self.add_score=1

class Chili(arcade.Sprite):
    def __init__(self):
        super().__init__("chili.png")
        self.width=35
        self.height=35
        self.center_x=random.randint(10,450)
        self.center_y=random.randint(10,450)
        self.change_x=0
        self.change_y=0
        self.add_score=-1