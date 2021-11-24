# -*- coding: utf-8 -*-

CONFIG_NAME = 'config_results'

ARCHIVES_PATH = '../../data/results/archives/'
LEAGUE_LISTS_PATH = '../../data/results/leagues/'
CURRENTS_PATH = '../../data/results/currents/'

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
            'designation':'Espagne : Liga BBVA',
        },
        'spain_2': {
            'country':'espagne',
            'division':'segunda-division-liga-adelante',
            'designation':'Espagne : Liga Adelante',
        },
        'germany_1': {
            'country':'allemagne',
            'division':'bundesliga-1',
            'designation':'Allemagne : Bundesliga',
        },
        'germany_2': {
            'country':'allemagne',
            'division':'bundesliga-2',
            'designation':'Allemagne : 2. Bundesliga',
        },
        'italy_1': {
            'country':'italie',
            'division':'serie-a',
            'designation':'Italie : Serie A',
        },
        'italy_2': {
            'country':'italie',
            'division':'serie-b',
            'designation':'Italie : Série B',
        },
        'portugal_1': {
            'country':'portugal',
            'division':'bwin-liga',
            'designation':'Portugal : Liga Sagres',
        },
        'portugal_2': {
            'country':'portugal',
            'division':'liga-vitalis',
            'designation':'Portugal : Liga Vitalis',
        },
        'belgium_1': {
            'country':'belgique',
            'division':'jupiler-league',
            'designation':'Belgique : Pro League',
        },
        'belgium_2': {
            'country':'belgique',
            'division':'2e-klasse',
            'designation':'Belgique : 2ème Division',
        },
        'turkey_1': {
            'country':'turquie',
            'division':'super-lig',
            'designation':'Turquie : Lig A',
        },
        'turkey_2': {
            'country':'turquie',
            'division':'bank-asya-1-lig',
            'designation':'Turquie : Lig B',
        },
        'netherlands_1': {
            'country':'pays-bas',
            'division':'eredivisie',
            'designation':'Pays-Bas : Eredivisie',
        },
        'netherlands_2': {
            'country':'pays-bas',
            'division':'jupiler-league',
            'designation':'Pays-Bas : Eerste Divisie',
        },
    },
}
