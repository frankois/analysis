# -*- coding: utf-8 -*-

""" Fetching listing of all teams of a specific league
Based on www.matchendirect.fr website
"""

from analysis.common.parsing import fetch_soup
from analysis.common.calendar import get_current_date
import config
import sys
import pandas as pd

if __name__ == "__main__":
    country = sys.argv[1]
    league = sys.argv[2]

    date = "today"
    search_url = f"{config.BROKER}/{country}/{league}"

    soup_data = fetch_soup(search_url)
    soup_data.select("#colonne_droite")

    teams = pd.DataFrame([], columns=['league','name','url','date'])
    teams.url = [url.a['href'] for url in soup_data.select(".equipe")]
    teams.name = [name.split('.')[-2].split('/')[-1] for name in teams.url]
    teams.league = league
    teams.date = get_current_date()

    print(teams)