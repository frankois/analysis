# -*- coding: utf-8 -*-

CONFIG_NAME = 'config_results'

ARCHIVES_PATH = '../../data/results/archives/'
LEAGUE_LISTS_PATH = '../../data/results/leagues/'

AVAILABLE_COUNTRIES = [
    'france',
    'spain',
    'germany',
    'italy',
    'portugal',
    'belgium',
    'turkey',
    'netherlands'
]

BROKERS = {
    'med' : {
        'class': 'MatchEnDirect',
        'root_url': 'https://www.matchendirect.fr'
    }
}

BROKERS_LEAGUES = {
    'med': {
        'france_1': {
            'country':'france',
            'division':'ligue-1',
            'designation': 'France : Ligue 1',
        },
        'france_2': {
            'country':'france',
            'division':'ligue-2',
            'designation':'France : Ligue 2',
        },
        'spain_1': {
            'country':'espagne',
            'division':'primera-division',
            'designation':'',
        },
        'spain_2': {
            'country':'espagne',
            'division':'segunda-division-liga-adelante',
            'designation':'',
        },
        'germany_1': {
            'country':'allemagne',
            'division':'bundesliga-1',
            'designation':'',
        },
        'germany_2': {
            'country':'allemagne',
            'division':'bundesliga-2',
            'designation':'',
        },
        'italy_1': {
            'country':'italie',
            'division':'serie-a',
            'designation':'',
        },
        'italy_2': {
            'country':'italie',
            'division':'serie-b',
            'designation':'',
        },
        'portugal_1': {
            'country':'portugal',
            'division':'bwin-liga',
            'designation':'',
        },
        'portugal_2': {
            'country':'portugal',
            'division':'liga-vitalis',
            'designation':'',
        },
        'belgium_1': {
            'country':'belgique',
            'division':'jupiler-league',
            'designation':'',
        },
        'belgium_2': {
            'country':'belgique',
            'division':'2e-klasse',
            'designation':'',
        },
        'turkey_1': {
            'country':'turquie',
            'division':'super-lig',
            'designation':'',
        },
        'turkey_2': {
            'country':'turquie',
            'division':'bank-asya-1-lig',
            'designation':'',
        },
        'netherlands_1': {
            'country':'pays-bas',
            'division':'eredivisie',
            'designation':'',
        },
        'netherlands_2': {
            'country':'pays-bas',
            'division':'jupiler-league',
            'designation':'',
        },
    },
}
