#!/usr/bin/env python

import re
from setuptools import setup

# get author and version from stgithub.py
# since it has some not yet installed dependencies, parsing the file:
head = open('stgithub.py').read(2048)
pattern = """__%s__\\s*=\\s*['"]([^'"]*)['"]"""
kwargs = {keyword: re.search(pattern % keyword, head).group(1)
          for keyword in ('version', 'author', 'license')}

# extract requirements.
# Dev requirements are listed in Makefile (see install_dev)
requirements = [
    line.strip()
    for line in open('requirements.txt')
    if line.strip() and not line.strip().startswith('#')]


# options reference: https://docs.python.org/2/distutils/
# see also: https://packaging.python.org/tutorials/distributing-packages/
setup(
    # whenever you're updating the next three lines
    # please also update oscar.py
    name="strudel.ghutils",
    description="Interface to undocumented GitHub API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[  # full list: https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering'
    ],
    platforms=["Linux", "Solaris", "Mac OS-X", "Unix", "Windows"],
    python_requires='>2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    # entry_points={'console_scripts': [
    #     'console_scripts = stscraper.github:print_limits',
    # ]},
    py_modules=['stgithub'],
    url='https://github.com/cmustrudel/strudel.ghutils',
    install_requires=requirements,
    **kwargs
)