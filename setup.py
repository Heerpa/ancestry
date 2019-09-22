import os
import re
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    """Get version from git or file system.
    If this is a git repository, try to get the version number by
    running ``git describe``, then store it in
    ancestry/_version.py. Otherwise, try to load the version number
    from that file. If both methods fail, quietly return None.
    """
    git_version_nr = None
    git_version_sub = None
    git_version_full = None
    if os.path.exists(os.path.join(os.path.dirname(__file__), '.git')):
        import subprocess
        try:
            git_version_sub = subprocess.check_output(
                    ["git", "describe", "--always"]).decode('UTF-8').rstrip()
            git_version_full = subprocess.check_output(
                    ["git", "describe", "--tags"]).decode('UTF-8').rstrip()
            git_version_nr = re.search(
                    r"([^-]*)", git_version_full, re.M).group(1)
            # git_version = subprocess.Popen(['git', 'describe'],
            #                                stdout=subprocess.PIPE).communicate(
            #                                  )[0].strip().decode('utf-8')
        except:
            pass

    version_file = os.path.join(os.path.dirname(__file__), 'ancestry',
                                '_version.py')
    if os.path.exists(version_file):
        with open(version_file) as f:
            cached_version_content = f.read().strip()
            # print(cached_version_content)
        try:
            # From http://stackoverflow.com/a/3619714/17498
            # print(re.search(
            #         r"^__version__ = ['\"]([^'\"]*)['\"]",
            #         cached_version_content, re.M))
            cached_version_nr = re.search(
                    r"^__version__ = ['\"]([^'\"]*)['\"]",
                    cached_version_content, re.M).group(1)
            # print(re.search(
            #         r"^__version__ = ['\"]([^'\"]*)['\"]",
            #         cached_version_content, re.M))
            cached_version_sub = re.search(
                    r"^__version_full__ = ['\"]([^'\"]*)['\"]",
                    cached_version_content, re.M).group(1)
        except:
            raise RuntimeError("Unable to find version in %s" % version_file)
    else:
        cached_version_sub = None
        cached_version_nr = None

    if git_version_sub and git_version_sub != cached_version_sub:
        with open(version_file, 'w') as f:
            if isinstance(git_version_nr, str):
                f.write('__version__ = "'+git_version_nr+'"\n')
            if isinstance(git_version_full, str):
                f.write('__version_full__ = "'+git_version_full+'"\n')
            # print('__version__ = "%s"' % git_version_nr, file=f)
            # print('__version_full__ = "%s"' % git_version_full, file=f)

    return git_version_nr or cached_version_nr


def get_url():
    """Get url from git or file system.
    If this is a git repository, try to get the url by
    running ``git describe``, then store it in
    ancestry/_url.py. Otherwise, try to load the version number
    from that file. If both methods fail, quietly return None.
    """
    git_url = None
    if os.path.exists(os.path.join(os.path.dirname(__file__), '.git')):
        import subprocess
        try:
            git_url = subprocess.check_output(
                    ["git", "config",
                     "--get", "remote.origin.url"]).decode('UTF-8').rstrip()
        except:
            pass

    url_file = os.path.join(os.path.dirname(__file__), 'ancestry',
                            '_url.py')
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

    if git_url and git_url != cached_url:
        with open(url_file, 'w') as f:
            f.write('__url__ = "%s"'.format(git_url))
            # print('__url__ = "%s"' % git_url, file=f)

    return git_url or cached_url


setup(
    name="ancestry",
    # version=get_version(),
    author="Peter & Heinrich Grabmayr",
    description=("A python based software suite to " +
                 "manage and plot ancestry data."),
    license="GPL-2",
    keywords="ancestors, descendents",
    # url=get_url(),
    # entry_points={'console_scripts':
    #               ['ancestry = ancestry.__main__:main']},
    packages=find_packages(exclude=['tests']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Topic :: Utilities",
        # "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent"
    ],
)
