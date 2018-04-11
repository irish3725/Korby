import threading
import random

# my imports
import ui

class enemy:
    def __init__(self, name='Waddle Dee', health=100, key=False):
        self.name = name
        self.health = health
        self.key = key

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getKey(self):
        return self.key

    def attack(self):
        return int(random.triangular(1, 65, 60))

    def hit(self):
        self.health -= int(random.triangular(1,75, 70))
        if self.health < 0:
            self.health = 0

class node:
    def __init__(self, name=1, n_type='empty', key=False):
        self.n_type = n_type
        if n_type == 'fight':
            self.enemies = self.getEnemies(e_key=key)

        self.name = name
        self.north = None
        self.east = None 
        self.south = None
        self.west = None

    def getEnemies(self, e_type='normal', e_number=1, e_key=False):
        minions = ['Waddle Dee', 'Waddle Doo']
        possible_enemies = ['Sword Knight', 'Gordo', 'Hot Head', 'Laser Ball', 'Wheelie', 'Broom Hatter', 'UFO', 'Chilly']

        enemies = []

        if e_type == 'normal':
            enemy_name = possible_enemies[int(random.uniform(0, len(possible_enemies)))]
            enemies.append(enemy(enemy_name, key=e_key))
        else:
            for i in range(e_number):
                enemy_name = minions[int(random.uniform(0, len(minions)))]
                enemies.append(enemy(enemy_name, key=e_key))

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
            
            

class player:
    def __init__(self, level=1): 
        self.location = None
        self.health = 100
        self.state = None
        self.key = False
        self.createLevel(level)

    def createLevel(self, level):
        if level == 1:
            home = node()
            self.setLocation(home)
            self.location.setPath('south', node(2, 'fight'))
            self.location.south.setPath('west', node(3, 'chest'))
            self.location.south.setPath('east', node(4, 'fight', True))
            self.location.south.setPath('south', node(5, 'recharge'))

    def setLocation(self, location):
        self.location = location

    def action(self, action, message=True):

        if self.state == 'dead':
            return 'You can\'t do anything. You\'re dead'
        elif self.state == 'won':
            return 'Where are you going? You alread won.'

        m = ''

        if action == 'w' and self.location.north != None and self.state == None:
            self.location = self.location.north
        elif action == 'a' and self.location.west != None and self.state == None:
            self.location = self.location.west
        elif action == 's' and self.location.south != None and self.state == None:
            self.location = self.location.south
        elif action == 'd' and self.location.east != None and self.state == None:
            self.location = self.location.east
        elif action == 'f' and self.state == 'fight':
            m += self.attack()
        elif action == 'r' and self.state == 'fight' and self.health < 50:
            m += self.run()
        else:
            if message:
                m += 'can\'t go that way\n'
            return m

        if message:
            m += 'I am now at location ' + str(self.location.name) + ' which is a ' + self.location.n_type + ' room.\n'

        if self.location.n_type == 'fight':
            m += self.fight()
        elif self.location.n_type == 'recharge':
            m += self.recharge()
        elif self.location.n_type == 'chest':
            m += self.chest()

        # get rid of newline at end
        m = m[0:len(m)-1]

        return m

    def attack(self):
        m = ''

        monster = int(random.uniform(0, len(self.location.enemies)))

        # hit moster
        self.location.enemies[monster].hit()
        m += self.location.enemies[monster].getName() + ': ' + str(self.location.enemies[monster].getHealth()) + '\n'

        if self.location.enemies[monster].getHealth() < 1:
            m += 'enemy died\n'
            self.key = self.location.enemies[monster].getKey()
            if self.key:
                m += 'got key!!!\n'
            self.location.n_type = 'empty'
            self.state = None
        else:
            # take damage from monster
            self.health -= self.location.enemies[monster].attack()
            if self.health < 1:
                m += 'Oh dear. You are dead.\n'
                self.health = 0
                self.state = 'dead'
                self.location.n_type = 'empty'


        m += 'player health:' + str(self.health) + '\n'

        return m

    def run(self):
        m = 'running\n'
        self.state = None
        current_room = self.location
        while self.location == current_room:
            direction = int(random.uniform(0,4))
            if direction == 0:
                self.action('w', False)
            elif direction == 1:
                self.action('a', False)
            elif direction == 2:
                self.action('s', False)
            elif direction == 3:
                self.action('d', False)

        return m

    def fight(self):
        m = ''
        self.state = 'fight'
        for enemy in self.location.enemies:
            m += 'There is a ' + enemy.getName() + ' in this room\n'
        m += 'Would you like to attack or run away?\n'
        
        return m

    def recharge(self):
        m = 'recharging health\n'
        self.health = 100
        
        return m

    def chest(self):
        m = ''
        if self.key:
            self.state = 'won'
            m += 'you won!!\n'
        else:
            m += 'you need to find the key\n'

        return m 

if __name__ == '__main__':
    p = player(level=1)

    ui = ui.ui(p)


    ui.run() 

