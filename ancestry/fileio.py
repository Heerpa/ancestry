#!/usr/bin/env python
"""
    fileio.py
    ~~~~~~~~~

    This module provides functionality for file in and output.

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import pandas as pd


def read_csv(fname):
    '''Reads a csv file (semicolon separated) into a pandas dataframe.

    Args:
        fname : str
            file name of the csv file

    Returns:
        data : pd.DataFrame
            the content of the file
    '''
    return pd.read_csv(fname, sep=';', index_col=0)


def to_csv(fname, data):
    '''Writes data to a csv file (semicolon separated).

    Args:
        fname : str
            file name of the csv file
        data : pd.DataFrame
            the content to write to file
    '''
    data.to_csv(fname, sep=';', encoding='utf-8')


def read_excel(fname):
    '''Reads an escel file into a pandas dataframe.

    Args:
        fname : str
            file name of the xlsx file

    Returns:
        data : pd.DataFrame
            the content of the file
    '''
    return pd.read_excel(fname, index_col=0)


def to_excel(fname, data):
    '''Writes data to an excel file.

    Args:
        fname : str
            file name to write
        data : pd.DataFrame
            data to write
    '''
    data.to_excel(fname)
