# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-18 21:53:09
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-19 19:11:36

DB_NAME = "sare_log.db"

SCHEMA = "CREATE TABLE users(" \
         "    username TEXT," \
         "    name TEXT," \
         "    serial_no INTEGER," \
         "    password TEXT" \
         ")"

VALUES = (
    ("admin", "Admin", 1, "admin123"),
    ("foo", "bar", 2, "foo123"),
    ("john", "doe", 3, "john123"),
)
