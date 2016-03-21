# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-19 00:10:33
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-21 09:28:07

"""
Contains the class 'GuiLogin()' which will be imported by 'main.py' to be run

References:
[1]: http://www.python-course.eu/tkinter_variable_classes.php
[2]: https://pymotw.com/2/sqlite3/#row-objects
[3]: http://stackoverflow.com/a/1301369/3834059
"""

from tkinter import *
import sqlite3

from termcolor import colored

from constants import DB_NAME
from utils import email_validator, password_validator


class GuiLogin(Frame):

    """
    The tkinter class which defines the structure and functions of th GUI
    """

    def __init__(self):
        """
        Initializes the tkinter object and aggregates the data to be displayed
        """
        # Create and add GUI components to the screen
        Frame.__init__(self)
        self.master.title("Login Screen")

        self.master.minsize(300, 200)
        self.pack()

        self._usernameLabel = Label(self, text="Enter email")
        self._usernameLabel.pack()

        """StringVar() makes self._usernameVar store "" by default
        Ref: [1]
        """
        self._usernameVar = StringVar()
        self._usernameEntry = Entry(
            self, textvariable=self._usernameVar, width=30)
        self._usernameEntry.pack()

        self._passwordLabel = Label(self, text="Enter password")
        self._passwordLabel.pack()

        self._passwordVar = StringVar()
        self._passwordEntry = Entry(
            self, textvariable=self._passwordVar, width=30)
        self._passwordEntry.pack()

        self._loginButton = Button(self, text="Login", command=self._login)
        self._loginButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(
            self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()

        self._quitButton = Button(self, text="Quit", command=self._quit)
        self._quitButton.pack()

    def _quit(self):
        """
        Exits from the GUI that we are running
        """
        exit(0)

    def _db_connect(self):
        """
        Called by the '_authenticate()' method.

        Connects to the database and returns the cursor object.

        :returns: The cursor object to the databas 'DB_NAME'
        """
        connection = sqlite3.connect(DB_NAME)
        # Using row objects
        # ref: [2]
        connection.row_factory = sqlite3.Row
        """
        row_factory will allow us to refer to the columns by their names
        instead of their index numbers
        """
        return (connection, connection.cursor())

    # more on private and protected classes
    # ref: [3]
    def _authenticate(self, email, password):
        """
        Called by the method '_login()'

        Unpacks the **kwargs key pair value to get email and password
        and query it to the database in an unsecure way to demonstrate SQL
        injection

        :param email: email entered by the user
        :param password: Password entered by the user
        :returns: None or a result from the database based on the success of
                  the user query
        """
        print(
            colored("Attempting to login with email:'{0}' "
                    "password:'{1}'".format(email, password),
                    "yellow"
                    )
        )

        connection, cursor = self._db_connect()

        # validating username and password entered by the user
        if not email_validator(email) and password_validator(password):
            self._resultVar.set("Gotcha you invalid Input!")

        else:
            # Defining the vulnerable SQL query which will be used to exploit the database
            # usign SQL injection
            # SQL_QUERY = '''SELECT name FROM users WHERE email = '%s' and password = '%s' ''' % (email, password)

            # --- Secure method ---
            ## parameterized SQL query
            cursor.execute("""SELECT name FROM users
                              WHERE
                              email=? and password=?
                           """,(email, password)
                           )

            # print("Executing the SQL query")
            # print(colored(SQL_QUERY, "yellow"))


            # Will assume here that the login failed, if no rows are returned back
            # by the database
            response = None
            # This loop won't run if no results are returned.
            for row in cursor:
                response = row['name']  # Extract name from first row
                break

            connection.close()
            return response

    def _login(self):
        """
        Calls the 

        parses the user input for email and password and calls the
        '_authenticate()' 



        TO-DO: To add input validation using WTForms, which will address the
               issue(I guess!)
        """
        kwargs = {
            "email": self._usernameVar.get(),
            "password": self._passwordVar.get()
        }

        response = self._authenticate(**kwargs)

        if response is None:    # 'is' checks for object similarity.
            result_of_query = "email or password was incorrect"
        else:
            result_of_query = "Logged in! :)"

        self._resultVar.set(result_of_query)
