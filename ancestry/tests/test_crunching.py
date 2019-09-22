#!/usr/bin/env python
"""
    test_crunching.py
    ~~~~~~~~~~~~~~~~

    tests the chrunching.py module

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import unittest
import pandas as pd
import numpy as np

from ancestry import __ancestry_cols__
from ancestry import crunching as acrunch


class TestCrunching(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_peroson(self):
        all_cols = __ancestry_cols__

        df = pd.DataFrame(
            data={
                'Name-geb': ['mySurnam', 'mySurnam', 'mySurnam2', 'mySurnam'],
                'ID': [1, 2, 3, 4],
                'Vorname': ['myDad', 'myDaught', 'myMoth', 'mySon']
                },
            columns=all_cols)
        print(df)
        print(all_cols)

        newborn = {
            'Name-geb': 'mySurnam',
            'Vorname': 'myGrandson'
        }
        new_dataset = acrunch.add_person(df, newborn)

        print('new dataset')
        print(new_dataset)

        # assert False

    def test_is_consistent(self):
        all_cols = __ancestry_cols__

        df = pd.DataFrame(
            data={
                'Name-geb': ['mySurnam', 'mySurnam', 'mySurnam2', 'mySurnam'],
                'ID': [1, 2, 3, 4],
                'Vorname': ['myDad', 'myDaught', 'myMoth', 'mySon']
                },
            columns=all_cols)

        acrunch.is_consistent(df)

    def test_get_ancestors(self):
        all_cols = __ancestry_cols__

        df = pd.DataFrame(
            data={
                'Name-geb': ['mySurnam', 'mySurnam', 'mySurnam2', 'mySurnam',
                             'mySurnam'],
                'ID': [1, 2, 3, 4, 5],
                'Vorname': ['myDad', 'myDaught', 'myMoth', 'mySon',
                            'myGrandson'],
                '#Mutter': [np.nan, 3, np.nan, 3, 2],
                '#Vater': [np.nan, 1, np.nan, np.nan, np.nan]
                },
            columns=all_cols)

        anc_expect = {
            'mother': [2, {'mother': [3, {}], 'father': [1, {}]}],
            'father': {}
        }

        anc = acrunch.get_ancestors(df, 5)

        print('expected')
        print(anc_expect,)
        print('got')
        print(anc)

        self.assertDictEqual(anc_expect, anc)

        assert True

    def test_count_generations(self):
        ancestrydict = {'father': [3, {'mother': [1, {}]}],
                        'mother': [4, {'father': [5, {'father': [6, {}]}]}]}

        ngen_exp = 3
        ngen = acrunch.count_generations(ancestrydict)

        print('expected', ngen_exp)
        print('got', ngen)
        assert ngen == ngen_exp

        assert True
