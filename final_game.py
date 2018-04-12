import threading
import random

# my imports
import ui
from player import *

class enemy:
    def __init__(self, name='Waddle Dee', max_hit=65, health=100, key=False):
        # list of minions
        minions = ['Blipper', 'Cappy', 'Scarfy', 'Waddle Dee', 'Waddle Doo']

        self.name = name
        self.health = health
        self.max_hit = max_hit
        self.key = key

        if name in minions and health == 100:
            self.health = 40 
        if name in minions and max_hit == 65:
            self.max_hit = 20 

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getKey(self):
        return self.key

    def attack(self):
        # return random value between 1 and max hit with average of 3/4
        return int(random.triangular(1, self.max_hit, (self.max_hit/4)*3 ))

    def hit(self):
        self.health -= int(random.triangular(1,75, 70))
        if self.health < 0:
            self.health = 0

class node:
    def __init__(self, name=1, n_type='empty', n_enemies=1, key=False):
        self.n_type = n_type

        if n_type == 'hard_fight':
            self.enemies = self.getEnemies(difficulty='hard', e_key=key, e_number=n_enemies)
        if n_type == 'easy_fight':
            self.enemies = self.getEnemies(difficulty='easy', e_key=key, e_number=n_enemies)

        self.name = name
        self.north = None
        self.east = None 
        self.south = None
        self.west = None

    def getEnemies(self, difficulty='hard', e_number=1, e_key=False):
        minions = ['Blipper', 'Cappy', 'Scarfy', 'Waddle Dee', 'Waddle Doo']
        possible_enemies = ['Sword Knight', 'Gordo', 'Hot Head', 'Laser Ball', 'Wheelie', 'Broom Hatter', 'UFO', 'Chilly']

        # roll for room with multiple easy or one hard
        if difficulty == 'hard':
            e_number = int(random.uniform(0,2))
            e_number = (e_number * 3) + 1


        enemies = []

        # if difficulty is easy, put one easy monster in room
        if difficulty == 'easy':
            enemy_name = minions[int(random.uniform(0, len(minions)))]
            enemies.append(enemy(enemy_name, key=e_key))
        elif e_number == 1:
            enemy_name = possible_enemies[int(random.uniform(0, len(possible_enemies)))]
            enemies.append(enemy(enemy_name, key=e_key))
        else:
            for i in range(e_number):
                enemy_name = minions[int(random.uniform(0, len(minions)))]
                enemies.append(enemy(enemy_name))

        return enemies

    def setPath(self, direction, n):
        
        direction = direction.lower()
        if direction == 'north':
            # set north path
            self.north = n
            # set south path on north node
            self.north.south = self
        elif direction == 'east':
            # set east path
            self.east = n
            # set west path on east node
            self.east.west = self
        elif direction == 'south':
            # set south path
            self.south = n
            # set north path on south node
            self.south.north = self
        elif direction == 'west':
            # set north path
            self.west = n
            # set east path on west node
            self.west.east = self

    def getDirections(self):
        m = 'I see a path to the '
        directions = []
        if self.north != None:
            directions.append('north')
        if self.east != None:
            directions.append('east')
        if self.south != None:
            directions.append('south')
        if self.west != None:
            directions.append('west')

        m += directions[0]

        for i in range(1,len(directions) - 1):
            m += ', ' + directions[i]

        if len(directions) > 1:
            m += ', and ' + directions[len(directions) - 1]

        return m + '.\n'
            
if __name__ == '__main__':
    # create new player
    p = player(level=1)
    # create ui
    ui = ui.ui(p)
    # run ui
    ui.run() 

