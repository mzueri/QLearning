from helper.functions.emptyEntries import emptyEntries

class Board:

    def __init__(self):
        self.state=[[" "," "," "],[" "," "," "],[" "," "," "]]

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
                self.state[action["entry"][0]][action["entry"][1]] = action["player"]
        except:
            print("Error: This is not a valid action.")
            raise

