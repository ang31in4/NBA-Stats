import api
import data_visualization as dv
import os


def print_seasons(seasons: list):
    '''
    Prints out seasons in double columns if more than 8 seasons.
    '''
    print("\n------ Available Seasons ------")
    command_index = 0
    n = len(seasons)
    if n <= 8:
        for s in seasons:
            print(f'[{command_index}]: {s}')
            command_index += 1
    else:
        half = (n + 1) // 2
        for i in range(half):
            left_index = i
            right_index = i + half

            left = f'[{left_index}]: {seasons[left_index]}'
            if right_index < n:
                right = f'[{right_index}]: {seasons[right_index]}'
            else:
                right = ''

            print(f"{left:<16} {right}")
    print()
    

def run():
    name_input = input('Please enter the name of a player (Please include'
                    ' correct spelling and capitalization): ')
    # Find if the player is valid
    league, player_id = api.find_player(name_input)
    if not (player_id):
        print('ERROR: Invalid name! Try again.')
        return True

    # Find a list of career seasons to choose from
    career, career_seasons = api.get_player_career_seasons(player_id, league)
    found_season = False
    print_seasons(career_seasons)
    while not (found_season):
        season_input = input('Choose a season by typing its corresponding number ([s]: to see seasons again): ')
        # Check if valid input
        if season_input == 's':
            print_seasons(career_seasons)
            continue
        if not season_input.isdigit():
            print('\nERROR: Please enter a valid number.\n')
            continue
        season_input = int(season_input)
        if (season_input < 0) or (season_input >= len(career_seasons)):
            print('\nERROR: Invalid season! Try again.\n')
            continue
        found_season = True


    # Grab data from season
    player_stats = api.get_stats_from_season(career, season_input)

    # Make graph
    dv.make_graph(name_input, player_stats, career_seasons[season_input])
    print(f'\nSuccess! Graph created for {name_input} during the {career_seasons[season_input]} season.\n')
    return False


def main():
    # For personal testing
    os.system('ipconfig /flushdns > nul 2>&1')

    print('\nWelcome! This program will create a bar graph using the statistics'
          ' of an NBA or WNBA player. \n')
    cond = True

    while cond is True:
        cond = run()


if __name__ == "__main__":
    main()
