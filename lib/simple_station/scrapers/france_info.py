# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from scraper import Scraper


class FranceInfo(Scraper):

    ART = {'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Franceinfo.svg/500px-Franceinfo.svg.png'}
    ARTIST = 'France Info'

    @classmethod
    def get_live_channels(cls):
        return [{
            'url': 'https://icecast.radiofrance.fr/franceinfo-hifi.aac',
            'label': 'France Info - direct radio',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'direct radio',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        },
        ]


if __name__ == '__main__':
    FranceInfo.test(10)
