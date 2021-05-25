import arcade
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
SCREEN_TITLE = "FlappyBird"
CHARACTER_SCALING = 0.15
PIPE_SCALING = 0.3



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE, resizable=False)
        self.flappybird_list = None
        self.pipeup_list = None
        self.pipedown_list = None
        self.flappybird_sprite = None
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        

    def setup(self):
        self.flappybird_list = arcade.SpriteList()
        self.pipedown_list =arcade.SpriteList()
        self.pipeup_list =arcade.SpriteList()
        self.flappybird_sprite = arcade.Sprite("flappybird.png", CHARACTER_SCALING)
        self.flappybird_sprite.center_x = 64
        self.flappybird_sprite.center_y =120
        self.flappybird_list.append(self.flappybird_sprite)

        for x in range(128, SCREEN_WIDTH, 200):
                wall = arcade.Sprite("pipe.png", PIPE_SCALING)
                wall.center_x = x
                wall.center_y = random.randrange(-50, 100)
                self.pipeup_list.append(wall)

        for i in range(128, SCREEN_WIDTH, 200):
                v = wall.center_y
                if v < 0:
                    pipedown = arcade.Sprite("pipe2.png", PIPE_SCALING)
                    pipedown.center_x = i
                    pipedown.center_y = random.randrange(300, 450)
                    self.pipedown_list.append(pipedown)
                else:
                    pipedown = arcade.Sprite("pipe2.png", PIPE_SCALING)
                    pipedown.center_x = i
                    pipedown.center_y = random.randrange(300+v , 450)
                    self.pipedown_list.append(pipedown)

    def on_draw(self):
        arcade.start_render()
        self.flappybird_list.draw()
        self.pipeup_list.draw()
        self.pipedown_list.draw()
    
    


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()