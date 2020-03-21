import re


class Validator:
    def __init__(self, email):
        self.email = email

    def check_for_symbol(self):
        if re.search("[@.]", self.email) is None:
            return False
        else:
            return True
