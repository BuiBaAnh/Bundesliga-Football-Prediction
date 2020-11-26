# import pandas as pd
# import sys

# def result_near_3(df):
#     avg_per_team = {}
#     all_teams = df['HomeTeam'].unique()
#     for t in all_teams:
#         result = pd.DataFrame()
#         for q in all_teams :
#             df_team = df[((df['HomeTeam']==t)&(df['AwayTeam']==q))|((df['HomeTeam']==q)&(df['AwayTeam']==t))].fillna(0)
#             if(len(df_team)!=0):
#                 df_team['RN1'] = df_team.apply(lambda row : row['HomeTeam'] if row['HTGDIFF'] > 0 else 'Draw' if row['HTGDIFF'] == 0 else row['AwayTeam'] ,axis = 1)
#                 # result = df_team['RN'].rolling(1)
#                 # df_team['RN1'] = df_team['RN'].shift(-1)
#                 # df_team['HRN1'] = df_team.apply(lambda row: 1 if row['HomeTeam'] == row['RN1'] else -1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 # df_team['ARN1'] = df_team.apply(lambda row: -1 if row['HomeTeam'] == row['RN1'] else 1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 happen = len(df_team[df_team['HP']==0])
                
#                 df_team['HRWN3'] = df_team.apply(lambda row: 1 if t == row['RN1'] else 0, axis = 1)
#                 result1 = df_team['HRWN3'].rolling(6).mean()
#                 df_team['HWN3'] = result1.shift(-6)
#                 final1 = df_team['HWN3'].iloc[happen-1]
#                 df_team['HWN3'] = df_team.apply(lambda row: row['HWN3'] if row['HP'] ==1 else final1,axis = 1)

#                 df_team['HRLN3'] = df_team.apply(lambda row: 1 if q == row['RN1'] else 0, axis = 1)
#                 result2 = df_team['HRLN3'].rolling(6).mean()
#                 df_team['HLN3'] = result2.shift(-6)
#                 final2 = df_team['HLN3'].iloc[happen-1]
#                 df_team['HLN3'] = df_team.apply(lambda row: row['HLN3'] if row['HP'] ==1 else final2,axis = 1)

#                 df_team['HRDN3'] = df_team.apply(lambda row: 1 if 'Draw' == row['RN1'] else 0, axis = 1)
#                 result3 = df_team['HRDN3'].rolling(6).mean()
#                 df_team['HDN3'] = result3.shift(-6)
#                 final3 = df_team['HDN3'].iloc[happen-1]
#                 df_team['HDN3'] = df_team.apply(lambda row: row['HDN3'] if row['HP'] ==1 else final3,axis = 1)

#                 df_team['ARWN3'] = df_team.apply(lambda row: 1 if q == row['RN1'] else 0, axis = 1)
#                 result4 = df_team['ARWN3'].rolling(6).mean()
#                 df_team['AWN3'] = result4.shift(-6)
#                 final4 = df_team['AWN3'].iloc[happen-1]
#                 df_team['AWN3'] = df_team.apply(lambda row: row['AWN3'] if row['HP'] ==1 else final4,axis = 1)

#                 df_team['ARLN3'] = df_team.apply(lambda row: 1 if t == row['RN1'] else 0, axis = 1)
#                 result5 = df_team['ARLN3'].rolling(6).mean()
#                 df_team['ALN3'] = result5.shift(-6)
#                 final5 = df_team['ALN3'].iloc[happen-1]
#                 df_team['ALN3'] = df_team.apply(lambda row: row['ALN3'] if row['HP'] ==1 else final5,axis = 1)

#                 df_team['ARDN3'] = df_team.apply(lambda row: 1 if 'Draw' == row['RN1'] else 0, axis = 1)
#                 result6 = df_team['ARDN3'].rolling(6).mean()
#                 df_team['ADN3'] = result6.shift(-6)
#                 final6 = df_team['ADN3'].iloc[happen-1]
#                 df_team['ADN3'] = df_team.apply(lambda row: row['ADN3'] if row['HP'] ==1 else final6,axis = 1)
#                 result = pd.concat([result,df_team], axis = 0)
#         avg_per_team[t] = result[result['HomeTeam'] == t].drop(['RN1','HRWN3','HRLN3','HRDN3','ARWN3','ARLN3','ARDN3'], axis = 1)
#     return avg_per_team

# def result_near_opposite(df):
#     avg_per_team = {}
#     all_teams = df['HomeTeam'].unique()
#     for t in all_teams:
#         result = pd.DataFrame()
#         for q in all_teams :
#             df_team = df[((df['HomeTeam']==t)&(df['AwayTeam']==q))|((df['HomeTeam']==q)&(df['AwayTeam']==t))].fillna(0)
#             if(len(df_team)!=0):
#                 # df_team['RN1'] = df_team.apply(lambda row : row['HomeTeam'] if row['HTGDIFF'] > 0 else 'Draw' if row['HTGDIFF'] == 0 else row['AwayTeam'] ,axis = 1)
#                 # result = df_team['RN'].rolling(1)
#                 # df_team['RN1'] = df_team['RN'].shift(-1)
#                 # df_team['HRN1'] = df_team.apply(lambda row: 1 if row['HomeTeam'] == row['RN1'] else -1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 # df_team['ARN1'] = df_team.apply(lambda row: -1 if row['HomeTeam'] == row['RN1'] else 1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 happen = len(df_team[df_team['HP']==0])

#                 df_team['GT'] = df_team.apply(lambda row: row['FTHG'] if t == row['HomeTeam'] else row['FTAG'], axis = 1)
#                 result1 = df_team['GT'].rolling(6).mean()
#                 df_team['GT'] = result1.shift(-6)
#                 final1 = df_team['GT'].iloc[happen-1]
#                 df_team['GT'] = df_team.apply(lambda row: row['GT'] if row['HP'] ==1 else final1,axis = 1)

#                 df_team['GQ'] = df_team.apply(lambda row: row['FTHG'] if q == row['HomeTeam'] else row['FTAG'], axis = 1)
#                 result2 = df_team['GQ'].rolling(6).mean()
#                 df_team['GQ'] = result2.shift(-6)
#                 final2 = df_team['GQ'].iloc[happen-1]
#                 df_team['GQ'] = df_team.apply(lambda row: row['GQ'] if row['HP'] ==1 else final2,axis = 1)

#                 df_team['GTA'] = df_team.apply(lambda row: row['HTGDIFF'] if t == row['HomeTeam'] else row['ATGDIFF'], axis = 1)
#                 result3 = df_team['GTA'].rolling(6).mean()
#                 df_team['GTA'] = result3.shift(-6)
#                 final3 = df_team['GTA'].iloc[happen-1]
#                 df_team['GTA'] = df_team.apply(lambda row: row['GTA'] if row['HP'] ==1 else final3,axis = 1)

#                 df_team['GQA'] = df_team.apply(lambda row: row['HTGDIFF'] if q == row['HomeTeam'] else row['ATGDIFF'], axis = 1)
#                 result4 = df_team['GQA'].rolling(6).mean()
#                 df_team['GQA'] = result4.shift(-6)
#                 final4 = df_team['GQA'].iloc[happen-1]
#                 df_team['GQA'] = df_team.apply(lambda row: row['GQA'] if row['HP'] ==1 else final4,axis = 1)

#                 df_team['HGT'] = df_team.apply(lambda row: row['GT'] if row['HomeTeam'] == t else row['GQ'], axis = 1)
#                 df_team['AGT'] = df_team.apply(lambda row: row['GQ'] if row['HomeTeam'] == t else row['GT'], axis = 1)

#                 df_team['HGTA'] = df_team.apply(lambda row: row['GTA'] if row['HomeTeam'] == t else row['GQA'], axis = 1)
#                 df_team['AGTA'] = df_team.apply(lambda row: row['GQA'] if row['HomeTeam'] == t else row['GTA'], axis = 1)
                
#                 result = pd.concat([result,df_team], axis = 0)
#         avg_per_team[t] = result[result['HomeTeam'] == t].drop(['GT','GQ','GTA','GQA'], axis = 1)
#     return avg_per_team

# def result_near(df):
#     df['HRN1'] = 0
#     df['ARN1'] = 0
#     avg_per_team = {}
#     all_teams = df['HomeTeam'].unique()
#     for t in all_teams:
#         result = pd.DataFrame()
#         for q in all_teams :
#             df_team = df[((df['HomeTeam']==t)&(df['AwayTeam']==q))|((df['HomeTeam']==q)&(df['AwayTeam']==t))].fillna(0)
#             if(len(df_team)!=0):
#                 df_team['RN'] = df_team.apply(lambda row : row['HomeTeam'] if row['HTGDIFF'] > 0 else 'Draw' if row['HTGDIFF'] == 0 else row['AwayTeam'] ,axis = 1)
#                 # result = df_team['RN'].rolling(1)
#                 df_team['RN1'] = df_team['RN'].shift(-1)
#                 happen = len(df_team[df_team['HP']==0])
#                 final = df_team['RN1'].iloc[happen-1]
#                 df_team['RN1'] = df_team.apply(lambda row: row['RN1'] if row['HP'] ==1 else final,axis = 1)
#                 df_team['HRN1'] = df_team.apply(lambda row: 1 if row['HomeTeam'] == row['RN1'] else -1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 df_team['ARN1'] = df_team.apply(lambda row: -1 if row['HomeTeam'] == row['RN1'] else 1 if row['AwayTeam'] == row['RN1'] else 0, axis = 1)
#                 result = pd.concat([result,df_team], axis = 0)
#         avg_per_team[t] = result[result['HomeTeam'] == t].drop(['RN','RN1'], axis = 1)
#     return avg_per_team

# def avg_result_win_near(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['HTGDIFF'] if row['HomeTeam'] == t else row['ATGDIFF'] ,axis = 1)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row: 1 if row['HTGDIFF'] > 0 else 0, axis = 1)
#         result = df_team['{}R5'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}R5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_result_draw_near(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['HTGDIFF'] if row['HomeTeam'] == t else row['ATGDIFF'] ,axis = 1)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row: 1 if row['HTGDIFF'] == 0 else 0, axis = 1)
#         result = df_team['{}R5'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}R5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_result_lose_near(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['HTGDIFF'] if row['HomeTeam'] == t else row['ATGDIFF'] ,axis = 1)
#         df_team['{}R5'.format(a_h_goal_letter)] = df_team.apply(lambda row: 1 if row['HTGDIFF'] < 0 else 0, axis = 1)
#         result = df_team['{}R5'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}R5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_goal_near(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}G5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['FTHG'] if row['HomeTeam'] == t else row['FTAG'] ,axis = 1)
#         result = df_team['{}G5'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}G5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_goal_diff_near(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}GD5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['HTGDIFF'] if row['HomeTeam'] == t else row['ATGDIFF'] ,axis = 1)
#         result = df_team['{}GD5'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}GD5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team


# def avg_goal_near5(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}G5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['FTHG'] if row['HomeTeam'] == t else row['FTAG'] ,axis = 1)
#         result = df_team['{}G5'.format(a_h_goal_letter)].rolling(5).mean()
#         df_team[avg_h_a_diff] = result.shift(-5)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}G5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_goal_diff_near5(df,avg_h_a_diff,a_h_team,a_h_goal_letter):
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[(df['HomeTeam']==t)|(df['AwayTeam']==t)].fillna(0)
#         df_team['{}GD5'.format(a_h_goal_letter)] = df_team.apply(lambda row : row['HTGDIFF'] if row['HomeTeam'] == t else row['ATGDIFF'] ,axis = 1)
#         result = df_team['{}GD5'.format(a_h_goal_letter)].rolling(5).mean()
#         df_team[avg_h_a_diff] = result.shift(-5)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team[df_team[a_h_team] == t].drop(['{}GD5'.format(a_h_goal_letter)], axis = 1)
#     return avg_per_team

# def avg_goal_diff(df, avg_h_a_diff, a_h_team, a_h_goal_letter):
#     """
#     input: 
#         df = dataframe with all results
#         avg_h_a_diff = name of the new column
#         a_h_team = HomeTeam or AwayTeam
#         a_h_goal_letter = 'H' for home or 'A' for away
#     output: 
#         avg_per_team = dictionary with with team as key and columns as values with new column H/ATGDIFF
#     """
#     df[avg_h_a_diff] = 0
#     avg_per_team = {}
#     all_teams = df[a_h_team].unique()
#     for t in all_teams:
#         df_team = df[df[a_h_team]==t].fillna(0)
#         result = df_team['{}TGDIFF'.format(a_h_goal_letter)].rolling(10).mean()
#         df_team[avg_h_a_diff] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[avg_h_a_diff].iloc[happen-1]
#         df_team[avg_h_a_diff] = df_team.apply(lambda row: row[avg_h_a_diff] if row['HP'] ==1 else final,axis = 1)
#         avg_per_team[t] = df_team
#     return avg_per_team

# def avg_goals(df,h_or_a_avg, h_or_a_team, h_or_a_letter):
#     """
#     input: 
#         df = dataframe with all results
#         h_or_a_avg = name of the new column
#         a_h_team = HomeTeam or AwayTeam
#         a_h_goal_letter = 'H' for home or 'A' for away
#     """
#     df[h_or_a_avg] = 0
#     avg_goals_team = {}
#     all_teams = df[h_or_a_team].unique()
#     for t in all_teams:
#         df_team = df[df[h_or_a_team]==t].fillna(0)
#         result = df_team['FT{}G'.format(h_or_a_letter)].rolling(10).mean()
#         df_team[h_or_a_avg] = result.shift(-10)
#         happen = len(df_team[df_team['HP']==0])
#         final = df_team[h_or_a_avg].iloc[happen-1]
#         df_team[h_or_a_avg] = df_team.apply(lambda row: row[h_or_a_avg] if row['HP'] ==1 else final,axis = 1)
#         avg_goals_team[t] = df_team
#     return avg_goals_team

# def from_dict_value_to_df(d):
#     """
#     input = dictionary 
#     output = dataframe as part of all the values from the dictionary
#     """
#     df = pd.DataFrame()
#     for v in d.values():
#         df = df.append(v)
#     return df

# def previous_data(df, h_or_a_team, column):
#     """
#     input: 
#         df = dataframe with all results
#         a_h_team = HomeTeam or AwayTeam
#         column = column selected to get previous data from
#     output:
#         team_with_past_dict = dictionary with team as a key and columns as values with new 
#                               columns with past value
#     """
#     d = dict()
#     team_with_past_dict = dict()
#     all_teams = df[h_or_a_team].unique()
#     for team in all_teams:
#         n_games = len(df[df[h_or_a_team]==team])
#         team_with_past_dict[team] = df[df[h_or_a_team]==team]
#         for i in range(1, n_games):
#             d[i] = team_with_past_dict[team].assign(
#                 result=team_with_past_dict[team].groupby(h_or_a_team)[column].shift(-i)
#             ).fillna({'{}_X'.format(column): 0})
#             team_with_past_dict[team]['{}_{}'.format(column, i)] = d[i].result
#     return team_with_past_dict
import pandas as pd
import sys

def avg_goal_diff(df, avg_h_a_diff, a_h_team, a_h_goal_letter):
    """
    input: 
        df = dataframe with all results
        avg_h_a_diff = name of the new column
        a_h_team = HomeTeam or AwayTeam
        a_h_goal_letter = 'H' for home or 'A' for away
    output: 
        avg_per_team = dictionary with with team as key and columns as values with new column H/ATGDIFF
    """
    df[avg_h_a_diff] = 0
    avg_per_team = {}
    all_teams = df[a_h_team].unique()
    for t in all_teams:
        df_team = df[df[a_h_team]==t].fillna(0)
        result = df_team['{}TGDIFF'.format(a_h_goal_letter)].rolling(10).mean()
        df_team[avg_h_a_diff] = result.shift(-9)
        avg_per_team[t] = df_team
    return avg_per_team

def avg_goals(df,h_or_a_avg, h_or_a_team, h_or_a_letter):
    """
    input: 
        df = dataframe with all results
        h_or_a_avg = name of the new column
        a_h_team = HomeTeam or AwayTeam
        a_h_goal_letter = 'H' for home or 'A' for away
    """
    df[h_or_a_avg] = 0
    avg_goals_team = {}
    all_teams = df[h_or_a_team].unique()
    for t in all_teams:
        df_team = df[df[h_or_a_team]==t].fillna(0)
        result = df_team['FT{}G'.format(h_or_a_letter)].rolling(10).mean()
        df_team[h_or_a_avg] = result.shift(-9)
        avg_goals_team[t] = df_team
    return avg_goals_team

def from_dict_value_to_df(d):
    """
    input = dictionary 
    output = dataframe as part of all the values from the dictionary
    """
    df = pd.DataFrame()
    for v in d.values():
        df = df.append(v)
    return df

def previous_data(df, h_or_a_team, column):
    """
    input: 
        df = dataframe with all results
        a_h_team = HomeTeam or AwayTeam
        column = column selected to get previous data from
    output:
        team_with_past_dict = dictionary with team as a key and columns as values with new 
                              columns with past value
    """
    d = dict()
    team_with_past_dict = dict()
    all_teams = df[h_or_a_team].unique()
    for team in all_teams:
        n_games = len(df[df[h_or_a_team]==team])
        team_with_past_dict[team] = df[df[h_or_a_team]==team]
        for i in range(1, n_games):
            d[i] = team_with_past_dict[team].assign(
                result=team_with_past_dict[team].groupby(h_or_a_team)[column].shift(-i)
            ).fillna({'{}_X'.format(column): 0})
            team_with_past_dict[team]['{}_{}'.format(column, i)] = d[i].result
    return team_with_past_dict
    