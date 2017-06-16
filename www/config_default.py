#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}