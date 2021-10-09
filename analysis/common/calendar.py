# -*- coding: utf-8 -*-

""" Calendar utilities.

"""

import datetime

def get_current_year():
    """ Return the current year."""
    return datetime.date.today().isocalendar()[0]

def get_current_week():
    """ Return the current week."""
    return datetime.date.today().isocalendar()[1]

def get_current_day():
    """ Return the current day."""
    return datetime.date.today().isocalendar()[2]

def get_current_date():
    """ Return the current date."""
    return datetime.datetime.today().strftime('%Y-%m-%d')