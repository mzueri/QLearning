from helper.functions.gameEnd import gameEnd
from helper.functions.reward import reward
from helper.functions.initializationQ import npFindIndex
from helper.functions.getQValue import getQValue
from helper.functions.getNextState import getNextState
from helper.functions.getOptimalAction import getOptimalAction

def otherMark(currMark):
    marks = ["X","O"]
    assert currMark in marks, f"Not a viable mark: {currMark}." 
    marks.remove(currMark)
    return marks.pop()

def updateQ(state,action,learningRate,discountFactor,QStatesActionsValues):  
    assert not gameEnd(state), "Game is already finished."
    indexStateAction=npFindIndex(state,action,QStatesActionsValues)
    
    currMark=action["mark"]
    nextState=getNextState(state,action)
    nextMark=otherMark(currMark)

    if gameEnd(nextState):
        assert not gameEnd(state), "Game is already finished."
        QStatesActionsValues[indexStateAction][2] = reward(state,action)
        return QStatesActionsValues

    # update Q value.
    QStatesActionsValues[indexStateAction][2]=(1-learningRate)*getQValue(state,action,QStatesActionsValues)+learningRate*(reward(state,action)-discountFactor*getQValue(nextState,getOptimalAction(nextState,nextMark,QStatesActionsValues),QStatesActionsValues))
    
    return QStatesActionsValues