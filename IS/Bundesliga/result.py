import pandas as pd
import os
import pickle
import numpy as np

def writeResultHome():
    f = open('resultHome.csv','w')
    f.write('HomeTeam,HomeGoal\n')

    df_home = pd.read_excel('df_both_seasons_home.xlsx')
    df_predict = df_home[df_home['Year'] == 2021]
    home = df_predict.HomeTeam.unique()
    for i in home :
        result = df_home[df_home['HomeTeam'] == i]
        f.write(str(i) + ',' + str(result.iloc[0]['FTHG']) + '\n')
    f.close()

writeResultHome()
def writeResultAway():
    f = open('resultAway.csv','w')
    f.write('AwayTeam,AwayGoal\n')

    df_away = pd.read_excel('df_both_seasons_away.xlsx')
    df_predict = df_away[df_away['Year'] == 2021]
    home = df_predict.HomeTeam.unique()
    for i in home :
        result = df_away[df_away['AwayTeam'] == i]
        f.write(str(i) + ',' + str(result.iloc[0]['FTAG']) + '\n')
    f.close()
writeResultAway()

