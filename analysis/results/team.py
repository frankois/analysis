# -*- coding: utf-8 -*-

from analysis.results.brokers import MatchEnDirect # Change to conditional import

import matplotlib.pyplot as plt

import config
import os

class Team:

    def __init__(self, name, country, level, broker):
        self.name = name
        self.country = country
        self.level = level
        self.broker = eval(config.BROKERS[broker]['class'])
        self.search_url = self.broker.format_team_url(self.name)

        self.archive_name = f'archive_{self.name}_{self.level}_{broker}.html'
        self.archive_path = f'{config.ARCHIVES_PATH}{self.archive_name}'

        self.draw_statistics = None
        self.draw_kpis = None
        self.series_max = None

    @property
    def has_archive(self):
        if os.path.isfile(self.archive_path): # TOMOD: move this in commons
            return True
        else:
            return False


    @property
    def archive(self):
        if not self.has_archive:
            print('This team does not have archive, please fetch it first')
        elif self.has_archive:
            with open(self.archive_path, 'r') as f:
                archive = f.read()
            return archive


    def fetch_archive(self, force=0):
        if self.has_archive and not force:
            print('This team already have its archive')
        else:
            archive = self.broker.fetch_team_archive(self)
            with open(self.archive_path, 'w') as f:
                f.write(str(archive))


    def generate_draw_statistics(self):
        if self.draw_statistics:
            print('Statistics for this team are already available')
        else:
            self.draw_statistics = self.broker.get_draw_statistics(self)


    def generate_draw_kpis(self):
        if self.draw_kpis:
            print('KPIs for this team are already available')
        else:
            self.series_max, self.draw_kpis = self.broker.get_draw_kpis(self.draw_statistics)


    def display(self):
        if not self.draw_kpis:
            print('Please generate KPIs before')
        else:
            plt.bar(list(self.draw_kpis.keys()), self.draw_kpis.values(), color='g')
            plt.show()
