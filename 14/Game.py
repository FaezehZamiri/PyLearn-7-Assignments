import arcade
import time
from SpaceCraft import SpaceCraft
from Enemy import Enemy
from Count import Count

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,600,600,"Silver Space Craft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.width=600
        self.height=600
        self.me=SpaceCraft(self.width,self.height)
        self.enemy_list=arcade.SpriteList()
        self.score=0
        self.start_time=time.time()
        #self.t=random.randint(2,6)
        self.t=3
        self.gun_sound=arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound=arcade.sound.load_sound(":resources:sounds/explosion2.wav")
        self.count_list=[None,None,None]
        self.game=""
        self.max_x=0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background_image)
        arcade.draw_text(f"Score: {self.score}",500, 20, arcade.color.WHITE, 14)
        self.me.draw()
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(len(self.count_list)):
            self.count_list[i].draw()
        if self.game=="gameover":
            arcade.start_render()
            arcade.draw_text("Game Over",110, 300, arcade.color.WHITE, 54)
            score_taken_formatted = f"{round(self.score, 2)}"
            arcade.draw_text(f"Score taken: {score_taken_formatted}",300,200,arcade.color.GRAY,font_size=15,anchor_x="center")            
        
    def on_key_press(self, symbol, modifiers):
        if symbol== arcade.key.RIGHT:
            #self.me.change_angle=-1
            self.me.change_x=1
        elif symbol==arcade.key.LEFT:
            #self.me.change_angle=1
            self.me.change_x=-1

        elif symbol==arcade.key.SPACE:
            self.me.fire()
            arcade.sound.play_sound(self.gun_sound)
    
    def on_key_release(self, symbol,modifiers):
        #self.me.change_angle=0 
        self.me.change_x=0

    def on_update(self, delta_time):
        self.me.rotate()
        self.end_time=time.time()
        for i in range(len(self.count_list)):
            self.count_list[i]=Count()
            self.count_list[i].center_x=30*i+30

        if self.end_time-self.start_time>=self.t:
            self.enemy_list.append(Enemy())
            self.start_time=time.time()
            #self.t=random.randint(2,6)
            self.t=3

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move((i+1))

        for bullet in self.me.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                arcade.sound.play_sound(self.hit_sound)
                self.score+=1
        j=0
        for enemy in self.enemy_list:
            if enemy.center_y<0: 
                j+=1
                if j==1:
                    try:
                        self.count_list.pop(2)
                    except(IndexError):
                        pass
                elif j==2:
                    try:
                        self.count_list.pop(1)
                    except(IndexError):
                        pass
                elif j==3:
                    try:
                        self.count_list.pop(0)
                    except(IndexError):
                        pass
                    self.game="gameover"
                    arcade.exit()
        
game=Game()
arcade.run()

