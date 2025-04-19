
def emptyEntries(state: list[list[str]]) -> list[tuple]:
    # find possible actions
    emptyEntries = []
    for row in range(3):
        for col in range(3):
            if state[row][col]==" ":
                emptyEntries.append((row,col)) 
    return emptyEntries