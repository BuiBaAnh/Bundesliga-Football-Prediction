arr =['Bayern Munich', 'Ein Frankfurt', 'FC Koln', 'Stuttgart',
       'Union Berlin', 'Werder Bremen', 'Dortmund', 'RB Leipzig',
       'Wolfsburg', 'Hertha', 'Augsburg', 'Bielefeld', 'Leverkusen',
       'Mainz', "M'gladbach", 'Schalke 04', 'Hoffenheim', 'Freiburg']

def current_year(arr):
    f = open('cur.csv','w')
    f.write('Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HST,AST\n')
    for i in range(len(arr)-1):
        f.write('12/12/2021,'+arr[i]+','+arr[i+1]+',0,0,D,0,0'+'\n')
    for i in range(len(arr)-1):
        f.write('12/12/2021,'+arr[len(arr) - i - 1]+','+arr[len(arr) - i - 2]+',0,0,D,0,0'+'\n')
    f.close()

current_year(arr)