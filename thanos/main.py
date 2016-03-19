# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-18 18:59:22
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-19 19:42:22

import os

from gui import GuiLogin


PARENT_DIR = os.path.abspath(os.path.join('.', os.pardir))
PROJECT_DIR = os.path.join(PARENT_DIR, 'thanos')


def main():
    """
    Makes an instance of the class 'GuiLogin()'' and runs the mainloop
    """
    GuiLogin().mainloop()

if __name__ == "__main__":
    main()
