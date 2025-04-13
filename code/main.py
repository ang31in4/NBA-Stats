import api
import data_visualization as dv


def run():

    name_input = input('Please enter the name of an NBA Player (Please include'
                 ' correct spelling and capitalization): ')

    # Find if the player is valid
    player_id = api.find_player(name_input)
    if not (player_id):
        print('Invalid name! Try again.')
        return True
    
    # Find a list of career seasons to choose from
    career_seasons = api.get_player_career_seasons(player_id)
    found_season = False
    while not (found_season):
        i = 0
        for player_season in career_seasons:
            print(f'{i}: {player_season}')
            i += 1
        season_input = input('Choose a season by typing its corresponding number: ')
        # Check if input is a digit
        if not season_input.isdigit():
            print('Please enter a valid number.')
            continue
        # Check if input is within range
        season_input = int(season_input)
        if (season_input < 0) or (season_input >= len(career_seasons)):
            print('Invalid season! Try again.')
            continue
        found_season = True
    

"""
    if len(split_name) == 2:

        player_profile = api.player_filter(split_name[0], split_name[1])
        if player_profile is None:
            print('Player does not exist! Try again.')
            return True

        player_stats = api.get_player_stats(player_profile.id)
        if player_stats is None:
            print('Must be a current player! Try again.')
            return True

        dv.make_graph(player_profile, player_stats)
        print(f'Success! Graph created for: {name}')
        return False
"""

def main():
    print('Welcome! This program will create a bar graph using the statistics'
          ' of an NBA player.')
    cond = True

    while cond is True:
        cond = run()


if __name__ == "__main__":
    main()
