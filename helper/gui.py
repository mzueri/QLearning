import tkinter as tk
import copy
from helper.players import Human, Computer
from helper.board import Board
from helper.players import Player
from helper.players import switchPlayers
from helper.functions.initializationQ import is_initialized, initialize


class TicTacToeGUI():

    
    def __init__(self, player1: Player, player2: Player, QStatesActionsValues):
        # constructor only sets up data attributes

        # initialize the board
        self.board=Board()
        
        # initialize the players
        self.currPlayer=player1
        self.player1=player1
        self.player2=player2

        # computer actions
        self.QStatesActionsValues=QStatesActionsValues



    def setup_ui(self):

        # GUI setup
        self.root=tk.Tk()
        self.root.geometry("500x500") # size of window
        self.root.title("Tic Tac Toe") # set title

        label=tk.Label(text="Make your next move.",font=("Arial",18))
        label.pack(padx=20,pady=20)
        
        buttonframe=tk.Frame(self.root)
        buttonframe.columnconfigure(0,weight=1) # weight is the proportion of size the button takes in the buttonframe.
        # 0 is the index of the column in the buttonframe widget. 
        buttonframe.columnconfigure(1,weight=1) 
        buttonframe.columnconfigure(2,weight=1)
        buttonframe.rowconfigure(0, weight=1)
        buttonframe.rowconfigure(1, weight=1)
        buttonframe.rowconfigure(2, weight=1)
        self.btn1=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(1,self.currPlayer.mark))
        self.btn1.grid(row=0,column=0,sticky="nsew") # sticky extends the buttons to the edge of the window.
        self.btn2=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(2,self.currPlayer.mark))
        self.btn2.grid(row=0,column=1,sticky="nsew")
        self.btn3=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(3,self.currPlayer.mark))
        self.btn3.grid(row=0,column=2,sticky="nsew")
        self.btn4=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(4,self.currPlayer.mark))
        self.btn4.grid(row=1,column=0,sticky="nsew") 
        self.btn5=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(5,self.currPlayer.mark))
        self.btn5.grid(row=1,column=1,sticky="nsew")
        self.btn6=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(6,self.currPlayer.mark))
        self.btn6.grid(row=1,column=2,sticky="nsew")
        self.btn7=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(7,self.currPlayer.mark))
        self.btn7.grid(row=2,column=0,sticky="nsew") 
        self.btn8=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(8,self.currPlayer.mark))
        self.btn8.grid(row=2,column=1,sticky="nsew")
        self.btn9=tk.Button(buttonframe, text=" ", font=("Arial", 18), command=lambda: self.click_cell(9,self.currPlayer.mark))
        self.btn9.grid(row=2,column=2,sticky="nsew")
        buttonframe.pack(expand=True, fill="both")




    def run(self):
        
        if not self.currPlayer.is_human():
            #self.root.after(2000, self.computer_move)
            self.computer_move()
            self.currPlayer=switchPlayers(self.currPlayer,self.player1,self.player2)
        
        self.root.mainloop()



    def computer_move(self):

        # get the optimal action
        for entry in self.board.emptyEntries():
            action={"entry":entry,"mark":self.currPlayer.mark}
            if not is_initialized(self.board.state,action,self.QStatesActionsValues):
                self.QStatesActionsValues=initialize(copy.deepcopy(self.board.state),action,self.QStatesActionsValues)

        optimal_action=self.currPlayer.choose_optimal_action(self.board,self.QStatesActionsValues)
        
        # update the board by applying the action
        self.board.applyAction(optimal_action)
        #print("Computer makes the following move: ")
        
        # update GUI
        cell=self.entry_to_cell_mapping(optimal_action["entry"])
        mark=optimal_action["mark"]
        button = getattr(self, f'btn{cell}')
        button.config(text=mark, state="disabled", font=("Arial",18))

        # check if the game has ended. If it has ended show the result of the game to the user.
        if self.board.gameEnd():
            self.root.destroy()
            # display the result to the user.
            if self.board.winner()==self.player1.mark:
                print("Player 1 wins!")
            elif self.board.winner()==self.player2.mark:
                print("Player 2 wins!")
            else: 
                print("Nobody wins!")
            return



    def click_cell(self, cell, mark):

        # update board
        entry=self.cell_to_entry_mapping(cell)
        self.board.applyAction({"entry":entry,"mark":mark})

        # update the GUI
        # update the clicked cell
        button = getattr(self, f'btn{cell}')
        button.config(text=mark, state="disabled", font=("Arial",18))

        # check if the game has ended. If it has ended show the result of the game to the user.
        if self.board.gameEnd():
            self.root.destroy()
            # display the result to the user.
            if self.board.winner()==self.player1.mark:
                print("Player 1 wins!")
            elif self.board.winner()==self.player2.mark:
                print("Player 2 wins!")
            else: 
                print("Nobody wins!")
            return

        self.currPlayer=switchPlayers(self.currPlayer,self.player1, self.player2)

        if not self.currPlayer.is_human():
            #self.root.after(2000, self.computer_move)
            self.computer_move()
            self.currPlayer=switchPlayers(self.currPlayer,self.player1,self.player2)



    def entry_to_cell_mapping(self,entry: tuple[int]) -> int:
        return entry[0]*3+entry[1]+1
    

    def cell_to_entry_mapping(self,cell: int) -> tuple[int]:
        assert cell in list(range(1, 10)), "ERROR: Invalid cell."
        if cell==1:
            return (0,0)
        elif cell==2:
            return (0,1)
        elif cell==3:
            return (0,2)
        elif cell==4:
            return (1,0)
        elif cell==5:
            return (1,1)
        elif cell==6:
            return (1,2)
        elif cell==7:
            return (2,0)
        elif cell==8:
            return (2,1)
        else:
            return (2,2)
