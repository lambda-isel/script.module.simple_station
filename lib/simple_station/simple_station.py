# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from scrapers.scraper import Scraper
from simple_plugin import SimplePlugin


class SimpleStation(SimplePlugin):

    def root(self, live_label='Live', replay_label='Replay'):
        return [
            {'url': self.url_for(self.live_channels), 'label': live_label},
            {'url': self.url_for(self.replay_channels), 'label': replay_label},
        ]

    def live_channels(self):
        self.set_content('songs')
        return [channel for scraper in Scraper.get_scrapers()
                for channel in scraper.get_live_channels()]

    def replay_channels(self):
        self.set_content('artists')
        items = [channel for scraper in Scraper.get_scrapers()
                 for channel in scraper.get_replay_channel()]
        for item in items:
            item['url'] = self.url_for(
                self.programs, scraper_id=item.pop('scraper_id'))
        return items

    def programs(self, scraper_id):
        self.set_content('albums')
        items = Scraper.get_scraper(scraper_id).get_programs()
        for item in items:
            item['url'] = self.url_for(
                self.broadcasts, scraper_id=scraper_id, program_id=item.pop('program_id'))
        return items

    def broadcasts(self, scraper_id, program_id):
        self.set_content('songs')
        return Scraper.get_scraper(scraper_id).get_broadcasts(program_id)
