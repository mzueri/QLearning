import random
import pandas as pd
from helper.learn import learn
from helper.functions.saveAndRead import save_Q_as_json, read_json_as_Q
from helper.play import play
from helper.players import Human, Computer
from helper.board import Board
import json


with open('settings.json', 'r') as file:
    settings = json.load(file)
random.seed(settings["main"]["randomSeed"])


if settings["main"]["resetLearning"]:
    QStatesActionsValues=[]
else:
    QStatesActionsValues=read_json_as_Q("trainedFiles/Q.json")
    

if settings["main"]["train"]:
    QStatesActionsValues = learn(settings["training"]["learningEpisodes"], settings["training"]["learningRate"],settings["training"]["discountFactor"],QStatesActionsValues,settings["training"]["epsilon"])
    save_Q_as_json(QStatesActionsValues,"trainedFiles/Q.json")
    # We save Q in an excel sheet for visualization and manual error checking. 
    # However, saving and writing Q as a data frame is cumbersome, we rather use JSON files (due to 'state' column of lists).
    df_Q = pd.DataFrame(QStatesActionsValues, columns=["state", "action", "Qvalue"])
    df_Q.to_excel('trainedFiles/Q.xlsx',index=False)


if settings["main"]["playGame"]:
    QStatesActionsValues=read_json_as_Q("trainedFiles/Q.json")
    playerStartingInput = input("Who should start? \nType 'm' if you want to start. Otherwise the computer will start. ")
    if playerStartingInput=="m":
        print("OK, you can start.")
        play(Board(),Human("X"),Computer("O"),QStatesActionsValues)
    else:
        print("OK, computer will start.")
        play(Board(),Human("O"),Computer("X"),QStatesActionsValues)