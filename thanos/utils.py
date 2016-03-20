# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-20 10:52:15
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-20 11:03:29

"""
Tries to validate the email address entered by the user to the GUI.

References:
[1]: http://stackoverflow.com/q/3217682/3834059
[*]: http://stackoverflow.com/q/201323/3834059
"""

import re
import string

# ref: [1]
REGEX_EXP = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
PUNCTUATIONS = string.punctuation

def email_validator(email):
    """
    A simple regex which checks whether the entered user email is a valid
    email address or not
    """
    if len(email) > 6:
        if re.match(REGEX_EXP, email) != None:
            return True
    return False

def password_validator(password):
    """
    Rejects a password if the password has special characters in it
    """
    if PUNCTUATIONS in password:
        return False
    else:
        return True