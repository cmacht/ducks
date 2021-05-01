# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150
SCALING = 2.0


# Classes
class Multiplayer(arcade.Window):
    """Two dots on screen
    Two Players on keyboard, each can move their dot
    Collisions detection (push other?)
    Touching border ends game (lose)
    """
    def __init__(self, width, height, title):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(width, height, title)
        self.paused = False

        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

        # Set up the player
        self.player = arcade.Sprite(":resources:images/alien/alienBlue_walk1.png", 0.5)
        self.player.center_y = self.height / 2
        self.player.left = 220
        self.all_sprites.append(self.player)

        self.player2 = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", 0.5)
        self.player2.center_y = self.height / 2
        self.player2.right = 50
        self.all_sprites.append(self.player2)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W:
            self.player.change_y = 5

        if symbol == arcade.key.S:
            self.player.change_y = -5

        if symbol == arcade.key.A:
            self.player.change_x = -5

        if symbol == arcade.key.D:
            self.player.change_x = 5

        if symbol == arcade.key.UP:
            self.player2.change_y = 5

        if symbol == arcade.key.DOWN:
            self.player2.change_y = -5

        if symbol == arcade.key.LEFT:
            self.player2.change_x = -5

        if symbol == arcade.key.RIGHT:
            self.player2.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0

        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_update(self, delta_time):
        if self.paused:
            return

        self.all_sprites.update()

        # Keep the player on the screen
        if self.player.top > self.height:
            self.player.top = self.height

        if self.player.right > self.width:
            self.player.right = self.width

        if self.player.bottom < 0:
            self.player.bottom = 0

        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()
        self.all_sprites.draw()


# main code entry point
if __name__ == "__main__":
    app = Multiplayer(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
    app.setup()
    arcade.run()
