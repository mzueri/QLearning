
def winner(state: list[list[str]]) -> str | None:
    # returns the winner of the game as a string.
    def rowWinner(state, row):
        potentialWinner = state[row][0]
        if potentialWinner not in ["X","O"]:
            return None
        for col in range(1,3):
            if state[row][col] != potentialWinner:
                return None
        return potentialWinner  

    def colWinner(state, col):
        potentialWinner = state[0][col]
        if potentialWinner not in ["X","O"]:
            return None
        for row in range(1,3):
            if state[row][col] != potentialWinner:
                return None
        return potentialWinner

    def leftDiagWinner(state):
        potentialWinner = state[0][0]
        if potentialWinner not in ["X","O"]:
            return None
        for diag in range(1,3):
            if state[diag][diag] != potentialWinner:
                return None
        return potentialWinner

    def rightDiagWinner(state):
        potentialWinner = state[0][2]
        if potentialWinner not in ["X","O"]:
            return None
        for diag in range(1,3):
            if state[diag][2-diag] != potentialWinner:
                return None
        return potentialWinner

    # check if there is a winner in the rows.
    for row in range(3):
        result = rowWinner(state,row)
        if result != None:
            return result
    # check if there is a winner in the columns.
    for col in range(3):
        result = colWinner(state,col)
        if result != None:
            return result
    # check if there is a winner in the diagonals.
    result = leftDiagWinner(state)
    if result != None:
        return result
    result = rightDiagWinner(state)
    if result != None:
        return result
    return None