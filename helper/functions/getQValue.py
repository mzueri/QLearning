from helper.functions.initializationQ import is_initialized

def getQValue(state,action,QStatesActionsValues):
    assert is_initialized(state,action,QStatesActionsValues), "State and action are not definied in Q."
    for i in range(len(QStatesActionsValues)):
        if (state==QStatesActionsValues[i][0]).all() & (action==QStatesActionsValues[i][1]):
            return QStatesActionsValues[i][2]
    return None