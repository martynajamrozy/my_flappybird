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
jump_sound = arcade.load_sound("jump1.wav")
hurt_sound = arcade.load_sound("hurt5.wav")
gameover_sound = arcade.load_sound("gameover4.wav")

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
        arcade.draw_text("Click ENTER to START AGAIN", SCREEN_WIDTH/2, 200, arcade.color.WHITE, 30, anchor_x= "center")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 350, arcade.color.WHITE, 10, anchor_x= "center")
        arcade.set_viewport(0, SCREEN_WIDTH -1, 0, SCREEN_HEIGHT -1)
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


class Collisions(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename,scale)
        self.changed = False

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.flappybird_list = None
        self.background = None
        self.pipedown_list = None
        self.pipeup_list = None
        self.view_bottom = 0
        self.view_left = 0
        self.lives = 3
        self.score = 0

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
        self.lives = 3
        self.score = 0
        
        up =[]
        for x in range(250, 50000,250):
            pipeup = Collisions("pipe.png", PIPE_SCALING)
            pipeup.center_x = x
            pipeup.center_y = random.randrange(-50, 100)
            self.pipeup_list.append(pipeup)
            up.append(pipeup.center_y)
            pipedown = Collisions("pipe2.png", PIPE_SCALING)
            pipedown.center_x = x
            for g in up:
                if g>0:
                    pipedown.center_y = random.randrange(360 + g, 460)
                    self.pipedown_list.append(pipedown)
                else:
                    pipedown.center_y = random.randrange(300, 460)
                    self.pipedown_list.append(pipedown)
                    
    def on_draw(self):
        arcade.start_render()
        for a in range(0,50000,SCREEN_WIDTH):
            arcade.draw_lrwh_rectangle_textured(a,0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.flappybird_list.draw()
        self.pipeup_list.draw()
        self.pipedown_list.draw()
        score_text = f"Score:{self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.WHITE, 18)
        lives_text = f"Lives:{self.lives}"
        arcade.draw_text(lives_text, 10 + self.view_left, 30 + self.view_bottom, arcade.csscolor.WHITE, 18)


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
        self.pipedown_list.update()
        uppipes = arcade.check_for_collision_with_list(self.flappybird_sprite, self.pipeup_list)
        downpipes = arcade.check_for_collision_with_list(self.flappybird_sprite, self.pipedown_list)
        for pipeup in uppipes:
            if not pipeup.changed:
                pipeup.append_texture(arcade.load_texture("pipe.png"))
                arcade.play_sound(hurt_sound)
                pipeup.set_texture(1)
                pipeup.changed = True
                self.lives += -1

        for pipedown in downpipes:
            if not pipedown.changed:
                pipedown.append_texture(arcade.load_texture("pipe2.png"))
                arcade.play_sound(hurt_sound)
                pipedown.set_texture(1)
                pipedown.changed = True
                self.lives += -1
                                      
        if self.lives == 0:
            gameover_view = GameOverView()
            self.window.show_view(gameover_view)
            arcade.play_sound(gameover_sound)

        points = list(range(250, 50000,250))
        for i in points:
            if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+5 :
                self.score +=1
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.flappybird_sprite.change_y = JUMP_SPEED
            arcade.play_sound(jump_sound)
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
