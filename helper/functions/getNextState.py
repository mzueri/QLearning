from helper.functions.emptyEntries import emptyEntries

def getNextState(state,action):
    entry=action["entry"]
    try:
        if entry not in emptyEntries(state):
            raise ValueError("Error: This is not a valid action.")
        else:
            nextState = state.copy()
            nextState[entry] = action["player"]
    except:
        print("Error: This is not a valid action.")
        raise
    return nextState