# -*- coding: utf-8 -*-

from analysis.common.calendar import get_current_date
from analysis.config import ROOT_DIR
from analysis.results.brokers import MatchEnDirect # Change to conditional import

import analysis.results.config as config
import os
import pandas as pd


class League:
    """ Fetching listing of all teams of a specific league
    Based on www.matchendirect.fr website
    """

    def __init__(self, country, level, broker):
        self.country = country
        self.level = level
        self.broker = eval(config.BROKERS[broker]['class'])

        self.search_url = self.broker.format_league_url(self.country, self.level)

        self.league_list_name = f'league_{self.country}_{self.level}_{broker}.csv'
        self.league_list_path = os.path.join(ROOT_DIR, config.LEAGUE_LISTS_PATH, self.league_list_name)


    @property
    def date(self):
        return get_current_date()


    @property
    def has_league_list(self):
        if os.path.isfile(self.league_list_path): # TOMOD: move this in commons
            return True
        else:
            return False


    @property
    def league_list(self):
        if not self.has_league_list:
            print('This team does not have league list, please fetch it first')
        elif self.has_league_list:
            with open(self.league_list_path, 'r') as f:
                league_list = f.read()
            return league_list


    def fetch_list(self, force=0, verbose=0):
        if self.has_league_list and not force:
            if verbose:
                print('This league already has its list')
            else:
                pass
        else:
            league_list = self.broker.fetch_league_list(self.search_url, self.country, self.level)
            league_list.to_csv(self.league_list_path)
