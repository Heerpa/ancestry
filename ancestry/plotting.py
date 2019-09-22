#!/usr/bin/env python
"""
    plotting.py
    ~~~~~~~~~~~

    This module provides functionality for visualization.

    :author:    Peter & Heinrich Grabmayr, 2019
    :copyright: Copyright (c) 2019
"""
import matplotlib.pyplot as plt

import ancestry.crunching as acrunch


def tree_up(data, ID, annotate='Vorname'):
    '''Plot a Stammbaum with ID and its ancestors

    Args:
        data: pd.DataFrame
            the whole dataset
        ID: int
            the entry point ID
        annotate: string
            the key to annotate. must be a column name
            (in ancestry.__init__.__ancestry_cols__)

    Returns:
        fig: matplotlib figure
        ax: matplotlib axis
    '''
    ancestors = acrunch.get_ancestors(data, ID)
    ngens = acrunch.count_generations(ancestors)

    fig, ax = plt.subplots()

    currx = 0
    curry = 0

    label = data.loc[data['ID'] == ID, annotate].values[0]
    print(label)
    if ancestors.get('father'):
        next_x = currx-ngens
        ax.plot([currx, next_x], [curry, curry+1], 'grey')
        plot_ancestors(
            ax, data, ancestors['father'],
            next_x, curry+1, ngens, 1, annotate)
    if ancestors.get('mother'):
        next_x = currx+ngens
        ax.plot([currx, next_x], [curry, curry+1], 'grey')
        plot_ancestors(
            ax, data, ancestors['mother'],
            currx+ngens, curry+1, ngens, 1, annotate)
    ax.text(currx, curry, label,
            verticalalignment='center', horizontalalignment='center',
            bbox={'facecolor': 'white', 'edgecolor': 'white'})
    ax.set_xlim([-ngens-2, ngens+2])
    ax.set_ylim([-1, ngens+1])
    ax.set_axis_off()
    return fig, ax


def plot_ancestors(ax, data, ancestors,
                   currx, curry, ngens, currgen, annotate):
    '''recursively plot ancestors
    '''
    label = data.loc[data['ID'] == ancestors[0], annotate].values[0]

    if ancestors[1].get('father'):
        next_x = currx - (ngens-currgen)
        ax.plot([currx, next_x], [curry, curry+1], 'grey')
        plot_ancestors(
            ax, data, ancestors[1]['father'],
            next_x, curry+1, ngens, currgen+1, annotate)
    if ancestors[1].get('mother'):
        next_x = currx + (ngens-currgen)
        ax.plot([currx, next_x], [curry, curry+1], 'grey')
        plot_ancestors(
            ax, data, ancestors[1]['mother'],
            next_x, curry+1, ngens, currgen+1, annotate)

    ax.text(currx, curry, label,
            verticalalignment='center', horizontalalignment='center',
            bbox={'facecolor': 'white', 'edgecolor': 'white'})
