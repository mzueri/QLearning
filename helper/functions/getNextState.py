from helper.functions.emptyEntries import emptyEntries
import copy

def getNextState(state,action):
    entry=action["entry"]
    try:
        if entry not in emptyEntries(state):
            raise ValueError("Error: This is not a valid action.")
        else:
            nextState = copy.deepcopy(state)
            nextState[entry[0]][entry[1]] = action["player"]
    except:
        print("Error: This is not a valid action.")
        raise
    return nextState