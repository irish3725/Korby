
import os
import final_game as game

class ui:

    ## @param cal - calendar object that will be interated with
    def __init__(self, player):
        self.p = player 

    ## main ui loop
    def run(self):  
        # value to read input into 
        val = ''

        while val != 'q' and val != 'quit' and val != 'exit':
            output = self.p.location.getDirections() + '(w/a/s/d/f/r/q) > '
            val = input(output).lower()

            # adding an event
            if val == 'w' or val == 'a' or val == 's' or val == 'd' or val == 'f' or val == 'r':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\n' + self.p.action(val))
                val = ''

