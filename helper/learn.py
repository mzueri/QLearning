import random
import copy
from helper.functions.gameEnd import gameEnd
from helper.functions.initializationQ import is_initialized,initialize
from helper.functions.emptyEntries import emptyEntries
from helper.functions.getNextState import getNextState
from helper.functions.getQValue import getQValue
from helper.functions.updateQ import updateQ
from helper.functions.otherPlayer import otherPlayer
from helper.functions.actions import optimalAction, randomAction
from helper.board import Board


def learn(iterations,learningRate,discountFactor,QStatesActionsValues):
    
    epsilon = 0.4 

    for i in range(iterations):
        
        if i%100==0:
            print("Iteration "+str(i))
        
        currPlayer="X"
        board = Board() 

        while not gameEnd(copy.deepcopy(board.state)):

            # Initialize Q if not done yet.
            for entry in emptyEntries(copy.deepcopy(board.state)):
                action={"entry":entry,"player":currPlayer}
                if not is_initialized(copy.deepcopy(board.state),action,QStatesActionsValues):
                    QStatesActionsValues=initialize(copy.deepcopy(board.state),action,QStatesActionsValues)

            if random.uniform(0,1) < epsilon:
                # explore, i.e. pick a random valid action.
                action = randomAction(copy.deepcopy(board.state),currPlayer)
                #print("random action chosen: "+str(action))
            else:
                # exploit, i.e. pick an optimal action.
                action = optimalAction(copy.deepcopy(board.state),currPlayer,QStatesActionsValues)
                #print("optimal action chosen: "+str(action))

            QStatesActionsValues = updateQ(copy.deepcopy(board.state),action,learningRate,discountFactor,QStatesActionsValues)
            board.applyAction(action)
            #board.printState()

            currPlayer=otherPlayer(currPlayer)

    return QStatesActionsValues
