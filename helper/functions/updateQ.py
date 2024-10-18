from helper.functions.gameEnd import gameEnd
from helper.functions.reward import reward
from helper.functions.initializationQ import npFindIndex
from helper.functions.getQValue import getQValue
from helper.functions.getNextState import getNextState
from helper.functions.emptyEntries import emptyEntries
from helper.functions.otherPlayer import otherPlayer
from helper.functions.winner import winner
from helper.functions.actions import optimalAction

def updateQ(state,action,learningRate,discountFactor,QStatesActionsValues):  
    assert not gameEnd(state), "Game is already finished."
    indexStateAction=npFindIndex(state,action,QStatesActionsValues)
    
    currPlayer=action["player"]
    nextState=getNextState(state,action)
    nextPlayer=otherPlayer(currPlayer)

    if gameEnd(nextState):
        assert not gameEnd(state), "Game is already finished."
        QStatesActionsValues[indexStateAction][2] = reward(state,action)
        return QStatesActionsValues
    """
    # if next player can win, set Q value to punishment. 
    for nextEntry in emptyEntries(nextState):
        nextAction={"entry":nextEntry,"player":dummyPlayer}
        nextnextState=getNextState(nextState,nextAction)
        if winner(nextnextState)==dummyPlayer:
            QStatesActionsValues[npFindIndex][2] = -1
            return QStatesActionsValues
            """
    """
    # otherwise the dummpy next player chooses a random action (for training).
    nextAction={"entry":random.sample(emptyEntries(nextState),1)[0],"player":dummyPlayer}
    nextnextState=getNextState(nextState,nextAction)
    """
    # update Q value.
    QStatesActionsValues[indexStateAction][2]=(1-learningRate)*getQValue(state,action,QStatesActionsValues)+learningRate*(reward(state,action)-discountFactor*getQValue(nextState,optimalAction(nextState,nextPlayer,QStatesActionsValues),QStatesActionsValues))
    
    return QStatesActionsValues