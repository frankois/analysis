# -*- coding: utf-8 -*-

""" Parsing utilities.

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetch_soup(urlPage):
    html = urlopen(urlPage)
    hData = html.read()
    return BeautifulSoup(hData, features="lxml")