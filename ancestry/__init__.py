#!/usr/bin/env python
# import subprocess
import os
import re
import matplotlib
# to use matplotlib in docker containers, we need 'agg'
# to use it in jupyter notebooks, we need
# 'module://ipykernel.pylab.backend_inline'
# currently: in jpnbs, first import pyplot as plt or directly set
# matplotlib.use('module://ipykernel.pylab.backend_inline')
# before importing ancestry.
# currbackend = matplotlib.get_backend()
# if ('ipykernel' not in currbackend) and 'plt' not in locals():
#     matplotlib.use('agg')  # to be able to save figs from docker container


def get_version():
    """Get version from file system, as written during install in
    ancestry/_version.py.
    """
    version_file = os.path.join(os.path.dirname(__file__),
                                '_version.py')
    # see if git can be accessed to write a new version file
    currdir = os.getcwd()
    ancestryroot = os.path.split(os.path.dirname(__file__))[0]
    gitloc = os.path.join(ancestryroot, '.git')
    possible_gitlocs = [gitloc,
                        os.path.join(os.path.split(version_file)[0], '.git')]
    gitloc = [loc for loc in possible_gitlocs if os.path.exists(loc)][0]
    if os.path.exists(gitloc):
        import subprocess
        try:
            os.chdir(ancestryroot)
            git_version_sub = subprocess.check_output(
                    ["git", "describe", "--always"]).decode('UTF-8').rstrip()
            git_version_full = subprocess.check_output(
                    ["git", "describe", "--tags"]).decode('UTF-8').rstrip()
            git_version_nr = re.search(
                    r"([^-]*)", git_version_full, re.M).group(1)
        except:
            git_version_sub = None
            git_version_nr = None
            git_version_full = None
    else:
        git_version_sub = None
        git_version_nr = None
        git_version_full = None
    os.chdir(currdir)

    version_file = os.path.join(os.path.dirname(__file__), '_version.py')
    # print('expecting version file at', version_file)
    if os.path.exists(version_file):
        with open(version_file) as f:
            cached_version_content = f.read().strip()
        try:
            # From http://stackoverflow.com/a/3619714/17498
            # cached_version_nr = re.search(
            #         r"^__version__ = ['\"]([^'\"]*)['\"]",
            #         cached_version_content, re.M).group(1)
            cached_version_sub = re.search(
                    r"^__version_full__ = ['\"]([^'\"]*)['\"]",
                    cached_version_content, re.M).group(1)
            cached_version_full = re.search(
                    r"^__version_full__ = ['\"]([^'\"]*)['\"]",
                    cached_version_content, re.M).group(1)
        except:
            raise RuntimeError("Unable to find version in %s" % version_file)
    else:
        cached_version_sub = None
        # cached_version_nr = None
        cached_version_full = None

    if git_version_sub and git_version_sub != cached_version_sub:
        with open(version_file, 'w') as f:
            f.write('__version__ = "' + git_version_nr + '"\n')
            f.write('__version_full__ = "' + git_version_full + '"\n')
            # print('__version__ = "%s"' % git_version_nr, file=f)
            # print('__version_full__ = "%s"' % git_version_full, file=f)

    return git_version_full or cached_version_full


def get_url():
    """Get url from file system as saved during install in
    ancestry/_url.py.
    """
    url_file = os.path.join(os.path.dirname(__file__), '_url.py')
    if os.path.exists(url_file):
        with open(url_file) as f:
            cached_url_line = f.read().strip()
        try:
            # From http://stackoverflow.com/a/3619714/17498
            cached_url = re.search(r"^__url__ = ['\"]([^'\"]*)['\"]",
                                   cached_url_line, re.M).group(1)
        except:
            raise RuntimeError("Unable to find version in %s" % url_file)
    else:
        cached_url = None

    return cached_url


currdir = os.getcwd()
# get the git revision name and url, keeping the current directory
__version__ = get_version()
URL = get_url()
os.chdir(currdir)


__ancestry_cols__ = [
    'ID', 'Name-geb', 'Vorname', 'Titel', 'akad.', 'andere Vorn', 'geb Datum',
    'Ort', 'gest Datum', 'Ort.1', '#Vater', '#Mutter', 'AnzP', 'verh',
    '#Part', 'Kinder', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9',
    'k10', 'k11', 'k12', 'k13', 'k14', 'kend', 'frau2', 'Kind2', '2k1',
    '2k2', '2k3', '2k4', '2k5', '2k6', '2k7', '2k8', '2k9', '2k10', '2k11',
    '2kend', 'uuid']
