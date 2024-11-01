import json
import urllib.request
from collections import namedtuple

player_data = namedtuple('player_data', ['first_name', 'last_name', 'id'])
player_stats = namedtuple('player_stats', ['season', 'points', 'rebounds',
                                           'assists', 'steals', 'blocks'])


def profile_extract(obj: dict):
    '''
    Extracts information from a json string that has player's
    first name, last name, and id.
    '''
    f_name = obj['first_name']
    l_name = obj['last_name']
    id = obj['id']
    return player_data(f_name, l_name, id)


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


def get_player_database(name: str):
    '''
    Retrieves a json object with all the players with a given name,
    must either be a first name or last name.
    '''

    url_name = 'https://www.balldontlie.io/api/v1/players?per_page=100' + \
               '&search=' + name

    request = urllib.request.Request(url_name)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    data = json.loads(response_data)
    return data['data']


def player_filter(first_name: str, last_name: str):
    '''
    Searches through the player database using the last_name first,
    then looks through first names to see which player has a corresponding
    first and last name given by the user.
    '''
    player_list = get_player_database(last_name)

    index = 0
    while index <= len(player_list) - 1:
        player_tuple = profile_extract(player_list[index])
        if player_tuple.first_name == first_name:
            return player_tuple
        index += 1

    return None


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
