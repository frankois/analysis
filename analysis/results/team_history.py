# -*- coding: utf-8 -*-

""" Fetching results of a team for its all time history
Based on www.matchendirect.fr website
"""

from analysis.common.parsing import fetch_soup
from analysis.common.calendar import get_current_date
import collections
import config
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def format_url_matchendirect(team):
    """Format matchendirect.fr search url."""

    return f'https://www.matchendirect.fr/equipe/{team}.html'

def get_team_history(soup_data, league):
    """Extract team history."""
    panels = soup_data.select("#bloc_anciennes_saisons")[0].select('div[class*="panel"]')

    history = list()
    for elt in panels:
        if elt.a.text == league: # remove hardcoded string
            history.append(elt)
            break

    return history[0]

def get_draw_statistics(soup_data, team_name):
    """Process games to extract relevant data."""
    raw_games = soup_data.find_all('tr')
    games = pd.DataFrame([], columns=['team','status','date','score','draw'])

    for elt in raw_games[1:]: # remove first misc
        try:
            date = elt.find_all('td',{'class':'lm2'})[0].text[-8:]
        except IndexError:  # End of proper formatted games
            break

        score = elt.find_all('td',{'class':'lm3'})[0].find_all('span',{'class':'lm3_score'})[0].text.strip().replace(" ","")
        if bool(score):
            status = "past"
            isDraw = 1 if int(score.split("-")[0]) == int(score.split("-")[1]) else 0
        elif not bool(score):
            status = "current"
            score = "x-x"
            isDraw = None
        games.loc[len(games)] = [team_name, status, date, score, isDraw]

    return games


def draw_series(games):
    """Calculation of the most important indicators."""
    # TODO: Fix this workaround
    # Since for some reason `series_detail` starts at 0 when I expected 1 if it
    # is not a draw, I double the line before removing it
    games.loc[-1] = games.loc[0]
    games.index = games.index + 1
    games = games.sort_index()
    series_detail = games.dropna().groupby('team').draw.apply(lambda x : x.groupby(x.ne(0).cumsum()).cumcount())
    games['series'] = pd.Series(series_detail, dtype=object)
    games = games.iloc[1:]
    # End workaround

    series_max = series_detail.max()

    series_reset = np.where(games.series == 0)[0]
    series_nodraw_max = games.series[series_reset]
    series_nodraw_max_clean = series_nodraw_max[series_nodraw_max!=0] # removes zeros

    return games, series_max, series_nodraw_max

def plot_series(series, method):
    if method == 1:
        # numpy way
        unique, counts = np.unique(series, return_counts=True)
        to_plot = dict(zip(unique, counts))

    elif method == 2:
        # std collections way
        to_plot = collections.Counter(series)

    plt.bar(list(to_plot.keys()), to_plot.values(), color='g')
    plt.show()

if __name__ == "__main__":
    team = sys.argv[1]
    search_url = format_url_matchendirect(team)
    soup_data = fetch_soup(search_url)

    for league in config.FRENCH_LEAGUES:
        try:
            history = get_team_history(soup_data, league)
            games = get_draw_statistics(history, team)
            games = games[::-1].reset_index(drop=True)

            games, series_max, series_nodraw_max = draw_series(games)
            print(f'The maximum nodraw series in {league} was {series_max} games')

        except IndexError:
            print(f'Sorry, {team} have never played in {league}')

    plot_series(series_nodraw_max, 2)