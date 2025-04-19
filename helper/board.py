from helper.functions.emptyEntries import emptyEntries
from helper.functions.gameEnd import gameEnd
from helper.functions.winner import winner

class Board:

    def __init__(self):
        self.state=[[" "," "," "],[" "," "," "],[" "," "," "]]

    def emptyEntries(self) -> list[tuple]:
        return emptyEntries(self.state)
    
    def gameEnd(self) -> bool:
        return gameEnd(self.state)

    def winner(self) -> str | None:
        return winner(self.state)

    def printState(self) -> None:
        for row in range(3):
            for col in range(3):
                if col != 2:
                    print(self.state[row][col]+"|",end="")
                else:
                    print(self.state[row][col])
            # add horizontal line
            if row != 2:
                print("-----")
        
    def applyAction(self,action) -> None:
        try:
            if action["entry"] not in self.emptyEntries():
                raise ValueError("Error: This is not a valid action.")
            else:
                self.state[action["entry"][0]][action["entry"][1]] = action["mark"]
        except:
            print("Error: This is not a valid action.")
            raise Exception

    


