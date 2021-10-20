from analysis.results.league import League
from team import Team
from league import League

import config
import sys

if __name__ == "__main__":

    method = sys.argv[1]
    if method == 'team':

        # python main.py team auxerre ligue2 med
        name = sys.argv[2]
        country = sys.argv[3]
        level = sys.argv[4]
        broker = sys.argv[5]

        team = Team(name, country, level, broker)

        team.fetch_archive()
        team.generate_draw_statistics()
        team.generate_draw_kpis()
        team.display()

    elif method == 'league':
        # python main.py league france 1 med
        if sys.argv[2] == 'all':

            broker = 'med'

            level = '1'
            for country in config.AVAILABLE_COUNTRIES:
                print(f'This {country} is now being downloaded for the level {level}')
                league = League(country, level, broker)
                league.fetch_list(1)
                print(f'This {country} download was successful')

            level = '2'
            for country in config.AVAILABLE_COUNTRIES:
                print(f'This {country} is now being downloaded for the level {level}')
                league = League(country, level, broker)
                league.fetch_list(1)
                print(f'This {country} download was successful')

        else:
            country = sys.argv[2]
            level = sys.argv[3]
            broker = sys.argv[4]

        league = League(country, level, broker)
        league.fetch_list(1)
