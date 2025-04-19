from helper.functions.emptyEntries import emptyEntries
from helper.functions.initializationQ import initialize, is_initialized
from helper.functions.getQValue import getQValue


def getOptimalAction(state: list[list[str]], mark: str, QStatesActionsValues: list) -> dict:
        
        optimalQValue=float("-inf")
        optimalAction={}

        for entry in emptyEntries(state):
            action={"entry":entry,"mark":mark}
            # make sure that Q is initialized for this action. 
            if not is_initialized(state,action,QStatesActionsValues):
                QStatesActionsValues=initialize(state,action,QStatesActionsValues)
            qValue=getQValue(state,action,QStatesActionsValues)

            assert qValue!=None, "Q-Value should not be undefined."
            if qValue > optimalQValue:
                optimalQValue=qValue
                optimalAction=action
                
        return optimalAction