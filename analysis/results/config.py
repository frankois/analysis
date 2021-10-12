# -*- coding: utf-8 -*-

CONFIG_NAME = 'config_results'

BROKERS = {
    'med' : {
        'class': 'MatchEnDirect',
        'root_url': 'https://www.matchendirect.fr'
    }
}

BROKER_LEAGUES = {
    'ligue1' : 'France : Ligue 1',
    'ligue2' : 'France : Ligue 2'
}

ARCHIVES_PATH = '../../data/results/archives/'
LEAGUE_LISTS_PATH = '../../data/results/leagues/'
