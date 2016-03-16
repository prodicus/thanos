#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''thanos

Usage:
  thanos ship new <name>...
  thanos ship <name> move <x> <y> [--speed=<kn>]
  thanos ship shoot <x> <y>
  thanos mine (set|remove) <x> <y> [--moored|--drifting]
  thanos -h | --help
  thanos --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.0.1"
__author__ = "Tasdik Rahman"
__license__ = "MIT"


def main():
    '''Main entry point for the thanos CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()