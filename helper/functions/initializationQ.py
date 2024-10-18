
from helper.functions.reward import reward

def npFindIndex(state,action,QStatesActionsValues):
    for i in range(len(QStatesActionsValues)):
        if (state==QStatesActionsValues[i][0]).all() & (action==QStatesActionsValues[i][1]):
                return i

def is_initialized(state,action,QStatesActionsValues):
    if npFindIndex(state,action,QStatesActionsValues)!=None:
        return True
    return False

def initialize(state,action,QStatesActionsValues):
    assert not is_initialized(state,action,QStatesActionsValues), "State and action already initialized."
    QStatesActionsValues.append([state,action,reward(state,action)])
    return QStatesActionsValues