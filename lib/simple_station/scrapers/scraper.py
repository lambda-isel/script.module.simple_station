# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from bs4 import BeautifulSoup
from json import dumps
from requests import get


class Scraper(object):

    @classmethod
    def get_id(cls):
        id = cls.__module__ + '.' + cls.__name__
        return id

    @classmethod
    def get_scraper(cls, id):
        for subclass in cls.__subclasses__():
            if subclass.get_id() == id:
                return subclass
        raise NotImplementedError

    @classmethod
    def get_scrapers(cls):
        scrapers = cls.__subclasses__()
        return scrapers

    @classmethod
    def get_soup(cls, url):
        html = get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    @classmethod
    def show(cls, items):
        for item in items:
            print(dumps(item, indent=4))

    @classmethod
    def test(cls, max_items=-1):
        live_channels = cls.get_live_channels()[0:max_items]
        cls.show(live_channels)
        replay_channel = cls.get_replay_channel()
        if replay_channel:
            cls.show(replay_channel)
            programs = cls.get_programs()[0:max_items]
            cls.show(programs)
            for program in programs:
                broadcasts = cls.get_broadcasts(program['program_id'])
                cls.show(broadcasts[0:max_items])

    @classmethod
    def get_live_channels(cls):
        return []

    @classmethod
    def get_replay_channel(cls):
        return []

    @classmethod
    def get_programs(cls):
        return[]

    @classmethod
    def get_broadcasts(cls, program_id):
        return[]
