import arcade

class Count(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/items/star.png")
        self.center_x=0
        self.center_y=30
        self.width=45
        self.height=45