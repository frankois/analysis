# -*- coding: utf-8 -*-

from analysis.config import DATE_FORMAT
from analysis.common.calendar import get_current_date, is_valid_date
from analysis.common.parsing import fetch_soup
from bs4 import BeautifulSoup

import analysis.results.config as config
import datetime
import numpy as np
import pandas as pd
import collections


def format_date(date):
    """Format dates in proper package format."""
    date_today = datetime.datetime.strptime(get_current_date(), DATE_FORMAT)
    date_formatted = ''

    if 'Hier' in date:
        date_formatted = date_today - datetime.timedelta(1)

    elif 'ourd\'hui' in date:
        date_formatted = date_today

    elif 'Demain' in date:
        date_formatted = date_today + datetime.timedelta(1)

    else:
        print(f'This should be a game happening right now --> {date}')

    if date_formatted:
        return date_formatted.strftime(DATE_FORMAT)

    else:
        return 'Running'

class MatchEnDirect:

    def __init__(self):
        pass


    @staticmethod
    def format_team_url(team):
        """Format matchendirect.fr search url for teams."""
        root_url = config.BROKERS['med']['root_url']
        team_url = f'{root_url}/equipe/{team}.html'
        return team_url


    @staticmethod
    def format_league_url(country, level):
        """Format matchendirect.fr search url for leagues."""
        root_url = config.BROKERS['med']['root_url']
        broker_league = f'{country}_{level}'
        broker_country = config.BROKERS_LEAGUES['med'][broker_league]['country']
        broker_division = config.BROKERS_LEAGUES['med'][broker_league]['division']
        broker_league_url = f'{root_url}/{broker_country}/{broker_division}'
        return broker_league_url


    @staticmethod
    def fetch_team_archive(team):
        """Extract team archive."""
        broker_league = f'{team.country}_{team.level}'
        broker_designation = config.BROKERS_LEAGUES['med'][broker_league]['designation']
        print(team.search_url)
        soup_data = fetch_soup(team.search_url)
        panels = soup_data.select("#bloc_anciennes_saisons")[0].select('div[class*="panel"]')

        archive = list()
        for elt in panels:
            if elt.a.text == broker_designation:
                archive.append(elt)
                break

        if archive:
            return archive[0]
        else:
            return 'empty_archive'  # this will still create a file, avoiding to try fetching it in the future


    @staticmethod
    def fetch_team_current(team):
        """Fetch raw data of current games for a single team."""
        broker_league = f'{team.country}_{team.level}'
        broker_designation = config.BROKERS_LEAGUES['med'][broker_league]['designation']
        soup_data = fetch_soup(team.search_url)
        panels = soup_data.select("#livescore")[0].select('div[class*="panel"]')

        current = list()
        for elt in panels:
            if elt.a.text == broker_designation:
                current.append(elt)
                break

        return current[0]


    @staticmethod
    def fetch_league_list(search_url, country, level):
        soup_data = fetch_soup(search_url)
        soup_data.select("#colonne_droite")

        teams = pd.DataFrame([], columns=['country', 'level','name','url','date'])
        teams.url = [url.a['href'] for url in soup_data.select(".equipe")]
        teams.name = [name.split('.')[-2].split('/')[-1] for name in teams.url]
        # TOMOD: maybe move next to league logic
        teams.country = country
        teams.level = level
        teams.date = get_current_date()

        return teams


    @staticmethod
    def get_draw_statistics(team):
        """Process games to extract relevant data."""
        soup_data = BeautifulSoup(team.archive, 'html.parser')
        raw_games = soup_data.find_all('tr')
        games = pd.DataFrame([], columns=['team','status','date','score','draw'])

        for elt in raw_games:

            try:
                date = elt.find_all('td',{'class':'lm2'})[0].text[-8:]
                if not is_valid_date(date):
                    date = format_date(date)

            except IndexError:  # End of proper formatted games
                break

            score = elt.find_all('td',{'class':'lm3'})[0].find_all('span',{'class':'lm3_score'})[0].text.strip().replace(" ","")
            if score: # avoid covid break
                status = "past"
                isDraw = 1 if int(score.split("-")[0]) == int(score.split("-")[1]) else 0
                games.loc[len(games)] = [team.name, status, date, score, isDraw]

        games = games[::-1].reset_index(drop=True)

        return games


    @staticmethod
    def get_draw_kpis(games):
        """Calculation of the most important indicators."""

        # TODO: Fix this workaround
        # Since for some reason `series_detail` starts at 0 when I expected 1 if it
        # is not a draw, I double the line before removing it
        games.loc[-1] = games.loc[0]
        games = games.sort_index().reset_index(drop=True)
        series_detail = games.dropna().groupby('team').draw.apply(lambda x : x.groupby(x.ne(0).cumsum()).cumcount())
        games['series'] = pd.Series(series_detail, dtype=object)
        games = games.iloc[1:,:].reset_index(drop=True)
        # End workaround

        series_max = games.series.max()
        series_reset = np.where(games.series == 0)[0]  # check when the draws happen
        series_reset = series_reset - 1  # fetch the last value before the reset
        series_reset = np.clip(series_reset, 0, None)  # prevent the case where first game is a draw
        series_end = games.series[series_reset]
        series_max_counts = collections.Counter(series_end)

        return series_max, series_max_counts


    @staticmethod
    def get_current_statistics(team):
        """Extract current games."""
        soup_data = BeautifulSoup(str(team.current), 'html.parser')
        raw_games = soup_data.find_all('tr')
        games = pd.DataFrame([], columns=['team','status','date','score','draw'])
        last_game = 0

        for elt in raw_games:

            try:
                date = elt.find_all('td',{'class':'lm2'})[0].text[-8:]
                if not is_valid_date(date):
                    date = format_date(date)

            except IndexError:  # End of proper formatted games
                break

            score = elt.find_all('td',{'class':'lm3'})[0].find_all('span',{'class':'lm3_score'})[0].text.strip().replace(" ","")

            if not score:
                score = -1
                status = "next"
                isDraw = -1
                games.loc[len(games)] = [team.name, status, date, score, isDraw]
                current_game = games.iloc[-1] # store the last "no score game"

            elif score:
                status = "past"
                isDraw = 1 if int(score.split("-")[0]) == int(score.split("-")[1]) else 0
                if date == 'Running':
                    isDraw = -1
                    score = 'x-x'
                games.loc[len(games)] = [team.name, status, date, score, isDraw]
                last_game = games.iloc[-1] # store the last "score game"
                break

        dashboard_games = [last_game, current_game]

        # TODO: Specify this workaround range
        if len(games) > 40:
            print(f'{team.name} is not in this division')
            return -1

        else:
            return dashboard_games