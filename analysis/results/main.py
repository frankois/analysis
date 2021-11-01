from analysis.results.league import League
from team import Team
from league import League

import config
import pandas as pd
import sys

if __name__ == "__main__":

    method = sys.argv[1]
    if method == 'team':

        if sys.argv[2] == 'all':
        # python main.py all france 2 med

            country = sys.argv[3]
            level = sys.argv[4]
            broker = sys.argv[5]

            league_file = f'../../data/results/leagues/league_{country}_{level}_{broker}.csv'
            all_teams = pd.read_csv(league_file)

            for index, row in all_teams.iterrows():
                team_name = row['name']
                team = Team(team_name, country, level, broker)
                print(f'{team_name} --> created')
                team.fetch_archive()
                if team.archive != 'empty_archive':
                    print(f'{team_name} --> archive')
                    team.generate_draw_statistics()
                    print(f'{team_name} --> statistics')
                    team.generate_draw_kpis()
                    print(f'{team_name} --> kpis')
                    # team.display()
                else:
                    print(f'{team_name} have nerver played in this division before')


        else:
        # python main.py team auxerre france 2 med

            team_name = sys.argv[2]
            country = sys.argv[3]
            level = sys.argv[4]
            broker = sys.argv[5]

            team = Team(team_name, country, level, broker)

            team.fetch_archive()
            if team.archive != 'empty_archive':
                team.generate_draw_statistics()
                team.generate_draw_kpis()
                team.display()
            else:
                print(f'{team_name} have nerver played in this division before')

    elif method == 'league':

        if sys.argv[2] == 'all':
        # python main.py league all med

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
        # python main.py league france 1 med

            country = sys.argv[2]
            level = sys.argv[3]
            broker = sys.argv[4]

        league = League(country, level, broker)
        league.fetch_list(1)
