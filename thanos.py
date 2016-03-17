#!/usr/bin/env python
# -*- coding: utf-8 -*-

r'''thanos

Usage:
  thanos crack (filename)
  thanos feeling-lucky
  thanos --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -a --all      Show all information.
'''

from __future__ import unicode_literals, print_function

from docopt import docopt
from termcolor import colored


__name__ = "thanos"
__version__ = "0.0.1"
__email__ = "prodicus@outlook.com"
__author__ = "Tasdik Rahman"
__license__ = "MIT"


PARENT_DIR = os.path.abspath('.')
DATA_DIR = os.path.join(PARENT_DIR, 'data')


def main():
    '''Main entry point for the thanos CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()