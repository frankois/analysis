# -*- coding: utf-8 -*-

from analysis.common.calendar import get_current_date
from analysis.common.parsing import fetch_soup
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import collections
import config


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
        league_url = f'{root_url}/{broker_country}/{broker_division}'
        return league_url


    @staticmethod
    def fetch_team_archive(search_url, league):
        """Extract team archive."""
        league = config.BROKERS_LEAGUES[league] # TODO: adjust with current config
        soup_data = fetch_soup(search_url)
        panels = soup_data.select("#bloc_anciennes_saisons")[0].select('div[class*="panel"]')

        archive = list()
        for elt in panels:
            if elt.a.text == league:
                archive.append(elt)
                break

        return archive[0]


    @staticmethod
    def fetch_league_list(search_url, country, level):
        soup_data = fetch_soup(search_url)
        soup_data.select("#colonne_droite")

        teams = pd.DataFrame([], columns=['country', 'level','name','url','date'])
        teams.url = [url.a['href'] for url in soup_data.select(".equipe")]
        teams.name = [name.split('.')[-2].split('/')[-1] for name in teams.url]
        # TOMOD: maybe move next to league logic
        teams.country = country
        teams.division = level
        teams.date = get_current_date()

        return teams


    @staticmethod
    def get_draw_statistics(team):
        """Process games to extract relevant data."""
        soup_data = BeautifulSoup(team.archive, 'html.parser')
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
            games.loc[len(games)] = [team.name, status, date, score, isDraw]
            # TODO: sometimes works, sometimes does not
            # For example needed with auxerre ligue 2
            # And need to be removed for grenoble ligue 2
            games = games[::-1].reset_index(drop=True)

        return games


    @staticmethod
    def get_draw_kpis(games):
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
        series_end = games.series[series_reset]
        series_max_counts = collections.Counter(series_end)

        return series_max, series_max_counts