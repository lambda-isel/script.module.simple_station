# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from scraper import Scraper


class FranceCulture(Scraper):

    ART = {'thumb': 'https://upload.wikimedia.org/wikipedia/fr/thumb/c/c9/France_Culture_-_2008.svg/1024px-France_Culture_-_2008.svg.png'}
    URL = 'https://www.franceculture.fr/'
    ARTIST = 'France Culture'

    @classmethod
    def get_live_channels(cls):
        items = [{
            'url': 'https://icecast.radiofrance.fr/franceculture-hifi.aac',
            'label': 'France Culture - Le direct',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'Le direct',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        },
        ]
        return items

    @classmethod
    def get_replay_channel(cls):
        items = [{
            'scraper_id': cls.get_id(),
            'label': cls.ARTIST,
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                },
            ),
        }]
        return items

    @classmethod
    def get_programs(cls):
        soup = cls.get_soup(cls.URL + 'emissions')
        items = soup.find_all('a', 'content')
        items = [{
            'program_id': item['href'],
            'label': item.span.text,
            'art': cls.ART,
            'info': (
                'music', {
                    'album': item.span.text,
                    'artist': cls.ARTIST,
                },
            ),
        }
            for item in items
        ]
        return items

    @classmethod
    def get_broadcasts(cls, program_id):
        url = cls.URL + program_id
        soup = cls.get_soup(url)
        items = soup.find_all('button', {'data-btn-type': 'aod'})
        items = [{
            'url': item['data-asset-source'],
            'label': item['data-asset-title'],
            'art': cls.ART,
            'info': (
                'music', {
                    'album': item['data-asset-surtitle'],
                    'duration': int(item['data-duration']),
                    'artist': cls.ARTIST,
                    'title': item['data-asset-title'],
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/mpeg',
            },
            'is_folder': False,
        }
            for item in items
        ]
        return items


if __name__ == '__main__':
    FranceCulture.test(10)
