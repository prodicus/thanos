# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-18 21:53:09
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-20 10:34:42

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
