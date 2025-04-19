import random
import copy
from helper.functions.initializationQ import is_initialized,initialize
from helper.functions.updateQ import updateQ
from helper.board import Board
from helper.players import Computer, switchPlayers


def learn(episodes: int,learningRate: float ,discountFactor: float,QStatesActionsValues: list,epsilon: float) -> list:
    
    for i in range(episodes):
        
        if i%100==0:
            print("Iteration "+str(i))
        
        
        board = Board() 
        player1=Computer(mark="X")
        player2=Computer(mark="O")
        currPlayer=player1

        while not board.gameEnd():

            # Initialize Q if not done yet.
            for entry in board.emptyEntries():
                action={"entry":entry,"mark":currPlayer.mark}
                if not is_initialized(board.state,action,QStatesActionsValues):
                    QStatesActionsValues=initialize(copy.deepcopy(board.state),action,QStatesActionsValues)

            if random.uniform(0,1) < epsilon:
                # explore, i.e. pick a random valid action.
                action=currPlayer.choose_random_action(board)
            else:
                # exploit, i.e. pick an optimal action.
                action=currPlayer.choose_optimal_action(board,QStatesActionsValues)

            QStatesActionsValues = updateQ(copy.deepcopy(board.state),action,learningRate,discountFactor,QStatesActionsValues)
            board.applyAction(action)

            currPlayer=switchPlayers(currPlayer, player1, player2)

    return QStatesActionsValues
