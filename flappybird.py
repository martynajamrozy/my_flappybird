import arcade
import random
from arcade.key import J
from pyglet import window

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
SCREEN_TITLE = "FlappyBird"
PIPE_SCALING = 0.3
JUMP_SPEED = 10
RIGHT_VIEWPORT_MARGIN = 300
BOTTOM_VIEWPORT_MARGIN = 0
TOP_VIEWPORT_MARGIN = 0
jump_sound = arcade.load_sound("sounds/jump1.wav")
hurt_sound = arcade.load_sound("sounds/hurt5.wav")
gameover_sound = arcade.load_sound("sounds/gameover4.wav")
nextlevel_sound = arcade.load_sound("sounds/nextlevel.mp3")
winning_sound = arcade.load_sound("sounds/preview.mp3")
blue = arcade.load_texture("pictures/bluebird.png")
yellow = arcade.load_texture("pictures/flappybird.png")
red = arcade.load_texture("pictures/redbird.png")


class MenuView(arcade.View):
    """This class creates a menu view from where you can enter different views by using your keyboard.
        Built-in function arcade. view allows showing the view in our game window."""
    def on_show(self):
        """This function creates a background with chosen color and/or picture."""
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
        self.background = arcade.load_texture("pictures/background.png")
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0, SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        arcade.draw_text("FlappyBird Game", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center", font_name = "fonts/KGHAPPY")
        arcade.draw_text("Click ENTER to START", SCREEN_WIDTH/2, 200, arcade.color.WHITE, 30, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click I to read INSTRUCTION", SCREEN_WIDTH/4, 120, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click B to see BEST SCORES", 3*SCREEN_WIDTH/4, 120, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click A to read about THE AUTHOR", SCREEN_WIDTH/4, 80, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click S to make SETUP", 3*SCREEN_WIDTH/4, 80, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ENTER:
            with open("characters.txt","w") as char:
                char.write("pictures/flappybird.png, 0.15")
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
        arcade.set_background_color(arcade.csscolor.LIGHT_GREEN)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How to play", SCREEN_WIDTH/2, 320, arcade.color.BLACK, 50, anchor_x= "center",font_name = "fonts/KGHAPPY")
        arcade.draw_text("Jump by clicking the SPACE button.", SCREEN_WIDTH/2, 250, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("On release bird starts to fall.", SCREEN_WIDTH/2, 225, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Avoid pipes and crossing top and bottom line of the game.", SCREEN_WIDTH/2, 200, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Crossing top/bottom line ends a game.", SCREEN_WIDTH/2, 175, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("You have 3 lifes. Every collision with pipe substract one life.", SCREEN_WIDTH/2, 150, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Every 25 points you hit next level and a bird starts flying faster.", SCREEN_WIDTH/2, 125, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Good look!", SCREEN_WIDTH/2, 50, arcade.color.BLACK, 30, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.EBONY, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)


class AuthorView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.PLUM)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("About Author", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center",font_name = "fonts/KGHAPPY")
        arcade.draw_text("Welcome to the FlappyBird game made by a first-year student ", SCREEN_WIDTH/2, 250, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("This game was made as an assignment for Programming classes.", SCREEN_WIDTH/2, 150, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("It is a copy of a popular arcade game followed by the same name.", SCREEN_WIDTH/2, 100, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("I hope you'll enjoy it! ", SCREEN_WIDTH/2, 50, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("of Applied Mathematics.", SCREEN_WIDTH/2, 200, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Martyna Jamrozy", 7*SCREEN_WIDTH/8, 25, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")

        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.EBONY, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class SetUpView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Choose your character", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 40, anchor_x= "center",font_name = "fonts/KGHAPPY")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.EBONY, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")
        blue.draw_sized(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, 100, 80)
        yellow.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, 80)
        red.draw_sized(3*SCREEN_WIDTH/4, SCREEN_HEIGHT / 2, 100, 80)
        arcade.draw_text("Click B", SCREEN_WIDTH / 4, 80, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click Y", SCREEN_WIDTH/2, 80, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click R", 3*SCREEN_WIDTH / 4,80, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        if symbol == arcade.key.B:
            with open("textfiles/characters.txt","w") as char:
                char.write("pictures/bluebird.png, 0.13")
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        if symbol == arcade.key.Y:
            with open("textfiles/characters.txt","w") as char:
                char.write("pictures/flappybird.png, 0.15")
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        if symbol == arcade.key.R:
            with open("textfiles/characters.txt","w") as char:
                char.write("pictures/redbird.png, 0.1")
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        

lista = []        
class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
    def on_draw(self):
        with open("textfiles/yourscore.txt", "r") as yourscore:
            self.text = yourscore.read()
            self.num = int(self.text)
        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH/2, 300, arcade.color.WHITE, 50, anchor_x= "center",font_name = "fonts/KGHAPPY")
        arcade.draw_text("Click ENTER to START AGAIN", SCREEN_WIDTH/2, 200, arcade.color.WHITE, 30, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("You Scored:" + str(self.text), SCREEN_WIDTH/2, 100, arcade.color.WHITE, 30, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.WHITE, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.set_viewport(0, SCREEN_WIDTH -1, 0, SCREEN_HEIGHT -1)
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)
            lista.append(self.num)
            
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
            lista.append(self.num)

        sorted_lista = sorted(lista)
        sorted_lista.reverse()
        with open("textfiles/highestscores.txt", "r+") as highest_scores:
            data = highest_scores.read()
            highest_scores.write(", " + str(sorted_lista[0]))

        
         

class ScoresView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.TEAL)
    def on_draw(self):
        x = sorted(lista)
        x.reverse()
        arcade.start_render()
        arcade.draw_text("Best Scores", SCREEN_WIDTH/2, 300, arcade.color.BLACK, 50, anchor_x= "center",font_name = "fonts/KGHAPPY")
        with open("textfiles/highestscores.txt", "r+") as highest_scores:
            data = highest_scores.read()
            x = data.split(", ")
            a = list(map(int, x))
            a = list( dict.fromkeys(a))
            b = sorted(a)
            b.reverse()
        for c in range(1,6):
            arcade.draw_text("%s." %c, SCREEN_WIDTH/2 -75, 250 - (c-1)*50, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        if len(b) < 6:
            for i in range(len(b)):
                arcade.draw_text(str(b[i]), SCREEN_WIDTH/2 +75, 250 - i*50, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        else:
            for i in range(0,5):
                arcade.draw_text(str(b[i]), SCREEN_WIDTH/2 +75, 250 - i*50, arcade.color.BLACK, 20, anchor_x= "center",font_name = "fonts/CaviarDreams")
        
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.ASH_GREY, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)           
            
    

class WinView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.GOLD)
    def on_draw(self):
        with open("textfiles/yourscore.txt", "r") as yourscore:
            self.text = yourscore.read()
            self.num = int(self.text)
        arcade.start_render()
        arcade.draw_text("YOU WON!", SCREEN_WIDTH/2, 250, arcade.color.BLACK, 50, anchor_x= "center",font_name = "fonts/KGHAPPY")
        arcade.draw_text("Click ENTER to START AGAIN", SCREEN_WIDTH/2, 200, arcade.color.BLACK, 30, anchor_x= "center",font_name = "fonts/Happy Lucky Free")
        arcade.draw_text("Click Q to go back", SCREEN_WIDTH/8, 375, arcade.color.BLACK, 10, anchor_x= "center",font_name = "fonts/CaviarDreams")
        arcade.set_viewport(0, SCREEN_WIDTH -1, 0, SCREEN_HEIGHT -1)
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            menu_view = MenuView()
            self.window.show_view(menu_view)
            lista.append(self.num)
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
            lista.append(self.num)
        sorted_lista = sorted(lista)
        sorted_lista.reverse()
        with open("textfiles/highestscores.txt", "r+") as highest_scores:
            data = highest_scores.read()
            highest_scores.write(", " + str(sorted_lista[0]))


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
        self.background = arcade.load_texture("pictures/background.png")
        self.flappybird_list = arcade.SpriteList()
        self.pipedown_list =arcade.SpriteList()
        self.pipeup_list =arcade.SpriteList()
        with open("textfiles/characters.txt", "r+") as f:
            data = f.read()
            x = data.split(", ")
            x = [ x[i] if i % 2 == 0 else float(x[i]) for i in range(0, len(x))]
        self.flappybird_sprite = arcade.Sprite(x[0], x[1])
        self.flappybird_sprite.center_x = 64
        self.flappybird_sprite.center_y =200
        self.flappybird_list.append(self.flappybird_sprite)
        self.lives = 3
        self.score = 0
        
        up =[]
        for x in range(250, 50000,250):
            pipeup = Collisions("pictures/pipe.png", PIPE_SCALING)
            pipeup.center_x = x
            pipeup.center_y = random.randrange(-50, 100)
            self.pipeup_list.append(pipeup)
            up.append(pipeup.center_y)
            pipedown = Collisions("pictures/pipe2.png", PIPE_SCALING)
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
        self.pipeup_list.draw()
        self.pipedown_list.draw()
        arcade.draw_text("CLICK SPACE TO JUMP", 250 , SCREEN_HEIGHT/2 , arcade.csscolor.WHITE, 30,font_name = "fonts/CaviarDreams")
        for x in range(25,175,25):
            if self.score == x:
                arcade.draw_text("NEXT LEVEL", 250 + self.view_left, SCREEN_HEIGHT/2, arcade.csscolor.WHITE, 60,font_name = "fonts/CaviarDreams")
                arcade.play_sound(nextlevel_sound)
        self.flappybird_list.draw()
        arcade.draw_lrtb_rectangle_filled(0, 150 + self.view_left, 400 + self.view_bottom,340 , color = (0,153,204,255) )
        
        score_text = f"Score:{self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 370 + self.view_bottom, arcade.csscolor.WHITE, 20, font_name = "fonts/CaviarDreams")
        lives_text = f"Lives:{self.lives}"
        arcade.draw_text(lives_text, 10 + self.view_left, 340 + self.view_bottom, arcade.csscolor.WHITE, 20, font_name = "fonts/CaviarDreams")
        
        
            


    def on_update(self, delta_time):
        self.flappybird_list.update()
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.flappybird_sprite.top > top_boundary:
            gameover_view = GameOverView()
            self.window.show_view(gameover_view)
            arcade.play_sound(gameover_sound)
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.flappybird_sprite.bottom < bottom_boundary:
            gameover_view = GameOverView()
            self.window.show_view(gameover_view)
            arcade.play_sound(gameover_sound)
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
                pipeup.append_texture(arcade.load_texture("pictures/pipe.png"))
                arcade.play_sound(hurt_sound)
                pipeup.set_texture(1)
                pipeup.changed = True
                self.lives += -1

        for pipedown in downpipes:
            if not pipedown.changed:
                pipedown.append_texture(arcade.load_texture("pictures/pipe2.png"))
                arcade.play_sound(hurt_sound)
                pipedown.set_texture(1)
                pipedown.changed = True
                self.lives += -1
 
                                      
        if self.lives == 0:
            gameover_view = GameOverView()
            self.window.show_view(gameover_view)
            arcade.play_sound(gameover_sound)
        if self.score == 199:
            winning_view = WinView()
            self.window.show_view(winning_view)
            arcade.play_sound(winning_sound)

        points = list(range(250, 50000,250))
        for i in points:
            if self.score >-1 and self.score<25:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+5 :
                    self.score +=1
            elif self.score >24 and self.score<50:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+7 :
                    self.score +=1
            elif self.score >49 and self.score<75:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+10 :
                    self.score +=1
            elif self.score >74 and self.score<100:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+12 :
                    self.score +=1
            elif self.score >99 and self.score<125:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+15 :
                    self.score +=1
            elif self.score >124 and self.score<150:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+17 :
                    self.score +=1
            elif self.score >149 and self.score<175:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+20 :
                    self.score +=1
            elif self.score >174 and self.score<200:
                if self.flappybird_sprite.right > i and self.flappybird_sprite.right < i+25 :
                    self.score +=1
                
        with open("textfiles/yourscore.txt","w") as out:
            out.write(str(self.score))



    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.score >-1 and self.score <25:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 5
            elif self.score >24 and self.score <50:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 7
            elif self.score >49 and self.score <75:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 10
            elif self.score >74 and self.score<100:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 12
            elif self.score >99 and self.score <125:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 15
            elif self.score >124 and self.score <150:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 17
            elif self.score >149 and self.score <175:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 20
            else:
                self.flappybird_sprite.change_y = JUMP_SPEED
                arcade.play_sound(jump_sound)
                self.flappybird_sprite.change_x = 25
            
        
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
