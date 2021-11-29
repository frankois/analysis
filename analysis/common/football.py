# -*- coding: utf-8 -*-

""" Football utilities.

"""

def is_draw(game):
    return int(game.split("-")[0]) == int(game.split("-")[1])