from django.shortcuts import render
from django.http import JsonResponse
from .models import Match
from django.core import serializers
from django.db.models import Avg, Max, Min, Q
from django.forms.models import model_to_dict
import os
import pandas as pd
from datetime import datetime
from pytz import timezone
import json
# Create your views here.

def index(request):
    round = 1
    series ='Bundesliga'
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(series=series,round=round)))
    for match in match_list:
        if check_time(match['fields']['startdate']):
            df_resultHome  = pd.read_csv(os.path.join(os.path.dirname(__file__),'../../../IS/'+ series + '/resultHome.csv'))
            df_resultAway  = pd.read_csv(os.path.join(os.path.dirname(__file__),'../../../IS/'+ series + '/resultAway.csv'))
            for i in match_list:
                home = i['fields']['HomeTeam']
                away = i['fields']['AwayTeam']
                resultHome = df_resultHome[(df_resultHome['HomeTeam'] == home)] # == home
                resultAway = df_resultAway[(df_resultAway['AwayTeam'] == away)] # ==away
                i['fields']['homegoals'] = int(resultHome.iloc[0]['HomeGoal'])
                i['fields']['awaygoals'] = int(resultAway.iloc[0]['AwayGoal'])


    best_match = Match.objects.filter(series=series,round=round).get(Q(homename='Bayern Munich')|Q(awayname='Bayern Munich'))
    if check_time(best_match.startdate):
        best_match.homegoals = '-'
        best_match.awaygoals = '-'
    round_max = Match.objects.filter(series=series).aggregate(Max('round'))

    context = {
        'round': round,
        'round_list': range(2, round_max['round__max'] + 1),
        'series': series,
        'series_slug': series.lower().replace(' ','-'),
        'match_num': len(match_list),
        'matches': match_list,
        'best_match': best_match,
        }
    return render(request,'matches.html', context=context)   

def match_detail(request, series, round, match_id):
    match_object = Match.objects.get(pk = match_id)
    if check_time(match_object.startdate):
        match_object.homegoals = '-'
        match_object.awaygoals = '-'
    data = serializers.serialize('json', [match_object,])
    struct = json.loads(data)
    match = struct[0]
    context = {
        'match': match,
        'round': round,
        'series': series,
        }
    return render(request,'match-live.html', context=context)   

def matches(request, series, round):
    series = convert_slug(series)
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(series=series, round=round)))
    for match in match_list:
        if check_time(match['fields']['startdate']):
            df_resultHome  = pd.read_csv(os.path.join(os.path.dirname(__file__),'../../../IS/'+ series + '/resultHome.csv'))
            df_resultAway  = pd.read_csv(os.path.join(os.path.dirname(__file__),'../../../IS/'+ series + '/resultAway.csv'))
            for i in match_list:
                home = i['fields']['HomeTeam']
                away = i['fields']['AwayTeam']
                resultHome = df_resultHome[(df_resultHome['HomeTeam'] == home)] # == home
                resultAway = df_resultAway[(df_resultAway['AwayTeam'] == away)] # ==away
                i['fields']['homegoals'] = int(resultHome.iloc[0]['HomeGoal'])
                i['fields']['awaygoals'] = int(resultAway.iloc[0]['AwayGoal'])
    star_team = ''
    if (series=='Premier League'):
        star_team = 'Manchester United'
    elif (series=='Bundesliga'):
        star_team = 'Bayern Munich'
    elif (series=='La Liga'):
        star_team = 'Real Madrid'
    elif (series=='Serie A'):
        star_team = 'Juventus'
    best_match = Match.objects.filter(series=series,round=round).get(Q(homename=star_team)|Q(awayname=star_team))
    if check_time(best_match.startdate):
        best_match.homegoals = '-'
        best_match.awaygoals = '-'
    best_match_obj = serializers.serialize('json', [ best_match, ])

    data = {
        'round': round,
        'match_num': len(match_list),
        'matches': match_list,
        'best_match': json.loads(best_match_obj)[0]
        }
    return JsonResponse(data)

def convert_slug(series):
    res = ''
    for i in series.split('-'):
        res += i.capitalize() + ' '
    return res[:len(res)-1]

def check_time(dt):
    now_time = datetime.now(timezone('Antarctica/DumontDUrville'))
    startdate= datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
    if startdate < now_time:
        return False
    return True