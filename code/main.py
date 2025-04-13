import api
import data_visualization as dv


def run():

    name = input('Please enter the name of an NBA Player (Please include'
                 ' correct spelling and capitalization): ')

    split_name = name.split(' ')

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

    else:
        print('Invalid name! Try again.')
        return True


def main():
    print('Welcome! This program will create a bar graph using the statistics'
          ' of an NBA player for the 2022-2023 season.')
    cond = True

    while cond is True:
        cond = run()


if __name__ == "__main__":
    main()
