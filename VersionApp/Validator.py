import re

"""
This class validates the inputed string and if the function is called
it validates for the "@" symbol in the inputed string
"""


class Validator:
    def __init__(self, email):
        self.email = email

    def check_for_symbol(self):
        if re.search("[@.]", self.email) is None:
            return False
        else:
            return True
