from analysis.results.league import League
from team import Team
from league import League

import sys

if __name__ == "__main__":

    method = sys.argv[1]

    if method == 'team':
        # python main.py team auxerre ligue2 med
        name = sys.argv[2]
        country = sys.argv[3]
        division = sys.argv[4]
        broker = sys.argv[5]

        team = Team(name, country, division, broker)

        team.fetch_archive()
        team.generate_draw_statistics()
        team.generate_draw_kpis()
        team.display()

    elif method == 'league':
        # python main.py league france ligue-1 med
        country = sys.argv[2]
        league = sys.argv[3]
        broker = sys.argv[4]

        league = League(country, league, broker)

        league.fetch_list()
