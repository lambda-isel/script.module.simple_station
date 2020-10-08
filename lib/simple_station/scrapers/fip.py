# coding: utf_8
# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2020-present lambda-isel (https://github.com/lambda-isel)

from scraper import Scraper


class FIP(Scraper):

    ART = {'thumb': 'https://upload.wikimedia.org/wikipedia/fr/thumb/d/d5/FIP_logo_2005.svg/1024px-FIP_logo_2005.svg.png'}
    ARTIST = 'FIP'

    @classmethod
    def get_live_channels(cls):
        return [{
            'url': 'https://icecast.radiofrance.fr/fip-hifi.aac',
            'label': 'FIP',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fiprock-hifi.aac',
            'label': 'FIP Rock',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Rock',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipjazz-hifi.aac',
            'label': 'FIP Jazz',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Jazz',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipgroove-hifi.aac',
            'label': 'FIP Groove',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Groove',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fippop-hifi.aac',
            'label': 'FIP Pop',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Pop',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipelectro-hifi.aac',
            'label': 'FIP Electro',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Electro',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipmonde-hifi.aac',
            'label': 'FIP Monde',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Monde',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipreggae-hifi.aac',
            'label': 'FIP Reggae',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Reggae',
                },
            ),
            'properties': {
                'isPlayable': 'true',
                'MimeType': 'audio/aac',
            },
            'is_folder': False,
        }, {
            'url': 'https://icecast.radiofrance.fr/fipnouveautes-hifi.aac',
            'label': 'FIP Nouveautés',
            'art': cls.ART,
            'info': (
                'music', {
                    'artist': cls.ARTIST,
                    'title': 'FIP Nouveautés',
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
    FIP.test(10)
