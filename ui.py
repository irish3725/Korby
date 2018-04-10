
import game

class ui:

    ## @param cal - calendar object that will be interated with
    def __init__(self, player):
        self.player = player 

    ## main ui loop
    def run(self):  
        # value to read input into 
        val = ''

        while val != 'q' and val != 'quit' and val != 'exit':
            val = input('(w/a/s/d/q) > ').lower()

            # adding an event
            if val == 'w' or val == 'a' or val == 's' or val == 'd':
                self.player.action(self.player, val)
                val = ''

