# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-18 20:21:56
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-19 16:26:27

from __future__ import print_function, unicode_literals
import sqlite3
import os

from constants import DB_NAME, SCHEMA, VALUES


connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def initialize_db():
    """
    Sets up the initial database file and populates it with some random users.
    Calls insert_values_to_db() for inserting values inside the DB file

    >>> import os
    >>> os.path.isfile('sare_log.db')
    True
    >>>

    """
    try:
        cursor.execute(SCHEMA)
    except sqlite3.OperationalError as msg:
        return msg


def insert_values_to_db():
    """
    Populates the database with 'VALUES'

    >>> import sqlite3
    >>> con = sqlite3.connect('sare_log.db')
    >>> cur = con.cursor()
    >>> cur.execute('select * from users').fetchall()
    [('admin', 'Admin', 1, 'admin123'), ('foo', 'bar', 2, 'foo123'), ('john', 'doe', 3, 'john123')]
    >>> 

    """
    try:
        cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", VALUES)
        connection.commit()
        connection.close()
    except sqlite3.OperationalError as msg:
        return msg


def main():
    initialize_db()
    insert_values_to_db()


if __name__ == "__main__":
    main()
