# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-23 21:53:49
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-23 23:51:24

import os
import sqlite3
import unittest

from thanos import *


BASE_DIR = os.path.abspath(os.path.join('.', os.pardir))
PROJECT_DIR = os.path.join(BASE_DIR, 'thanos')


DB_NAME = "sare_log.db"

SCHEMA = "CREATE TABLE users(" \
         "    email TEXT," \
         "    name TEXT," \
         "    serial_no INTEGER," \
         "    password TEXT" \
         ")"

VALUES = (
    ("admin@gmail.com", "Admin", 1, "admin123"),
    ("foo@outlook.com", "bar", 2, "foo123"),
    ("john@yahoo.com", "doe", 3, "john123"),
)

class TestDatabase(unittest.TestCase):

    """
    Defining all kinds of obstenity to be done with the database in
    question
    """

    def _connect(self):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        return (connection ,cursor)

    def set_up(self):
        """
        Sets up the database
        """
        test = os.path.isfile(DB_NAME)
        connection.close()

        self.assertEqual(test, True)

    def test_db_schema_correct(self):
        """checks for the similarity of the schema"""
        connection, cursor = self._connect()
        ## insert crap
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        test = cursor.fetchall()
        result = [('users',)]
        self.assertEqual(test, result)
        
        connection.close()

    def test_db_schema_incorrect(self):
        connection, cursor = self._connect()
        ## insert crap
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        test = False
        self.assertFalse(test)

    def test_db_values_correct(self):
        connection, cursor = self._connect()
        test = cursor.execute('select * from users;').fetchall()
        result = [
            ('admin@gmail.com', 'Admin', 1, 'admin123'),
            ('foo@outlook.com', 'bar', 2, 'foo123'),
            ('john@yahoo.com', 'doe', 3, 'john123')
        ]
        self.assertEqual(test, result)

        connection.close()

    def tear_down(self):
        os.remove(DB_NAME)
        test = os.path.isfile(DB_NAME)
        self.assertEqual(test, False)


if __name__ == "__main__":
    unittest.main()