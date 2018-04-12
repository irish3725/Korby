import threading
import random

# my imports
import ui

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
            # give random monster a key if there needs to be a key
            monster = int(random.uniform(0,e_number))
            print('monster', monster, 'has the key')
            
            enemies[monster].key = e_key

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
            self.location.setPath('south', node(2, 'hard_fight', n_enemies=3))
            self.location.south.setPath('west', node(3, 'chest'))
            self.location.south.setPath('east', node(4, 'hard_fight', key=True))
            self.location.south.setPath('south', node(5, 'recharge'))

    def setLocation(self, location):
        self.location = location

    def action(self, action, message=True):

        if self.state == 'dead':
            return 'You can\'t do anything. You\'re dead.'
        elif self.state == 'won':
            return 'Where are you going? You already won.'

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

        if self.location.n_type == 'hard_fight' or self.location.n_type == 'easy_fight':
            m += self.fight()
        elif self.location.n_type == 'recharge':
            m += self.recharge()
        elif self.location.n_type == 'chest':
            m += self.chest()

        # get rid of newline at end
        m = m[0:len(m)-1]

        return m

    ## method to be called when player wants
    ## to attack
    ## this method handles dealing damage to
    ## enemy, then check to see if enemy is dead,
    ## if so take key if enemy has it, then
    ## if enemy is not dead, take damage from
    ## enemy(s) and check to see if player is dead
    def attack(self):
        m = ''

        # get index of random monster to attack
        monster = int(random.uniform(0, len(self.location.enemies)))

        # hit monster
        self.location.enemies[monster].hit()

        # print health of all monsters
        for enemy in self.location.enemies:
            m += enemy.getName() + ': ' + str(enemy.getHealth()) + '\n'

        # check to see if monster that player hit is deadj
        if self.location.enemies[monster].getHealth() < 1:
            # append enemy died message
            m += 'enemy died\n'

            # if the monster has a key, take it
            if self.location.enemies[monster].getKey():
                self.key = True
                m += 'got key!!!\n'

            # remove dead enemy from room
            self.location.enemies.remove(self.location.enemies[monster])

            # if room is now empty make it an empty room
            if len(self.location.enemies) < 1:
                self.location.n_type = 'empty'
                self.state = None

        # if there are still monsters in the room
        if self.location.enemies:

            # take damage from each monster
            for enemy in self.location.enemies:
                self.health -= enemy.attack()

            # if player is dead
            if self.health < 1:
                # append death message
                m += 'Oh dear, you are dead!\n'
                # set health to 0 just in case negative
                self.health = 0
                # set state to dead
                self.state = 'dead'
                # set room type to empty
                self.location.n_type = 'empty'


        m += 'Player Health: ' + str(self.health) + '\n'

        return m

    ## method to call when player wants to
    ## run from a fight
    ## sends player to random adjacent room
    def run(self):
        m = 'running\n'
        # set state to default None
        self.state = None
        # hold current room
        current_room = self.location
        # iterate until a room is found
        while self.location == current_room:
            # choose a direction
            direction = int(random.uniform(0,4))
            # move that direction
            if direction == 0:
                self.action('w', False)
            elif direction == 1:
                self.action('a', False)
            elif direction == 2:
                self.action('s', False)
            elif direction == 3:
                self.action('d', False)

        # return message to player
        return m

    ## method to call when a fight room is
    ## reached
    def fight(self):
        m = ''
        # set state to fighting
        self.state = 'fight'
        # print out all enemies
        for enemy in self.location.enemies:
            m += 'There is a ' + enemy.getName() + ' in this room\n'
        # ask player if they want to fight or run away
        m += 'Would you like to fight or run away?\n'
        
        # return message to player
        return m

    ## method to call when a recharge room is
    ## reached
    def recharge(self):
        # tell player recharging
        m = 'recharging health\n'
        # set health to full
        self.health = 100
        
        return m

    ## method to call when a chest room is
    ## reached
    def chest(self):
        m = ''
        # if the player has the key
        if self.key:
            # change player state to won
            self.state = 'won'
            # return win message
            m += 'You won!!\n'
        # otherwise tell player they need a key
        else:
            m += 'You need to find the key.\n'

        return m 

if __name__ == '__main__':
    # create new player
    p = player(level=1)
    # create ui
    ui = ui.ui(p)
    # run ui
    ui.run() 

