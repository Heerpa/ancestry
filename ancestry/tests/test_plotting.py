#!/usr/bin/env python
"""
    test_plotting.py
    ~~~~~~~~~~~~~~~~

    tests the plotting.py module

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ancestry import __ancestry_cols__
from ancestry import plotting as aplot


class TestPlotting(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip('not implemented')
    def test_tree_up(self):
        all_cols = __ancestry_cols__

        df = pd.DataFrame(
            data={
                'Name-geb': ['mySurnam', 'mySurnam', 'mySurnam2', 'mySurnam',
                             'mySurnam', 'otherfamily'],
                'ID': [1, 2, 3, 4, 5, 6],
                'Vorname': ['myDad', 'myDaught', 'myMoth', 'mySon',
                            'myGrandson', 'grandsonsdad'],
                '#Mutter': [np.nan, 3, np.nan, 3, 2, np.nan],
                '#Vater': [np.nan, 1, np.nan, np.nan, 6, np.nan]
                },
            columns=all_cols)

        fig, ax = aplot.tree_up(df, ID=5)

        plt.savefig('./ancestry/tests/TestData/tree_up.png')

        assert False
