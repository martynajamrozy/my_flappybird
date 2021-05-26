import arcade
import random

from arcade.key import J

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
SCREEN_TITLE = "FlappyBird"
CHARACTER_SCALING = 0.15
PIPE_SCALING = 0.3
JUMP_SPEED = 10
MOVE_SPEED = 5
RIGHT_VIEWPORT_MARGIN = 300



class FlappyBird(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE, resizable=False)
        self.flappybird_list = None
        self.pipedown_list = None
        self.pipeup_list = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        self.flappybird_list = arcade.SpriteList()
        self.pipedown_list =arcade.SpriteList()
        self.pipeup_list =arcade.SpriteList()
        self.flappybird_sprite = arcade.Sprite("flappybird.png", CHARACTER_SCALING)
        self.flappybird_sprite.center_x = 64
        self.flappybird_sprite.center_y =200
        self.flappybird_list.append(self.flappybird_sprite)
        
        up =[]
        for x in range(200, 100000,250):
                self.pipeup = arcade.Sprite("pipe.png", PIPE_SCALING)
                self.pipeup.center_x = x
                self.pipeup.center_y = random.randrange(-50, 100)
                self.pipeup_list.append(self.pipeup)
                up.append(self.pipeup.center_y)
        for i in range(200, 100000, 250):
                self.pipedown = arcade.Sprite("pipe2.png", PIPE_SCALING)
                self.pipedown.center_x = i
                for g in up:
                    if g > 0:
                        self.pipedown.center_y = random.randrange(360 + g, 460)
                        self.pipedown_list.append(self.pipedown)
                    else:
                        self.pipedown.center_y = random.randrange(300, 460)
                        self.pipedown_list.append(self.pipedown)
     

    def on_draw(self):
        arcade.start_render()
        self.flappybird_list.draw()
        self.pipeup_list.draw()
        self.pipedown_list.draw()


    def on_update(self, delta_time):
        self.flappybird_list.update()
        changed = False
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.flappybird_sprite.right > right_boundary:
            self.view_left += self.flappybird_sprite.right - right_boundary
            changed = True
            if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
                self.view_bottom = int(self.view_bottom)
                self.view_left = int(self.view_left)

            # Do the scrolling
                arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.flappybird_sprite.change_y = JUMP_SPEED
            self.flappybird_sprite.change_x = MOVE_SPEED
        
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.flappybird_sprite.change_y = -3
           
def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()