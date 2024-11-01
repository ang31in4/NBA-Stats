from collections import namedtuple
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


def make_graph(player_data: namedtuple, player_stats: namedtuple):
    '''
    Writes a bar graph into an html file, using player data
    '''
    header = player_data.first_name + ' ' + \
        player_data.last_name + ' ' + \
        '- Averages per Game (2022-2023)'

    stats_list = [
        {'Statistic Type': 'Points', 'Value': player_stats.points},
        {'Statistic Type': 'Rebounds', 'Value': player_stats.rebounds},
        {'Statistic Type': 'Assists', 'Value': player_stats.assists},
        {'Statistic Type': 'Steals', 'Value': player_stats.steals},
        {'Statistic Type': 'Blocks', 'Value': player_stats.blocks}
    ]

    fig = px.bar(stats_list, x='Statistic Type', y='Value', text_auto=True)

    fig.update_layout(title=header, title_x=0.5)

    fig.update_traces(textfont_size=20, textposition='outside')

    fig.write_html('stat_bar.html')
