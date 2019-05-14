import arcade

from model import Player, World, Bullet

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
INSTRUCTION_PAGE = 0
GAME_RUNNING = 1
GAME_END = 2

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

        self.current_state = INSTRUCTION_PAGE
        self.score = 0

        self.background = arcade.load_texture('images/background.png')
        self.world = World(width, height)
        self.player_sprite = ModelSprite(
            'images/soilder.png', model=self.world.player)
        self.zombie_sprite = ModelSprite(
            'images/zombie.png', model=self.world.zombie)
        self.laser_sprite = ModelSprite(
            'images/laser1.png', model=self.world.player.bullet) 

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
        if key == arcade.key.P and self.current_state == INSTRUCTION_PAGE:
            self.current_state = GAME_RUNNING
            self.world.setStart()
        elif key == arcade.key.R and self.current_state == GAME_END:
            self.current_state = GAME_RUNNING
            self.world.setStart()
        elif key == arcade.key.Q and self.current_state == GAME_END:
             exit()

    def update(self, delta):
        if self.current_state == GAME_RUNNING:
            self.score = self.world.player.score
            self.world.update(delta)
        if self.world.gameEnd == True:
            self.current_state = GAME_END

    def draw_instruction_page(self):
        arcade.set_background_color(arcade.color.BABY_BLUE)
        output = "1 MAN STAND"
        arcade.draw_text(output, 130, 400, arcade.color.WHITE, 70)
        output = "Press P To Play"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 30)

    def draw_game(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.set_background_color(arcade.color.BABY_PINK)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 730, 630, arcade.color.WHITE, 30)
        self.player_sprite.draw()
        self.zombie_sprite.draw()
        self.zombie_sprite.draw()
        self.laser_sprite.draw()

    def draw_game_over(self):
        arcade.set_background_color(arcade.color.GO_GREEN)
        output = "GAME OVER"
        arcade.draw_text(output, 165, 400, arcade.color.WHITE, 70)
        output = f"Your score is {self.score}"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 30)
        output = "Press R to restart"
        arcade.draw_text(output, 205, 200, arcade.color.WHITE, 20)
        output = "Press Q to quit"
        arcade.draw_text(output, 515, 200, arcade.color.WHITE, 20)

    def on_draw(self):
        arcade.start_render()
        if self.current_state == INSTRUCTION_PAGE:
            self.draw_instruction_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == GAME_END:
            self.draw_game_over()

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
