from helper.board import Board
from helper.functions.initializationQ import npFindIndex
import copy
from helper.functions.gameEnd import gameEnd
from helper.functions.emptyEntries import emptyEntries
from helper.functions.initializationQ import is_initialized, initialize
from helper.functions.actions import optimalAction
from helper.functions.winner import winner

def play(QStatesActionsValues,playerStarting):

    assert playerStarting in ["human","computer"], "Invalid value for object 'playerStarting'. "

    board=Board()
    currPlayer=playerStarting
    if playerStarting=="human":
        humanMark="X"
        computerMark="O"
    else:
        humanMark="O"
        computerMark="X"

    while not(gameEnd(copy.deepcopy(board.state))):
        
        if currPlayer=="computer":
            # computer makes move.
            for entry in emptyEntries(copy.deepcopy(board.state)):
                action={"entry":entry,"player":computerMark}
                if not is_initialized(copy.deepcopy(board.state),action,QStatesActionsValues):
                    print("Need to initialize")
                    print(entry)
                    QStatesActionsValues=initialize(copy.deepcopy(board.state),action,QStatesActionsValues)
        
            action = optimalAction(copy.deepcopy(board.state),computerMark,QStatesActionsValues)
            board.applyAction(action)
            print("Computer makes the following move: ")
            board.printState()

        else:
            # human shall make a move. 
            humanMove = input("What is your next move? ")
            try:
                humanMove=eval(humanMove)
            except: 
                raise ValueError("Cannot evaluate input. Provide a tuple as input. ")
            assert isinstance(humanMove, tuple), "The input is not a tuple."
            assert len(humanMove)==2, "The tuple does consist of two elements."
            assert humanMove[0] in range(3) and humanMove[1] in range(3), "Row and column indices out of bounce. "
            action = {"entry":humanMove,"player":humanMark}
            board.applyAction(action)
            board.printState()
        
        if currPlayer=="computer":
            currPlayer="human"
        elif currPlayer=="human":
            currPlayer="computer"

    if winner(copy.deepcopy(board.state))==humanMark:
        print("You win!")
    elif winner(copy.deepcopy(board.state))==computerMark:
        print("Computer wins!")
    else: 


        print("Nobody wins!")


    
