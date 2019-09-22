#!/usr/bin/env python
"""
    test_fileio.py
    ~~~~~~~~~~~~~~

    tests the fileio.py module

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import unittest
import pandas as pd

from ancestry import fileio as acs_fio


class TestFileIO(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fileio_csv(self):
        testfname = './ancestry/tests/TestData/test.csv'
        df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5], 'c': [6, 7, 8]})
        acs_fio.to_csv(testfname, df)

        df_in = acs_fio.read_csv(testfname)
        print('orig')
        print(df)
        print('loaded')
        print(df_in)

        pd.testing.assert_frame_equal(df, df_in)

    def test_fileio_excel(self):
        testfname = './ancestry/tests/TestData/test.xlsx'
        df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5], 'c': [6, 7, 8]})
        acs_fio.to_excel(testfname, df)

        df_in = acs_fio.read_excel(testfname)
        print('orig')
        print(df)
        print('loaded')
        print(df_in)

        pd.testing.assert_frame_equal(df, df_in)
