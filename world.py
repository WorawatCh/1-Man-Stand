import arcade

from model import Player, World, Bullet, GAMEEND, SCORE_LIST

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
ZOMBIE_SPRIT_LIST = []

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.bullet_list = None
        self.score = 0

        self.background = arcade.load_texture('images/background.png')
        self.world = World(width, height)
        self.player_sprite = ModelSprite(
            'images/soilder.png', model=self.world.player)
        self.zombie_sprite = ModelSprite(
            'images/zombie.png', model=self.world.zombie)
        self.zombie_sprite1 = ModelSprite(
            'images/zombie.png', model=self.world.zombie)
        self.zombie_sprite2 = ModelSprite(
            'images/zombie.png', model=self.world.zombie)
        self.laser_sprite = ModelSprite(
            'images/laser1.png', model=self.world.player.bullet) 

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.score = self.world.countScore
        output = f"Score: {self.score}"
        arcade.draw_text(output, 800, 650, arcade.color.WHITE, 14)
        self.player_sprite.draw()
        self.zombie_sprite.draw()
        self.laser_sprite.draw()
    
    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        arcade.set_background_color(arcade.color.BABY_BLUE)
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def update(self, delta):
        if GAMEEND == True:
            self.draw_game_over()
            exit()
        self.world.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
