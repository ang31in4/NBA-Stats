import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


def make_graph(player_name: str, player_stats: pd.Series, season_id: str):
    '''
    Writes a bar graph into an html file, using player data
    '''
    header = f'{player_name} - Averages per Game {season_id}'

    stats_list = [
        {'Statistic Type': 'Points', 'Value': player_stats['PTS']},
        {'Statistic Type': 'Rebounds', 'Value': player_stats['REB']},
        {'Statistic Type': 'Assists', 'Value': player_stats['AST']},
        {'Statistic Type': 'Steals', 'Value': player_stats['STL']},
        {'Statistic Type': 'Blocks', 'Value': player_stats['BLK']}
    ]

    fig = px.bar(stats_list, x='Statistic Type', y='Value', text_auto=True)

    fig.update_layout(title=header, title_x=0.5)

    fig.update_traces(textfont_size=20, textposition='outside')

    fig.write_html('stat_bar.html')
