import threading
import random

# my imports
import ui
import final_game
#from final_game import *

class player:

    def __init__(self, level=1): 
        self.health = 100
        self.state = None
        self.key = False
        self.location = self.createLevel(level)
        print(self.location.getDirections())

    def createLevel(self, level):
        V = []
        E = []
        S = []

        # create level 1
        if level == 1:
            V = ['empty', 'hard_fight', 'chest', 'hard_fight', 'recharge']
            E = [[1, 2, 'north'], [2, 3, 'east'], [2, 4, 'west'], [2, 5, 'north']]
            S = [1]
            return self.buildGraph(V, E, S)
        if level == 2:
            return self.buildGraph(V, E, S)

    def buildGraph(self, V, E, S, key=False):
        
        ## choose new start node ##
        # get index of randomly chosen start node
        S = S[int(random.uniform(0, len(S)))] - 1
        # get index of current empty room
        i = V.index('empty')
        # get value of room we will set to empty
        val = V[S]
        # set new start room to empty
        V[S] = 'empty'
        # replace the old empty room with replaced value
        V[i] = val

        ## set all vertexes as correct node
        i = 0
        temp = []
        # turn each vertex into a node
        for v in V:
            # increment i
            i += 1
            # append node
            temp.append(final_game.node(i, v))
        # replace V with  list of nodes
        V = temp

        ## give one room a key
        # variable to decide who holds the key
        key = False
        # while key has not been assigned
        while not key:
            # choose random room
            i = int(random.uniform(0, len(V)))
            # if this is a hard fight room, give key to monster
            if V[i].n_type == 'hard_fight':
                # select random enemy from room
                e = int(random.uniform(0, len(V[i].enemies)))
                # give enemy key
                V[i].enemies[e].key = True
                print('gave', e, 'a key.')
                # set key to true
                key = True

        ## connect edges
        for e in E:
            # get each node in V
            v1 = e[0] - 1
            v1 = V[v1]
            v2 = e[1] - 1
            v2 = V[v2]
            direction = e[2]

            # if v1 is to the north
            if direction == 'north':
                v1.south = v2
                v2.north = v1
            # if v1 is to the east
            elif direction == 'east':
                v1.west = v2
                v2.east = v1
            # if v1 is to the south
            elif direction == 'south':
                v1.north = v2
                v2.south = v1
            # if v1 is to the west
            elif direction == 'west':
                v1.east = v2
                v2.west = v1

        ## return start node
        return V[S]
             

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
            return m + self.location.getDirections()

        if message:
            m += 'I am now at location ' + str(self.location.name) + ' which is a ' + self.location.n_type + ' room.\n'

        if self.location.n_type == 'hard_fight' or self.location.n_type == 'easy_fight':
            m += self.fight()
        elif self.location.n_type == 'recharge':
            m += self.recharge()
        elif self.location.n_type == 'chest':
            m += self.chest()

        # get rid of newline at end
#        m = m[0:len(m)-1]

        return m + self.location.getDirections()

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

