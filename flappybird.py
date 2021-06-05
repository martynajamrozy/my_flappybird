import arcade
import random

from arcade.key import J
from pyglet import window

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
SCREEN_TITLE = "FlappyBird"
CHARACTER_SCALING = 0.15
PIPE_SCALING = 0.3
JUMP_SPEED = 10
MOVE_SPEED = 5
RIGHT_VIEWPORT_MARGIN = 300

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("FlappyBird Game", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center")
        arcade.draw_text("Click ENTER to START", SCREEN_WIDTH/2, 200, arcade.color.BRUNSWICK_GREEN, 30, anchor_x= "center")
        arcade.draw_text("Click I to read INSTRUCTION", SCREEN_WIDTH/4, 120, arcade.color.DARK_TAUPE, 20, anchor_x= "center")
        arcade.draw_text("Click B to see BEST SCORES", 3*SCREEN_WIDTH/4, 120, arcade.color.DARK_TAUPE, 20, anchor_x= "center")
        arcade.draw_text("Click A to read about THE AUTHOR", SCREEN_WIDTH/4, 80, arcade.color.DARK_TAUPE, 20, anchor_x= "center")
        arcade.draw_text("Click S to make SETUP", 3*SCREEN_WIDTH/4, 80, arcade.color.DARK_TAUPE, 20, anchor_x= "center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        if symbol == arcade.key.I:
            game_view = InstructionView()
            self.window.show_view(game_view)
        if symbol == arcade.key.B:
            game_view = ScoresView()
            self.window.show_view(game_view)
        if symbol == arcade.key.A:
            game_view = AuthorView()
            self.window.show_view(game_view)
        if symbol == arcade.key.S:
            game_view = SetUpView()
            self.window.show_view(game_view)

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.NAVY)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How to play", SCREEN_WIDTH/2, 300, arcade.color.WHITE, 50, anchor_x= "center")
        arcade.draw_text("", SCREEN_WIDTH/2, 200, arcade.color.WHITE, 30, anchor_x= "center")
        arcade.draw_text("", SCREEN_WIDTH/2, 120, arcade.color.WHITE, 20, anchor_x= "center")
        arcade.draw_text("", SCREEN_WIDTH/2, 80, arcade.color.WHITE, 20, anchor_x= "center")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 350, arcade.color.ASH_GREY, 10, anchor_x= "center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class ScoresView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.TEAL)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Best Scores", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 350, arcade.color.ASH_GREY, 10, anchor_x= "center")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class AuthorView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.PLUM)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("About Author", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 350, arcade.color.EBONY, 10, anchor_x= "center")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class SetUpView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Setup", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 350, arcade.color.EBONY, 10, anchor_x= "center")

class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH/2, 300, arcade.color.WHITE, 50, anchor_x= "center")
        arcade.draw_text("Click ENTER to START AGAIN", SCREEN_WIDTH/4, 200, arcade.color.WHITE, 30, anchor_x= "center")
        arcade.draw_text("Click Q to go back to MENU", 3*SCREEN_WIDTH/4, 200, arcade.color.WHITE, 30, anchor_x= "center")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

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

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.flappybird_list = None
        self.background = None
        self.pipedown_list = None
        self.pipeup_list = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        self.background = arcade.load_texture("background.png")
        self.flappybird_list = arcade.SpriteList()
        self.pipedown_list =arcade.SpriteList()
        self.pipeup_list =arcade.SpriteList()
        self.flappybird_sprite = arcade.Sprite("flappybird.png", CHARACTER_SCALING)
        self.flappybird_sprite.center_x = 64
        self.flappybird_sprite.center_y =200
        self.flappybird_list.append(self.flappybird_sprite)
        
        up =[]
        for x in range(250, 50000,250):
            self.pipeup = arcade.Sprite("pipe.png", PIPE_SCALING)
            self.pipeup.center_x = x
            self.pipeup.center_y = random.randrange(-50, 100)
            self.pipeup_list.append(self.pipeup)
            up.append(self.pipeup.center_y)
            self.pipedown = arcade.Sprite("pipe2.png", PIPE_SCALING)
            self.pipedown.center_x = x
            for g in up:
                if g>0:
                    self.pipedown.center_y = random.randrange(360 + g, 460)
                    self.pipedown_list.append(self.pipedown)
                else:
                    self.pipedown.center_y = random.randrange(300, 460)
                    self.pipedown_list.append(self.pipedown)
     

    def on_draw(self):
        arcade.start_render()
        for a in range(0,50000,SCREEN_WIDTH):
            arcade.draw_lrwh_rectangle_textured(a,0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
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
                self.view_bottom = int(self.view_bottom)
                self.view_left = int(self.view_left)
                arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
        self.pipeup_list.update()
        pipes = arcade.check_for_collision

            

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.flappybird_sprite.change_y = JUMP_SPEED
            self.flappybird_sprite.change_x = MOVE_SPEED
        
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.flappybird_sprite.change_y = -3
           
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
