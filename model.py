import arcade.key

class Player:
    def __init__(self,world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        if self.y > self.world.height:
            self.y = 100
        
    def switch_direction(self):
        if self.direction == Ship.DIR_HORIZONTAL:
            self.direction = Ship.DIR_VERTICAL
        else:
            self.direction = Ship.DIR_HORIZONTAL

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self,80, 300)

    def update(self, delta):
        self.player.update(delta)
    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.ship.switch_direction()
        else if key == arcade.key.DOWN:
            self.ship.switch_direction()
        
