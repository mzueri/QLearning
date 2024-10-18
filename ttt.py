import random
import pandas as pd
import numpy as np
from helper.learn import learn
from helper.functions.saveAndRead import save_Q_as_json, read_json_as_Q
from helper.play import play

random.seed(1)
resetLearning = False
train=False
playGame=True

learningRate = 0.1
discountFactor = 0.9



if resetLearning:
    QStatesActionsValues=[]
else:
    QStatesActionsValues=read_json_as_Q("trainedFiles/Q.json")
    
    
if train:
    QStatesActionsValues = learn(100, learningRate,discountFactor,QStatesActionsValues)
    save_Q_as_json(QStatesActionsValues,"trainedFiles/Q.json")
    # We save Q in an excel sheet for visualization and manual error checking. 
    # However, saving and writing Q as a data frame is cumbersome, we rather use JSON files (due to 'state' column of lists).
    df_Q = pd.DataFrame(QStatesActionsValues, columns=["state", "action", "Qvalue"])
    df_Q.to_excel('trainedFiles/Q.xlsx',index=False)


if playGame:
    QStatesActionsValues=read_json_as_Q("trainedFiles/Q.json")
    playerStartingInput = input("Who should start? \n Type 'm' if you want to start. Otherwise the computer will start. ")
    if playerStartingInput=="m":
        playerStarting="human"
        print("OK, you can start. ")
    else:
        playerStarting="computer"
        print("OK, computer will start. ")
    
    play(QStatesActionsValues,playerStarting)


# todo check if action is valid tuple in play()