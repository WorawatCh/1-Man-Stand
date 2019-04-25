import arcade.key

DIR_STILL = 0
DIR_UP = 1
DIR_DOWN = 3

DIR_OFFSET = {DIR_STILL: (0, 0),
              DIR_UP: (0, 1),
              DIR_DOWN: (0, -1)}

STOP_MOVE = True


class Player:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.wait_time = 0

    def update(self, delta):
       global STOP_MOVE

       if STOP_MOVE:
           self.direction = DIR_STILL
           STOP_MOVE = False
       else:
           self.x += DIR_OFFSET[self.direction][0] * 100
           self.y += DIR_OFFSET[self.direction][1] * 100
           STOP_MOVE = True

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, 80, 300)

    def update(self, delta):
        self.player.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.direction = DIR_UP
        elif key == arcade.key.DOWN:
            self.player.direction = DIR_DOWN
