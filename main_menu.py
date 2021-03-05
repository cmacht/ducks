## TODO: kann man verhindernd, dass ich in jeder unterdatei arcade separat importieren muss?
import arcade
from arcade.gui import UIManager
import Figurines

def draw_backgrund(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BOTTOM):
    SUN_RADIUS = SCREEN_WIDTH / 2 + 10

    # Draw the sun
    arcade.draw_circle_filled(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2 - SCREEN_WIDTH / 4,
        SUN_RADIUS,
        (246, 201, 37),
    )

    # Draw the ground
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH / 2,
        SCREEN_BOTTOM + SCREEN_HEIGHT / 8,
        SCREEN_WIDTH,
        SCREEN_HEIGHT / 3,
        (78, 34, 9),
    )

def add_main_menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BOTTOM, NAME_OF_THE_GAME):
    arcade.draw_text(
            NAME_OF_THE_GAME,
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 3,
            (0, 0, 0,),
            anchor_x="center",
            font_size=60,
            #width: int = 0,
            #align: str = "left",
            font_name=['calibri_bold', 'arial'],
            #anchor_x: str = "left",
            #anchor_y: str = "baseline",
            #rotation: float = 0
            )