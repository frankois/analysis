# -*- coding: utf-8 -*-

""" Bets main.

"""

import analysis.results.config as config_results
import datetime
import pandas as pd
import sys

from analysis.results.team import Team as Teams_cls
from analysis.common.calendar import is_valid_date
from analysis.results.brokers import format_date
from analysis.config import DATE_FORMAT
from bs4 import BeautifulSoup
from config import DB_CONN_URI_SQLITE
from models import Team, League, Game
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database


if __name__ == "__main__":

    # Init DB
    force = int(sys.argv[1])

    if force == 1:
        if database_exists(DB_CONN_URI_SQLITE):
            drop_database(DB_CONN_URI_SQLITE)

    engine = create_engine(DB_CONN_URI_SQLITE, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
    Base.metadata.create_all(engine)  # DB file creation

    # Add models in the DB
    Team.__table__.create(engine)
    League.__table__.create(engine)
    Game.__table__.create(engine)

    # LEAGUES
    # Fill leagues
    broker = 'med'
    leagues = config_results.BROKERS_LEAGUES[broker]

    # available_leagues
    available_leagues = []
    for key, item in enumerate(leagues):
        country, level = item.split('_')
        name = leagues[item]['division']
        league = League(name=name, country=country, level=level)
        session.add(league)

    session.commit()
    # ---

    # TEAM
    # Fill teams
    available_leagues = session.query(League).all()

    for league in available_leagues:
        country = league.country
        level = league.level
        league_file = f'../../data/results/leagues/league_{country}_{level}_{broker}.csv'
        teams = pd.read_csv(league_file)
        query = session.query(League).filter_by(country=country, level=level).all()[0]

        teams['league_id'] = query.id
        teams = teams[['name', 'league_id']]
        teams.to_sql('team', con=engine, if_exists='append', index=False)

    # ---

    # GAMES
    # Fill games
    available_teams = session.query(Team).all()

    for team in available_teams:
        query = session.query(League).filter_by(id=team.league_id).all()[0]
        level = query.level
        country = query.country
        team_name = team.name
        broker = 'med'
        team = Teams_cls(team_name, country, level, broker)
        soup_data = BeautifulSoup(team.archive, 'html.parser')
        raw_games = soup_data.find_all('tr')

        # Create method PARSE_game

        for game in raw_games:

            try:
                date = game.find_all('td',{'class':'lm2'})[0].text[-8:]
                if not is_valid_date(date):
                    date = format_date(date)
                date = datetime.datetime.strptime(date, DATE_FORMAT)

            except IndexError:  # End of proper formatted games
                break


            score = game.find_all('td',{'class':'lm3'})[0].find_all('span',{'class':'lm3_score'})[0].text.strip().replace(" ","")
            if score:
                score_home, score_away = score.split('-')

                try:
                    team_home = game.find_all('span',{'class':'lm3_eq1'})[0].text.strip().replace(" ","")
                    # query = session.query(Team).filter_by(name=team_home.lower()).all()[0]
                    # team_home = query.id
                    team_away = game.find_all('span',{'class':'lm3_eq2'})[0].text.strip().replace(" ","")
                    # query = session.query(Team).filter_by(name=team_away.lower()).all()[0]
                    # team_away = query.id

                except:
                    import ipdb; ipdb.set_trace()

                is_draw = (score_home == score_away)
                game = Game(team_home=team_home, team_away=team_away, score_home=score_home, score_away=score_away, date=date)
                session.add(game)

    session.commit()
