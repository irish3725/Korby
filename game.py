import threading
import ui

class node:
    def __init__(self, name=1, n_type='empyt'):
        self.n_type = 'empty'
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def setPath(self, direction, n):
        direction = direction.lower()
        if direction == 'north':
            self.north = n
        elif direction == 'east':
            self.east = n
        elif direction == 'south':
            self.south = n
        elif direction == 'west':
            self.west = n

class player:
    def __init__(self):
        self.location = None
        self.health = 100

    def action(self, action):
        if action == 'w':
            self.location = self.location.north
        elif action == 'a':
            self.location = self.location.west
        elif action == 's':
            self.location = self.location.south
        elif action == 'd':
            self.location = self.location.east
        print('i am now at location', self.location.name, 'which is a', self.location.type, 'room.')

if __name__ == '__main__':
    p = player()
    home = node()
    ui = ui.ui(player)

    home.setPath('south', node(2, 'fight'))
    home.south.setPath('west', node(3, 'chest'))
    home.south.setPath('east', node(4, 'fight'))
    home.south.setPath('south', node(5, 'recharge'))

    ui = threading.Thread(name='ui', target=ui.run)

    ui.start()
    ui.join()
