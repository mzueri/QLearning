from helper.functions.reward import reward

def npFindIndex(state,action,QStatesActionsValues) -> int | None:
    for i in range(len(QStatesActionsValues)):
        if state==QStatesActionsValues[i][0] and action==QStatesActionsValues[i][1]:
                return i

def is_initialized(state,action,QStatesActionsValues) -> bool:
    if npFindIndex(state,action,QStatesActionsValues)!=None:
        return True
    return False

def initialize(state,action,QStatesActionsValues) -> list[list]:
    assert not is_initialized(state,action,QStatesActionsValues), "State and action already initialized."
    QStatesActionsValues.append([state,action,reward(state,action)])
    return QStatesActionsValues