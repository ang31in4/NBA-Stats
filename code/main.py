import api
import data_visualization as dv
import os


def run():
    name_input = input('Please enter the name of a player (Please include'
                    ' correct spelling and capitalization): ')
    # Find if the player is valid
    league, player_id = api.find_player(name_input)
    if not (player_id):
        print('Invalid name! Try again.')
        return True

    # Find a list of career seasons to choose from
    career, career_seasons = api.get_player_career_seasons(player_id, league)
    found_season = False
    while not (found_season):
        i = 0
        for player_season in career_seasons:
            print(f'{i}: {player_season}')
            i += 1
        season_input = input('Choose a season by typing its corresponding number: ')
        # Check if valid input
        if not season_input.isdigit():
            print('Please enter a valid number.')
            continue
        season_input = int(season_input)
        if (season_input < 0) or (season_input >= len(career_seasons)):
            print('Invalid season! Try again.')
            continue
        found_season = True


    # Grab data from season
    player_stats = api.get_stats_from_season(career, season_input)

    # Make graph
    dv.make_graph(name_input, player_stats, career_seasons[season_input])
    print(f'Success! Graph created for: {name_input}')
    return False


def main():
    # For personal testing
    os.system('ipconfig /flushdns')
    print()

    print('Welcome! This program will create a bar graph using the statistics'
          ' of an NBA or WNBA player.')
    cond = True

    while cond is True:
        cond = run()


if __name__ == "__main__":
    main()
