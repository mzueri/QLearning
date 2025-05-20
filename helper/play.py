from helper.board import Board
from helper.players import Human,Computer
from helper.functions.initializationQ import is_initialized, initialize
from helper.players import switchPlayers
import copy
from helper.gui import TicTacToeGUI

def play(QStatesActionsValues):

    playerStartingInput = input("Who should start? \nType 'm' if you want to start. Otherwise the computer will start. ")
    if playerStartingInput=="m":
        print("OK, you can start.")
        player1=Human("X")
        player2=Computer("O")
    else:
        print("OK, computer will start.")
        player1=Computer("X")
        player2=Human("O")

    game_gui=TicTacToeGUI(player1,player2,QStatesActionsValues)
    game_gui.setup_ui()
    game_gui.run()
    
    """
    while not board.gameEnd():
        
        if currPlayer.is_human():
            human_action=currPlayer.choose_action(board)
            currPlayer.apply_action(board,human_action)
            board.printState()
        else:
            for entry in board.emptyEntries():
                action={"entry":entry,"mark":currPlayer.mark}
                if not is_initialized(board.state,action,QStatesActionsValues):
                    QStatesActionsValues=initialize(copy.deepcopy(board.state),action,QStatesActionsValues)

            optimal_action=currPlayer.choose_optimal_action(board,QStatesActionsValues)
            currPlayer.apply_action(board,optimal_action)
            print("Computer makes the following move: ")
            board.printState()   
        
        # next player's turn, switch the current player
        currPlayer=switchPlayers(currPlayer,player1,player2)

    # display the result to the user.
    if board.winner()==player1.mark:
        print("Player 1 wins!")
    elif board.winner()==player2.mark:
        print("Player 2 wins!")
    else: 
        print("Nobody wins!")
        """