#!/usr/bin/env python
"""
    crunching.py
    ~~~~~~~~~~~~

    This module provides functionality to check for consistency, etc.

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import uuid
import numpy as np

from ancestry import __ancestry_cols__


def add_person(data, new_person):
    '''adds a new person to the dataset.
    ID and uuid are assigned automatically

    Args:
        data: pd.DataFrame
            dataset of present genealogy
        new_person: dict
            descdription of the new person. allowed keys are defined in
            ancestry.__init__.__ancestry_cols__

    Returns:
        new_data: pd.DataFrame
            the new dataset including the new person
    '''
    # make sure no undefined keys are present
    for k in new_person.keys():
        assert k in __ancestry_cols__

    new_person['ID'] = data['ID'].max() + 1
    new_person['uuid'] = str(uuid.uuid4())

    print(data)
    print(new_person)

    idx = data.index.max() + 1
    for k, v in new_person.items():
        data.loc[idx, k] = v
    return data


def is_consistent(data):
    '''checks whether data is consistent

    Args:
        data: pd.DataFrame
            dataset of present genealogy
    '''
    # make sure
    assert len(data['ID']) == len(data.index)


def get_ancestors(data, ID):
    '''gets the IDs of all present ancestors of ID

    Args:
        data: pd.DataFrame
            dataset of present genealogy
        ID: int
            the person to query

    Returns:
        ancestors: dicts
            returns all IDs of ancestors:
                {'father': [IDdad, {'father': [IDgrandpa],
                                    'mother': [IDgrandma]}],
                 'mother': [IDmom, {}]}
    '''
    familydict = {}
    id_mother = data.loc[data['ID'] == ID, '#Mutter'].values[0]
    if np.isnan(id_mother):
        familydict['mother'] = {}
    else:
        familydict['mother'] = [int(id_mother), get_ancestors(data, id_mother)]

    id_father = data.loc[data['ID'] == ID, '#Vater'].values[0]
    if np.isnan(id_father):
        familydict['father'] = {}
    else:
        familydict['father'] = [int(id_father), get_ancestors(data, id_father)]

    if (not familydict['mother']) and (not familydict['father']):
        familydict = {}

    return familydict


def count_generations(ancestors):
    '''counts the number of generations of an ancestrydict

    Args:
        ancestors: nested dicts
            IDs of ancestors in the form of:
                {'father': [IDdad, {'father': [IDgrandpa],
                                    'mother': [IDgrandma]}],
                 'mother': [IDmom, {}]}
    Returns:
        ngenerations : int
            the maximum number generations of ancestors
    '''
    if isinstance(ancestors, dict):
        # for the lowest generation
        ancestors = [np.nan, ancestors]
    if ancestors[1].get('father'):
        ngen_father = count_generations(ancestors[1].get('father'))
    else:
        ngen_father = -1
    if ancestors[1].get('mother'):
        ngen_mother = count_generations(ancestors[1].get('mother'))
    else:
        ngen_mother = -1
    return max(ngen_father+1, ngen_mother+1)
