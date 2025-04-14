from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.parameters import PerMode36
import pandas as pd

def find_player(player_name: str):
    '''
    Checks if the inputted player name is in the nba_api database.
    '''
    # Search both NBA and WNBA players
    all_league_players = [players.get_players(), players.get_wnba_players()]
    league_names = ["NBA", "WNBA"]

    for i, league in enumerate(all_league_players):
        try:
            player_id_data = [player for player in league if player["full_name"] == player_name][0]
            league = league_names[i]
            return league, player_id_data['id']
        except IndexError:
            continue  # Try next league

    # If player not found in any league
    return None, None

def get_player_career_seasons(user_player_id: str, league: str):
    '''
    Extracts a list containing every season the player has played.
    '''
    # NBA
    if (league == 'NBA'):
        career = playercareerstats.PlayerCareerStats(per_mode36=PerMode36.per_game, player_id=user_player_id)
    # WNBA
    else:
        career = playercareerstats.PlayerCareerStats(per_mode36=PerMode36.per_game, player_id=user_player_id, league_id_nullable=10)
    df = career.get_data_frames()[0]
    return df, df["SEASON_ID"].tolist()

def get_stats_from_season(career: pd.DataFrame, user_input_season: str):
    '''
    Retrieves stats from the selected season
    '''
    return career.iloc[user_input_season]