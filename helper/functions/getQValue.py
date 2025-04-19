from helper.functions.initializationQ import is_initialized

def getQValue(state: list[list[str]],action: dict,QStatesActionsValues: list) -> int | None:
    assert is_initialized(state,action,QStatesActionsValues), "State and action are not definied in Q."
    for i in range(len(QStatesActionsValues)):
        if state==QStatesActionsValues[i][0] and action==QStatesActionsValues[i][1]:
            return QStatesActionsValues[i][2]