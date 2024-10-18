import random
from helper.functions.getQValue import getQValue
from helper.functions.emptyEntries import emptyEntries
from helper.functions.initializationQ import is_initialized,initialize

def optimalAction(state,player,QStatesActionsValues):
    optimalQValue=float("-inf")
    optimalAction=None
    for entry in emptyEntries(state):
        action={"entry":entry,"player":player}
        # make sure that Q is initialized for this action. 
        if not is_initialized(state,action,QStatesActionsValues):
            QStatesActionsValues=initialize(state,action,QStatesActionsValues)
        if getQValue(state,action,QStatesActionsValues) > optimalQValue:
            optimalQValue=getQValue(state,action,QStatesActionsValues)
            optimalAction=action
    assert optimalQValue!=float("-inf"), "Something went wrong choosing a viable action."
    return optimalAction

def randomAction(state,player):
    return {"entry":random.sample(emptyEntries(state),1)[0],"player":player}
        