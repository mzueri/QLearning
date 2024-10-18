
def otherPlayer(currPlayer):
    players = ["X","O"]
    assert currPlayer in players, "Not a viable player." 
    players.remove(currPlayer)
    return players[0]
