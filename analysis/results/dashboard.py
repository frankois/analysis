import config
import config_dashboard

from analysis.common.parsing import fetch_soup
import pandas as pd

class Dashboard:

    def __init__(self, broker):
        self.broker = broker
        self.leagues = config.BROKERS_LEAGUES[self.broker]
        # self.dashboard_teams = config_dashboard.DASHBOARD_TEAMS

    @property
    def dashboard_teams(self):
        teams_dict = config_dashboard.TEAMS[self.broker]
        teams_all = []
        for _, league in enumerate(teams_dict):
            for team in teams_dict[league]:
                teams_all.append(team)

        return teams_all


    @property
    def available_leagues(self):
        """Return list of available league."""
        available_leagues = []
        for key, item in enumerate(self.leagues):
            country, level = item.split('_')
            available_leagues.append([country, level])

        return available_leagues

    @property
    def available_teams(self):
        """Return list of available teams."""
        available_teams = pd.DataFrame()
        for league in self.available_leagues:
            country = league[0]
            level = league[1]
            league_file = f'../../data/results/leagues/league_{country}_{level}_{self.broker}.csv'
            new_teams = pd.read_csv(league_file)
            teams_to_concat = [available_teams, new_teams]
            available_teams = pd.concat(teams_to_concat)

        return available_teams

    @property
    def teams(self):
        """Return list of dashboard teams."""
        filtered_teams = self.available_teams.loc[self.available_teams.name.isin(self.dashboard_teams)]

        return filtered_teams.values.tolist()