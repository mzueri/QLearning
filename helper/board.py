import numpy as np
from helper.functions.emptyEntries import emptyEntries

class Board:

    def __init__(self):
        self.state=np.array([[" "," "," "],[" "," "," "],[" "," "," "]])

    def printState(self):
        for row in range(3):
            for col in range(3):
                if col != 2:
                    print(self.state[row][col]+"|",end="")
                else:
                    print(self.state[row][col])
            # add horizontal line
            if row != 2:
                print("-----")
    
    def applyAction(self,action):
        try:
            if action["entry"] not in emptyEntries(self.state):
                raise ValueError("Error: This is not a valid action.")
            else:
                self.state[action["entry"]] = action["player"]
        except:
            print("Error: This is not a valid action.")
            raise

