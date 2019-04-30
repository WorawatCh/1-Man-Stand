import arcade.key

DIR_STILL = 0

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSET = {DIR_STILL: (0,0),
              DIR_UP: (0, 1),
              DIR_RIGHT: (1, 0),
              DIR_DOWN: (0, -1),
              DIR_LEFT: (-1, 0)}

STOP_MOVE = True
MAX_LANE = 600
MIN_LANE = 100


class Player:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.wait_time = 0

    def update(self, delta):
        # if self.y == MAX_LANE:
        #     self.y = 600
        # elif self.y == MIN_LANE:
        #     self.y = 100
        # else:
            self.move(delta)

      
    def move(self, delta):
          global STOP_MOVE
          
          if STOP_MOVE:
           self.direction = DIR_STILL
           STOP_MOVE = False
          else:
           self.x += DIR_OFFSET[self.direction][0] * 100
           self.y += DIR_OFFSET[self.direction][1] * 100
           STOP_MOVE = True

class Zombie:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0

    def update(self, delta):
        self.x = DIR_STILL
       


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, 80, 300)
        self.zombie = Zombie(self, 80, 300)

    def update(self, delta):
        self.player.update(delta)
        self.zombie.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.direction = DIR_UP
        elif key == arcade.key.DOWN:
            self.player.direction = DIR_DOWN
