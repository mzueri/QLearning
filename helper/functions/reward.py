from helper.functions.getNextState import getNextState
from helper.functions.winner import winner

def reward(state,action) -> int:
    nextState = getNextState(state,action)
    if winner(nextState)==action["player"]:
        return 1
    #elif winner(nextState)!="nobody":
    #    return -1
    else:
        return 0