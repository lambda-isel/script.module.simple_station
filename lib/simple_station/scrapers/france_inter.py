# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from scraper import Scraper


class FranceInter(Scraper):

    ART = {'thumb': 'https://upload.wikimedia.org/wikipedia/fr/thumb/8/8d/France_inter_2005_logo.svg/1024px-France_inter_2005_logo.svg.png'}
    URL = 'https://www.franceinter.fr/'
    ARTIST = 'France Inter'

    @classmethod
    def get_live_channels(cls):
        return [{
            'url': 'https://icecast.radiofrance.fr/franceinter-hifi.aac',
            'label': 'France Inter - Le direct',
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

    @classmethod
    def get_replay_channel(cls):
        return [{
            'scraper_id': cls.get_id(),
            'label': cls.ARTIST,
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                },
            ),
        }]

    @classmethod
    def get_programs(cls):
        soup = cls.get_soup(cls.URL + 'emissions')
        items = soup.find_all('a', 'rich-section-list-item-content-title')
        return [{
            'program_id': item['href'],
            'label': item['title'],
            'art': cls.ART,
            'info': (
                'music', {
                    'album': item['title'],
                    'artist': cls.ARTIST,
                },
            ),
        }
            for item in items
        ]

    @classmethod
    def get_broadcasts(cls, program_id):
        url = cls.URL + program_id
        soup = cls.get_soup(url)
        items = soup.find_all(True, attrs={'data-is-aod': '1'})
        return [{
            'url': item['data-url'],
            'label': item['data-diffusion-title'],
            'art': cls.ART,
            'info': (
                'music', {
                    'album': item['data-emission-title'],
                    'duration': int(item['data-duration-seconds']),
                    'artist': cls.ARTIST,
                    'title': item['data-diffusion-title'],
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


if __name__ == '__main__':
    FranceInter.test(10)
