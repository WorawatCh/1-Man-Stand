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

BULLET_SPEED = 5
ZOMBIE_SPEED = 3

BULLET_LIST = [5]

class Player:
    
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.laser_x = 80
        self.laser_y = 270
        for x in BULLET_LIST:
             x = Bullet(self.world, -100, -100)

    def update(self, delta):
        if self.y >= MAX_LANE:
            self.y -=100
        elif self.y <= MIN_LANE:
            self.y += 100
        self.bullet1.update(delta)
    
    def shoot(self):
        self.bullet1.move(self)


class Zombie:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0

    def update(self, delta):
       if self.x == 180:
           self.x = self.world.width
       self.x -= ZOMBIE_SPEED
       
       
class Bullet:
    DIR_HORIZONTAL = 0

    def __init__(self,world, x, y):
        self.x = x
        self.y = y
        self.world = world
        self.direction = Bullet.DIR_HORIZONTAL
        self.isShoot = False

    def move(self, player):
        self.x = player.x
        self.y = player.y
        self.isShoot = True

    def update(self, delta):
        if self.isShoot == True:
            self.x += BULLET_SPEED
        if self.x > self.world.width:
            self.isShoot = False
            self.x = -100
            self.y = -100
       

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, 80, 300)
        self.zombie = Zombie(self, self.width, 300)

    def update(self, delta):
        self.player.update(delta)
        self.zombie.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.y += 100
        elif key == arcade.key.DOWN:
            self.player.y -= 100
        elif key == arcade.key.SPACE:
            self.player.shoot()
