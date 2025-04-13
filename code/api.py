import json
from collections import namedtuple
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import PerMode36

#player_data = namedtuple('player_data', ['first_name', 'last_name', 'id'])
#player_stats = namedtuple('player_stats', ['season', 'points', 'rebounds',
                                           #'assists', 'steals', 'blocks'])

def find_player(player_name: str):
    '''
    Checks if the inputted player name is in the nba_api database.
    '''
    all_nba_players = players.get_players()
    try:
        player_id_data = [player for player in all_nba_players if player["full_name"] == player_name][0]
        return player_id_data['id']
    except IndexError:
        return None

def get_player_career_seasons(user_player_id: str):
    '''
    Extracts a list containing every season the player has played.
    '''
    career = playercareerstats.PlayerCareerStats(per_mode36=PerMode36.per_game, player_id=user_player_id)
    df = career.get_data_frames()[0]
    return df["SEASON_ID"].tolist()


"""
def stats_extract(obj: dict):
    '''
    Extracts information from a json string that has the stats
    of a player.
    '''
    season = obj['season']
    points = obj['pts']
    rebounds = obj['reb']
    assists = obj['ast']
    steals = obj['stl']
    blocks = obj['blk']
    return player_stats(season, points, rebounds, assists, steals, blocks)



def get_player_stats(id: int):
    '''
    Retrieves a player's stats using their id as a parameter
    '''

    url_name = 'https://www.balldontlie.io/api/v1/season_averages' + \
               '?player_ids[]=' + str(id)

    request = urllib.request.Request(url_name)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    data = json.loads(response_data)
    if len(data['data']) == 0:
        return None
    else:
        return stats_extract(data['data'][0])
"""
