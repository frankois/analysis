# -*- coding: utf-8 -*-

""" Database models.

"""

from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    league_id = Column(Integer, ForeignKey("league.id"))


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    team_home = Column(Integer, ForeignKey("team.id"))
    team_away = Column(Integer, ForeignKey("team.id"))
    score_home = Column(Integer)
    score_away = Column(Integer)
    date = Column(DateTime)
    is_draw = Column(Boolean, default=None)


class League(Base):
    __tablename__ = "league"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    level = Column(Integer)


class Bet(Base):
    __tablename__ = "bet"
    id = Column(Integer, primary_key=True)
    game = Column(Integer, ForeignKey("game.id"))
    odd = Column(Float)
    stake = Column(Float)
    gain = Column(Float, default=None)
