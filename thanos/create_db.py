# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-18 20:21:56
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-23 22:37:27

import sqlite3

from constants import DB_NAME, SCHEMA, VALUES


connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def initialize_db():
    """
    Sets up the initial database file and populates it with some random users.
    Calls insert_values_to_db() for inserting values inside the DB file
    """
    try:
        cursor.execute(SCHEMA)
    except sqlite3.OperationalError as msg:
        return msg


def insert_values_to_db():
    """
    Populates the database with 'VALUES'
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
