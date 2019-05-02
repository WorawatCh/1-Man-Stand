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
MAX_LANE = 650
MIN_LANE = 0


class Player:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL
        self.wait_time = 0

    def update(self, delta):
        if self.y >= MAX_LANE:
            self.y -=100
        elif self.y <= MIN_LANE:
            self.y += 100

class Zombie:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0

    def update(self, delta):
       if self.x == 180:
           self.x = self.world.width
       self.x -= 10
       
class Bullet:
    BULLET_SPEED = 5
    DIR_HORIZONTAL = 0

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Bullet.DIR_HORIZONTAL

    def update(self, delta):
        if self.x > self.world.width:
                self.x = 200
        self.x += 5
            
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, 80, 300)
        self.zombie = Zombie(self, self.width, 300)
        self.bullet = Bullet(self, 80,270)

    def update(self, delta):
        self.player.update(delta)
        self.zombie.update(delta)
        self.bullet.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.direction = DIR_UP
            self.player.y += 100
            self.bullet.y += 100
        elif key == arcade.key.DOWN:
            self.player.direction = DIR_DOWN
            self.player.y -= 100
            self.bullet.y -= 100
        elif key == arcade.key.SPACE:
            self.bullet.update()



