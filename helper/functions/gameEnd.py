from helper.functions.winner import winner

def gameEnd(state: list[list[str]]) -> bool:
    # returns True if game state is an end state and False otherwise.
    # game ends if there is a winner.
    if winner(state) != None:
        return True
    # otherwise game ends if the grid is full.
    for row in range(3):
        for col in range(3):
            if state[row][col] == " ":
                return False
    return True