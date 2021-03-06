import arcade
import main_menu
import Figurines


class Game(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """



    def __init__(self, width, height, game_title):
        super().__init__(width, height, game_title)

        arcade.set_background_color(arcade.color.SKY_BLUE)


        # If you have sprite lists, you should create them here,
        # and set them to None
        self.player_list = None
        self.sprite_list = None

    def setup(self):
        self.SCREEN_WIDTH = self.width
        self.SCREEN_HEIGHT = self.height
        self.SCREEN_BOTTOM = 0
        self.NAME_OF_THE_GAME = "The Drake's Pursuit"

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Create your sprites and sprite lists here
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enten_list = arcade.SpriteList(use_spatial_hash=True)


        # Score

        # Set up the player
        self.player_sprite = arcade.Sprite("sprites/Absehen.png", 0.3)
        self.player_list.append(self.player_sprite)


        # Set up the Duck
        self.enten_sprite = arcade.Sprite("sprites/Ente1/Enteganzoben.png", 0.3)
        self.enten_sprite.center_x = 64
        self.enten_sprite.center_y = 120
        self.enten_list.append(self.enten_sprite)

        #load sounds
        self.mossberg = arcade.load_sound("sounds/Mossberg500.ogg")
        self.walther = arcade.load_sound("sounds/Mein_Gott_Watlher.ogg")
        self.mossberg_happy = arcade.load_sound("sounds/Mossberg500-happy.ogg")
        self.Teckel = arcade.load_sound("sounds/Teckel.ogg")
        self.nachladen = arcade.load_sound("sounds/Mein_Gott_Watlher.ogg")


    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        main_menu.draw_backgrund(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_BOTTOM)
        main_menu.add_main_menu(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_BOTTOM, self.NAME_OF_THE_GAME)
        self.enten_list.draw()
        self.player_list.draw()



    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.enten_sprite.center_x = self.enten_sprite.center_x + 2
        self.enten_sprite.center_y = self.enten_sprite.center_y + 2

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.H:
            arcade.play_sound(self.Teckel)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.mossberg_happy)
            position_letzter_linksklick = [x, y]
            print("Letzter Linksklick: ", position_letzter_linksklick)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Nachladen")
            arcade.play_sound(self.nachladen)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game_title = "The Drake's Pursuit"  # Denkbare Alternative: Hunt for Cocks
    game = Game(1280, 960, game_title)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()