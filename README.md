# Something with ducks
A little journey to create something with ducks :duck: :duck:

### Steps
1. Install virtual environment `python3 -m venv .env`
1. Activate with `. .env/bin/activate`, deactivate with `deactivate`
1. With activated .env, install required modules `pip install -r requirements.txt`
1. Follow [RealPython Tutorial](https://realpython.com/arcade-python-game-framework/#basic-arcade-program) from here

### Resources
- [RealPython Tutorial](https://realpython.com/arcade-python-game-framework/)
- [Moorhuhn Sprites & Sounds](http://python4kids.net/downloads/py4k_cda4/py4kids-material/kap15_a4/Programme/)

### Learning Points
**Game Loop** \
Provided in `arcade.run()`.

**Event Handlers** \
Provides methods during game loop, can be overriden as needed. Examples:
* Keyboard Input: `.on_key_press()`, `.on_key_release()`
* Mouse Input: `.on_mouse_press()`, `.on_mouse_release()`, `.on_mouse_motion()`
* Updating Game Object: `.on_update()`
* Drawing: `.on_draw()`

**Sprites** \
2D images on sprite list:
* update all the sprites in the list with `SpriteList.update()`
* draw all the sprites in the list with`SpriteList.draw()`
  * `self.all_sprites.draw()`
* check if a single sprite has collided with any sprite in the list
