from helper.board import Board
from helper.functions.getOptimalAction import getOptimalAction
import random


class Player:

    def __init__(self,mark: str) -> None:
        assert mark in ["X","O"], "Invalid mark assignment to player."
        self.mark=mark
    
    def apply_action(self, board: Board, action) -> None:
        try:
            if action["entry"] not in board.emptyEntries():
                raise ValueError("Error: This is not a valid action.")
            else:
                board.state[action["entry"][0]][action["entry"][1]] = self.mark
        except:
            print("Error: This is not a valid action.")
            raise Exception
        

class Human(Player):

    def __init__(self, mark):
        super().__init__(mark)

    def choose_action(self, board: Board):
        
        while True:
            try:
                # human shall make a move. 
                humanMove = input("What is your next move? ")
                humanMove=eval(humanMove)
                assert isinstance(humanMove, tuple), "The input is not a tuple"
                assert len(humanMove)==2, "The tuple must consist of two elements"
                assert humanMove[0] in range(3) and humanMove[1] in range(3), "Row or column indices not valid. Choose in range 0-2"
                assert humanMove in board.emptyEntries(), "This is not a valid move anymore. Choose an empty field"
                
                break # input is valid
            except Exception as e:
                print(f"Input error: {e}. Please provide a valid tuple as input. Try again.")
        
        return {"entry":humanMove,"mark":self.mark}
    
    def is_human(self):
        return True


class Computer(Player):

    def __init__(self, mark):
        super().__init__(mark)

    def choose_optimal_action(self, board: Board, QStatesActionsValues) -> dict | None:
        return getOptimalAction(board.state,self.mark,QStatesActionsValues)

    def choose_random_action(self, board: Board) -> dict:
        return {"entry":random.sample(board.emptyEntries(),1)[0],"mark":self.mark}
    
    def is_human(self):
        return False
    

def switchPlayers(currPlayer, player1, player2):
    assert currPlayer==player1 or currPlayer==player2, "Current player is someone else."

    if currPlayer==player1:
        return player2
    else:
        return player1