import arcade.key, random

STOP_MOVE = True
MAX_LANE = 650
MIN_LANE = 0

BULLET_SPEED = 7
ZOMBIE_SPEED = [5,7,10,13,15]

BULLET_LIST = [5]
LANE_LIST = [100, 200, 300, 400, 500,600]

SCORE_LIST = []


class Player:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.bullet = Bullet(self.world, -100, -100)
        self.score = 0

    def update(self, delta):
        if self.y >= MAX_LANE:
            self.y -= 100
        elif self.y <= MIN_LANE:
            self.y += 100
        self.bullet.update(delta)

    def shoot(self):
        self.bullet.move(self)


class Zombie:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.hit = 0

    def update(self, delta):
       if self.x <= self.world.player.bullet.x and self.y == self.world.player.bullet.y:
           self.setPosition()
           self.world.player.bullet.isShoot = False
           self.world.player.bullet.setStart()
           self.world.player.score += 1
       self.world.checkGameEnd()
       self.x -= random.choice(ZOMBIE_SPEED)

    def setPosition(self):
        self.x = self.world.width
        self.y = random.choice(LANE_LIST)

class Bullet:
    DIR_HORIZONTAL = 0

    def __init__(self, world, x, y):
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
            self.setStart()
            
    def setStart(self):
        self.isShoot = False
        self.x = -100
        self.y = -100

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, 80, 300)
        self.zombie = Zombie(self, self.width, random.choice(LANE_LIST))
        self.gameEnd = False

    def update(self, delta):
        self.player.update(delta)
        self.zombie.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player.y += 100
        elif key == arcade.key.DOWN:
            self.player.y -= 100
        elif key == arcade.key.SPACE:
            if self.player.bullet.isShoot == False:
                 self.player.shoot()

    def checkGameEnd(self):
         if self.zombie.x <= 160:
            self.gameEnd = True
            self.player.score = 0
    
    def restart(self):
        self.player.x = 80
        self.player.y = 300
        self.zombie.x = self.width
        self.zombie.y = random.choice(LANE_LIST)
        self.player.bullet.setStart()
        self.gameEnd = False
