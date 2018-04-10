
import game

class ui:

    ## @param cal - calendar object that will be interated with
    def __init__(self, player):
        self.p = player 

    ## main ui loop
    def run(self):  
        # value to read input into 
        val = ''

        while val != 'q' and val != 'quit' and val != 'exit':
            val = input('(w/a/s/d/f/r/q) > ').lower()

            # adding an event
            if val == 'w' or val == 'a' or val == 's' or val == 'd' or val == 'f' or val == 'r':
                print(self.p.action(val))
                val = ''

