# -*- coding: utf-8 -*-

""" Calendar utilities.

"""

import datetime

from analysis.config import DATE_FORMAT

def get_current_year():
    """Return the current year."""
    return datetime.date.today().isocalendar()[0]


def get_current_week():
    """Return the current week."""
    return datetime.date.today().isocalendar()[1]


def get_current_day():
    """Return the current day."""
    return datetime.date.today().isocalendar()[2]


def get_current_date():
    """Return the current date."""
    return datetime.datetime.today().strftime(DATE_FORMAT)


def is_valid_date(date):
    """Check if date formatting is valid."""
    try:
        datetime.datetime.strptime(date, DATE_FORMAT)
        return True
    except:
        return False