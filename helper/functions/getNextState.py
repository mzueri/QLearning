from helper.functions.emptyEntries import emptyEntries
import copy

def getNextState(state: list[list[str]],action: dict) -> list[list[str]]:
    entry=action["entry"]
    try:
        if entry not in emptyEntries(state):
            raise ValueError("Error: This is not a valid action.")
        else:
            nextState = copy.deepcopy(state)
            nextState[entry[0]][entry[1]] = action["mark"]
    except:
        print("Error: This is not a valid action.")
        raise
    return nextState