from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import PerMode36

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

def get_stats_from_season(user_player_id: str, user_input_season: str):
    '''
    Retrieves stats from the selected season
    '''
    career = playercareerstats.PlayerCareerStats(per_mode36=PerMode36.per_game, player_id=user_player_id)
    df = career.get_data_frames()[0]
    return df.iloc[user_input_season]