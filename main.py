# Imports
import arcade
import arcade.gui
import main_menu


def main():
    # Constants
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 960
    SCREEN_BOTTOM = 0
    SCREEN_TITLE = "The Drake's Pursuit" #Denkbare Alternative: Hunt for Cocks
    NAME_OF_THE_GAME = "The Drake's Pursuit"

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Set the background color
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Clear the screen and start drawing the main screen
    arcade.start_render()
    main_menu.draw_backgrund(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BOTTOM)
    main_menu.add_main_menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BOTTOM, NAME_OF_THE_GAME)

    # Finish drawing
    arcade.finish_render()

    # Display everything
    arcade.run()

main()